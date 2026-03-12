# @ohos.security.huks (通用密钥库系统)

向应用提供密钥库能力，包括密钥管理及密钥的密码学操作等功能。

HUKS所管理的密钥可以由应用导入或者由应用调用HUKS接口生成。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { huks } from '@kit.UniversalKeystoreKit';
```

#### HuksParam

调用接口使用的options中的properties数组中的param。

**系统能力：** SystemCapability.Security.Huks.Core

名称类型只读可选说明tag[HuksTag](#ZH-CN_TOPIC_0000002529445359__hukstag)否否

标签。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

valueboolean|number|bigint|Uint8Array否否

标签对应值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### HuksOptions

调用接口使用的options。

**系统能力：** SystemCapability.Security.Huks.Core

名称类型只读可选说明propertiesArray<[HuksParam](#ZH-CN_TOPIC_0000002529445359__huksparam)>否是

属性，用于存HuksParam的数组。默认为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

inDataUint8Array否是

输入数据。默认为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### HuksSessionHandle9+

huks Handle结构体。

**系统能力：** SystemCapability.Security.Huks.Core

名称类型只读可选说明handlenumber否否

表示无符号整数类型的handle值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

challengeUint8Array否是

表示[initSession](#ZH-CN_TOPIC_0000002529445359__huksinitsession9)操作之后获取到的challenge信息。默认为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### HuksReturnResult9+

调用接口返回的result。

**系统能力：** SystemCapability.Security.Huks.Core

名称类型只读可选说明outDataUint8Array否是

表示输出数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

propertiesArray<[HuksParam](#ZH-CN_TOPIC_0000002529445359__huksparam)>否是

表示属性信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

certChainsArray<string>否是

表示证书链数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### HuksListAliasesReturnResult12+

调用接口返回的result。

**系统能力**：SystemCapability.Security.Huks.Extension

名称类型只读可选说明keyAliasesArray<string>否否

表示密钥别名集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### huks.generateKeyItem9+

generateKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>) : void

生成密钥。使用callback异步回调。

基于密钥不出TEE原则，此接口不会返回密钥材料内容，只用于表示此次调用是否成功。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于存放生成key所需TAG。其中密钥使用的算法、密钥用途、密钥长度为必选参数。callbackAsyncCallback<void>是回调函数。当生成密钥成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000012Device environment or input parameter abnormal.12000013queried credential does not exist.12000014memory is insufficient.12000015Failed to obtain the security information via UserIAM.12000017The key with same alias is already exist.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 以生成ECC256密钥为例 */
let keyAlias: string = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  },
];
let options: huks.HuksOptions = {
  properties: properties
};
huks.generateKeyItem(keyAlias, options, (error, data) => {
  if (error) {
    console.error(`callback: generateKeyItem failed`);
  } else {
    console.info(`callback: generateKeyItem key success`);
  }
});
```

#### huks.generateKeyItem9+

generateKeyItem(keyAlias: string, options: HuksOptions) : Promise<void>

生成密钥。使用Promise异步回调。

基于密钥不出TEE原则，此接口不会返回密钥材料内容，只用于表示此次调用是否成功。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于存放生成key所需TAG。其中密钥使用的算法、密钥用途、密钥长度为必选参数。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000012Device environment or input parameter abnormal.12000013queried credential does not exist.12000014memory is insufficient.12000015Failed to obtain the security information via UserIAM.12000017The key with same alias is already exist.

**示例：**

```ets
/* 以生成ECC256密钥为例 */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  },
];
let options: huks.HuksOptions = {
  properties: properties
};
huks.generateKeyItem(keyAlias, options)
  .then((data) => {
    console.info(`promise: generateKeyItem success`);
  });
```

#### huks.deleteKeyItem9+

deleteKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>) : void

删除密钥。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应为生成key时传入的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是

用于删除密钥时指定密钥的属性，如使用[HuksAuthStorageLevel](#ZH-CN_TOPIC_0000002529445359__huksauthstoragelevel11)指定需删除密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

callbackAsyncCallback<void>是回调函数。当删除密钥成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000004operating file failed.12000005IPC communication failed.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.deleteKeyItem(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: deleteKeyItem failed`);
  } else {
    console.info(`callback: deleteKeyItem key success`);
  }
});
```

#### huks.deleteKeyItem9+

deleteKeyItem(keyAlias: string, options: HuksOptions) : Promise<void>

删除密钥。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应为生成key时传入的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是

用于删除时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#ZH-CN_TOPIC_0000002529445359__huksauthstoragelevel11)指定需删除密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000004operating file failed.12000005IPC communication failed.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.deleteKeyItem(keyAlias, emptyOptions)
  .then((data) => {
    console.info(`promise: deleteKeyItem key success`);
  });
```

#### huks.importKeyItem9+

importKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>) : void

导入明文密钥。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于导入时所需TAG和需要导入的密钥。其中密钥使用的算法、密钥用途、密钥长度为必选参数。callbackAsyncCallback<void>是回调函数。当导入密钥成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000012Device environment or input parameter abnormal.12000013queried credential does not exist.12000014memory is insufficient.12000015Failed to obtain the security information via UserIAM.12000017The key with same alias is already exist.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 以导入AES256密钥为例 */
let plainTextSize32 = makeRandomArr(32);

function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value:
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let options: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
huks.importKeyItem(keyAlias, options, (error, data) => {
  if (error) {
    console.error(`callback: importKeyItem failed`);
  } else {
    console.info(`callback: importKeyItem success`);
  }
});
```

#### huks.importKeyItem9+

importKeyItem(keyAlias: string, options: HuksOptions) : Promise<void>

导入明文密钥。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于导入时所需TAG和需要导入的密钥。其中密钥使用的算法、密钥用途、密钥长度为必选参数。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000012Device environment or input parameter abnormal.12000013queried credential does not exist.12000014memory is insufficient.12000015Failed to obtain the security information via UserIAM.12000017The key with same alias is already exist.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 以导入AES256为例 */
function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};

/* 第一步：生成密钥 */
let plainTextSize32 = makeRandomArr(32);
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
/* 第二步：导入密钥 */
huks.importKeyItem(keyAlias, huksOptions)
  .then((data) => {
    console.info(`promise: importKeyItem success`);
  });
```

#### huks.attestKeyItem9+

attestKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

获取密钥证书。使用callback异步回调。

**需要权限**：ohos.permission.ATTEST_KEY，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，存放待获取证书密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于获取证书时指定所需参数与数据。callbackAsyncCallback<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>是回调函数。当获取密钥证书成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息201check permission failed.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let securityLevel = stringToUint8Array('sec_level');
let challenge = stringToUint8Array('challenge_data');
let versionInfo = stringToUint8Array('version_info');
let keyAliasString = "key attest";

async function generateKeyThenAttestKey() {
  let aliasString = keyAliasString;
  let aliasUint8 = stringToUint8Array(aliasString);
  let generateProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_PSS
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
      value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_ECB
    }
  ];
  let generateOptions: huks.HuksOptions = {
    properties: generateProperties
  };
  let attestProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
      value: securityLevel
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
      value: versionInfo
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
      value: aliasUint8
    }
  ];
  let attestOptions: huks.HuksOptions = {
    properties: attestProperties
  };
  huks.generateKeyItem(aliasString, generateOptions, (error, data) => {
    if (error) {
      console.error(`callback: generateKeyItem failed`);
    } else {
      console.info(`callback: generateKeyItem success`);
      huks.attestKeyItem(aliasString, attestOptions, (error, data) => {
        if (error) {
          console.error(`callback: attestKeyItem failed`);
        } else {
          console.info(`callback: attestKeyItem success`);
        }
      });
    }
  });
}
```

#### huks.attestKeyItem9+

attestKeyItem(keyAlias: string, options: HuksOptions) : Promise<HuksReturnResult>

获取密钥证书。使用Promise异步回调。

**需要权限**：ohos.permission.ATTEST_KEY，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，存放待获取证书密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于获取证书时指定所需参数与数据。

**返回值：**

类型说明Promise<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>Promise对象。当调用成功时，HuksReturnResult的certChains成员非空，为获取到的证书链。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息201check permission failed.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let securityLevel = stringToUint8Array('sec_level');
let challenge = stringToUint8Array('challenge_data');
let versionInfo = stringToUint8Array('version_info');
let keyAliasString = "key attest";

async function generateKey(alias: string) {
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_PSS
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
      value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_ECB
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };
  await huks.generateKeyItem(alias, options)
    .then((data) => {
      console.info(`promise: generateKeyItem success`);
    });
}

async function attestKey() {
  let aliasString = keyAliasString;
  let aliasUint8 = stringToUint8Array(aliasString);
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
      value: securityLevel
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
      value: versionInfo
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
      value: aliasUint8
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };
  await generateKey(aliasString);
  await huks.attestKeyItem(aliasString, options)
    .then((data) => {
      console.info(`promise: attestKeyItem success`);
    });
}
```

#### huks.anonAttestKeyItem11+

anonAttestKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

获取匿名化密钥证书。使用callback异步回调。

该操作需要联网进行，且耗时较长。返回12000012错误码时，可能是由于网络异常导致。此时如果没有联网，需要提示用户网络没有连接，如果已经联网，可能是由于网络抖动导致失败，建议重试。

密钥证明证书格式说明请参考[设备证书服务-密钥证明证书格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-servers#section8815174119330)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，存放待获取证书密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于获取证书时指定所需参数与数据。callbackAsyncCallback<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>是回调函数。当获取匿名化密钥证书成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let securityLevel = stringToUint8Array('sec_level');
let challenge = stringToUint8Array('challenge_data');
let versionInfo = stringToUint8Array('version_info');
let keyAliasString = "key anon attest";

async function generateKeyThenAttestKey(): Promise<void> {
  let aliasString = keyAliasString;
  let aliasUint8 = stringToUint8Array(aliasString);
  let generateProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_PSS
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
      value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_ECB
    }
  ];
  let generateOptions: huks.HuksOptions = {
    properties: generateProperties
  };
  let anonAttestProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
      value: securityLevel
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
      value: versionInfo
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
      value: aliasUint8
    }
  ];
  let anonAttestOptions: huks.HuksOptions = {
    properties: anonAttestProperties
  };
  huks.generateKeyItem(aliasString, generateOptions, (error, data) => {
    if (error) {
      console.error(`callback: generateKeyItem failed`);
    } else {
      console.info(`callback: generateKeyItem success`);
      huks.anonAttestKeyItem(aliasString, anonAttestOptions, (error, data) => {
        if (error) {
          console.error(`callback: anonAttestKeyItem failed`);
        } else {
          console.info(`callback: anonAttestKeyItem success`);
        }
      });
    }
  });
}
```

#### huks.anonAttestKeyItem11+

anonAttestKeyItem(keyAlias: string, options: HuksOptions) : Promise<HuksReturnResult>

获取匿名化密钥证书。使用Promise异步回调。

该操作需要联网进行，且耗时较长。返回12000012错误码时，可能是由于网络异常导致。此时如果没有联网，需要提示用户网络没有连接，如果已经联网，可能是由于网络抖动导致失败，建议重试。

密钥证明证书格式说明请参考[设备证书服务-密钥证明证书格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-servers#section8815174119330)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，存放待获取证书密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于获取证书时指定所需参数与数据。

**返回值：**

类型说明Promise<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>Promise对象。当调用成功时，HuksReturnResult的certChains成员非空，为获取到的证书链。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let securityLevel = stringToUint8Array('sec_level');
let challenge = stringToUint8Array('challenge_data');
let versionInfo = stringToUint8Array('version_info');
let keyAliasString = "key anon attest";

async function generateKey(alias: string): Promise<void> {
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_PSS
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
      value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_ECB
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };

  await huks.generateKeyItem(alias, options);
}

async function anonAttestKey(): Promise<void> {
  let aliasString = keyAliasString;
  let aliasUint8 = stringToUint8Array(aliasString);
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
      value: securityLevel
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
      value: versionInfo
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
      value: aliasUint8
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };

  await generateKey(aliasString);
  await huks.anonAttestKeyItem(aliasString, options);
}
```

#### huks.importWrappedKeyItem9+

importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, options: HuksOptions, callback: AsyncCallback<void>) : void

导入加密密钥。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，存放待导入密钥的别名。wrappingKeyAliasstring是密钥别名，对应密钥用于解密加密的密钥数据。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于导入时所需TAG和需要导入的加密的密钥数据。其中密钥使用的算法、密钥用途、密钥长度为必选参数。callbackAsyncCallback<void>是回调函数。不返回err值时表示接口使用成功时，其他时为错误。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000013queried credential does not exist.12000014memory is insufficient.12000015Failed to obtain the security information via UserIAM.12000017The key with same alias is already exist.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

let alias1 = "importAlias";
let alias2 = "wrappingKeyAlias";

async function TestGenFunc(alias: string, options: huks.HuksOptions) {
  await genKey(alias, options)
    .then((data) => {
      console.info(`callback: generateKeyItem success`);
    });
}

function genKey(alias: string, options: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    huks.generateKeyItem(alias, options, (error, data) => {
      if (error) {
        reject(error);
      } else {
        resolve(data);
      }
    });
  });
}

async function TestExportFunc(alias: string, options: huks.HuksOptions) {
  await exportKey(alias, options)
    .then((data) => {
      console.info(`callback: exportKeyItem success, data = ${JSON.stringify(data)}`);
    });
}

function exportKey(alias: string, options: huks.HuksOptions) {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    huks.exportKeyItem(alias, options, (error, data) => {
      if (error) {
        reject(error);
      } else {
        resolve(data);
      }
    });
  });
}

async function TestImportWrappedFunc(alias: string, wrappingAlias: string, options: huks.HuksOptions) {
  await importWrappedKey(alias, wrappingAlias, options)
    .then((data) => {
      console.info(`callback: importWrappedKeyItem success`);
    });
}

function importWrappedKey(alias: string, wrappingAlias: string, options: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    huks.importWrappedKeyItem(alias, wrappingAlias, options, (error, data) => {
      if (error) {
        reject(error);
      } else {
        resolve(data);
      }
    });
  });
}

async function TestImportWrappedKeyFunc(
  alias: string,
  wrappingAlias: string,
  genOptions: huks.HuksOptions,
  importOptions: huks.HuksOptions
) {
  await TestGenFunc(wrappingAlias, genOptions);
  await TestExportFunc(wrappingAlias, genOptions);

  /* 以下操作不需要调用HUKS接口，此处不给出具体实现：
   * 假设待导入的密钥为keyA。
   * 1. 生成ECC公私钥keyB，公钥为keyB_pub, 私钥为keyB_pri。
   * 2. 使用keyB_pri和wrappingAlias密钥中获取的公钥进行密钥协商，协商出共享密钥share_key。
   * 3. 随机生成密钥kek，用于加密keyA，采用AES-GCM加密，加密过程中需要记录：nonce1、aad1、加密后的密文keyA_enc、加密后的tag1。
   * 4. 使用share_key加密kek，采用AES-GCM加密，加密过程中需要记录：nonce2、aad2、加密后的密文kek_enc、加密后的tag2。
   * 5. 拼接importOptions.inData字段，满足以下格式：
   *     keyB_pub的长度（4字节） + keyB_pub的数据 + aad2的长度（4字节） + aad2的数据 +
   *     nonce2的长度（4字节）   + nonce2的数据   + tag2的长度（4字节） + tag2的数据 +
   *     kek_enc的长度（4字节）  + kek_enc的数据  + aad1的长度（4字节） + aad1的数据 +
   *     nonce1的长度（4字节）   + nonce1的数据   + tag1的长度（4字节） + tag1的数据 +
   *     keyA长度占用的内存长度（4字节）  + keyA的长度     + keyA_enc的长度（4字节） + keyA_enc的数据
   */
  /* 该处为示例代码，实际运行过程中，应使用实际导入密钥数据。数据构造方式由上注释可见说明 */
  let inputKey = new Uint8Array([0x02, 0x00, 0x00, 0x00]);
  importOptions.inData = inputKey;
  await TestImportWrappedFunc(alias, wrappingAlias, importOptions);
}

function makeGenerateOptions() {
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_ECC
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_UNWRAP
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_IMPORT_KEY_TYPE,
      value: huks.HuksImportKeyType.HUKS_KEY_TYPE_KEY_PAIR,
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };
  return options;
};

function makeImportOptions() {
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_AES
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_CBC
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_UNWRAP_ALGORITHM_SUITE,
      value: huks.HuksUnwrapSuite.HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NOPADDING
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };
  return options;
};

function huksImportWrappedKey() {
  let genOptions = makeGenerateOptions();
  let importOptions = makeImportOptions();
  TestImportWrappedKeyFunc(
    alias1,
    alias2,
    genOptions,
    importOptions
  );
}
```

#### huks.importWrappedKeyItem9+

importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, options: HuksOptions) : Promise<void>

导入加密密钥。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，存放待导入密钥的别名。wrappingKeyAliasstring是密钥别名，对应密钥用于解密加密的密钥数据。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于导入时所需TAG和需要导入的加密的密钥数据。其中密钥使用的算法、密钥用途、密钥长度为必选参数。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000013queried credential does not exist.12000014memory is insufficient.12000015Failed to obtain the security information via UserIAM.12000017The key with same alias is already exist.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 处理流程与callback类似，主要差异点为如下函数： */
/* 该处为示例代码，实际运行过程中，应使用实际导入密钥数据。数据构造方式由上注释可见说明 */
async function TestImportWrappedFunc(alias: string, wrappingAlias: string, options: huks.HuksOptions) {
  await huks.importWrappedKeyItem(alias, wrappingAlias, options)
    .then((data) => {
      console.info(`promise: importWrappedKeyItem success`);
    });
}
```

#### huks.exportKeyItem9+

exportKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

导出密钥。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应与所用密钥生成时使用的别名相同。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是

用于导出密钥时指定密钥的属性，如使用[HuksAuthStorageLevel](#ZH-CN_TOPIC_0000002529445359__huksauthstoragelevel11)指定需导出密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

callbackAsyncCallback<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>是回调函数。当导出密钥成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。HuksReturnResult中的outData返回从HUKS中导出的公钥。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.exportKeyItem(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: exportKeyItem failed`);
  } else {
    console.info(`callback: exportKeyItem success, data = ${JSON.stringify(data)}`);
  }
});
```

#### huks.exportKeyItem9+

exportKeyItem(keyAlias: string, options: HuksOptions) : Promise<HuksReturnResult>

导出密钥。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应与所用密钥生成时使用的别名相同。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是空对象（此处传空即可）。

**返回值：**

类型说明Promise<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>Promise对象。当调用成功时，HuksReturnResult的outData成员非空，为从密钥中导出的公钥。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.exportKeyItem(keyAlias, emptyOptions)
  .then((data) => {
    console.info(`promise: exportKeyItem success, data = ${JSON.stringify(data)}`);
  });
```

#### huks.wrapKeyItem20+

wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>

加密导出密钥。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应与所用密钥生成时使用的别名相同。params[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于指定导出密钥时的加密类型。

**返回值：**

类型说明Promise<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>Promise对象。当调用成功时，HuksReturnResult的outData成员非空，为导出的密钥密文。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息801api is not supported.12000004operating file failed.12000005IPC communication failed.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000018the input parameter is invalid.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = "testWrapKey";
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_GCM
  },
  /* 生成密钥时指定允许加密导出 */
  {
    tag: huks.HuksTag.HUKS_TAG_IS_ALLOWED_WRAP,
    value: true
  }
];

let options: huks.HuksOptions = {
  properties: properties,
};

let wrapKeyProperties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
    value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
  }
];

let wrapKeyOptions: huks.HuksOptions = {
  properties: wrapKeyProperties,
};

let wrappedKey: Uint8Array;

async function testGenerateKey() {
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generateKeyItem success`);
    })
    .catch((error: Error) => {
      console.error(`promise: generateKeyItem failed`);
    });
}

async function testWrapKey(){
  await testGenerateKey();

  await huks.wrapKeyItem(keyAlias, wrapKeyOptions)
    .then((data) => {
      wrappedKey = data.outData as Uint8Array;
      console.info(`promise: wrapKeyItem success, data = ${JSON.stringify(data)}`);
    })
    .catch((error: Error) => {
      console.error(`promise: wrapKeyItem failed`);
    });
}
```

#### huks.unwrapKeyItem20+

unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>

加密导入密钥。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，指定导入密钥的密钥别名。params[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于指定导入密钥时的加密类型。wrappedKeyUint8Array是加密导出密钥的密文。

**返回值：**

类型说明Promise<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息801api is not supported.12000004operating file failed.12000005IPC communication failed.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000015Failed to obtain the security information via UserIAM.12000018the input parameter is invalid.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

let wrapKeyProperties: Array<huks.HuksParam> = [];
let wrapKeyOptions: huks.HuksOptions = {
  properties: wrapKeyProperties,
};

/* keyAlias要和wrapKeyItem一致, wrappedKey在wrapKeyItem后获取 */
let keyAlias = "testWrapKey";
let wrappedKey: Uint8Array;

async function testUnwrapKey(){
  await huks.unwrapKeyItem(keyAlias, wrapKeyOptions, wrappedKey)
    .then((data) => {
      console.info(`promise: unwrapKeyItem success`);
    })
    .catch((error: Error) => {
      console.error(`promise: unwrapKeyItem failed`);
    });
}
```

#### huks.getKeyItemProperties9+

getKeyItemProperties(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

获取密钥属性。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应与所用密钥生成时使用的别名相同。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是空对象（此处传空即可）。callbackAsyncCallback<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>是回调函数。当获取密钥属性成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。HuksReturnResult的properties为生成密钥时所需参数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.getKeyItemProperties(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: getKeyItemProperties failed`);
  } else {
    console.info(`callback: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
  }
});
```

#### huks.getKeyItemProperties9+

getKeyItemProperties(keyAlias: string, options: HuksOptions) : Promise<HuksReturnResult>

获取密钥属性。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应与所用密钥生成时使用的别名相同。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是空对象（此处传空即可）。

**返回值：**

类型说明Promise<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>Promise对象。返回HuksReturnResult。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.getKeyItemProperties(keyAlias, emptyOptions)
  .then((data) => {
    console.info(`promise: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
  });
```

#### huks.isKeyItemExist9+

isKeyItemExist(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>) : void

判断密钥是否存在。使用callback异步回调。

若密钥不存在，则抛出错误码为12000011的异常。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是所需查找的密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是

用于查询时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#ZH-CN_TOPIC_0000002529445359__huksauthstoragelevel11)指定需查询密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

callbackAsyncCallback<boolean>是回调函数。密钥存在时，data为true；密钥不存在时，data为undefined，err中的错误码为12000011，并附带对应错误描述。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.isKeyItemExist(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: isKeyItemExist failed`);
  } else {
    if (data) {
      console.info(`keyAlias:${keyAlias} is existed!`);
    } else {
      console.error(`find key failed`);
    }
  }
});
```

#### huks.isKeyItemExist9+

isKeyItemExist(keyAlias: string, options: HuksOptions) : Promise<boolean>

判断密钥是否存在。使用Promise异步回调。

若密钥不存在，则抛出错误码为12000011的异常。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是所需查找的密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是

用于查询时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#ZH-CN_TOPIC_0000002529445359__huksauthstoragelevel11)指定需查询密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

**返回值：**

类型说明Promise<boolean>Promise对象。密钥存在时，data为true；密钥不存在时，err中的错误码为12000011，并附带对应错误描述。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.isKeyItemExist(keyAlias, emptyOptions).then((data) => {
  console.info(`keyAlias:${keyAlias} is existed!`);
});
```

#### huks.hasKeyItem11+

hasKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>) : void

判断密钥是否存在。使用callback异步回调。

若密钥不存在，则通过callback返回false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是所需查找的密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是

用于查询时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#ZH-CN_TOPIC_0000002529445359__huksauthstoragelevel11)指定需查询密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

callbackAsyncCallback<boolean>是回调函数。若密钥存在，data为true，若密钥不存在，data为false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.hasKeyItem(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: hasKeyItem failed`);
  } else {
    if (data) {
      console.info(`keyAlias:${keyAlias} is existed!`);
    } else {
      console.error(`find key failed`);
    }
  }
});
```

#### huks.hasKeyItem11+

hasKeyItem(keyAlias: string, options: HuksOptions) : Promise<boolean>

判断密钥是否存在。使用Promise异步回调。

若密钥不存在，则通过Promise返回false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是所需查找的密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是

用于查询时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#ZH-CN_TOPIC_0000002529445359__huksauthstoragelevel11)指定需查询密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

**返回值：**

类型说明Promise<boolean>Promise对象。若密钥存在，返回值为true，若密钥不存在，返回值为false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.hasKeyItem(keyAlias, emptyOptions).then((data) => {
  if (data) {
    console.info(`keyAlias:${keyAlias} is existed!`);
  } else {
    console.info(`find key failed!`);
  }
});
```

#### huks.initSession9+

initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>) : void

initSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明keyAliasstring是initSession操作密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是initSession操作的参数集合。callbackAsyncCallback<[HuksSessionHandle](#ZH-CN_TOPIC_0000002529445359__hukssessionhandle9)>是回调函数。当密钥操作init成功时，err为undefined，data为获取到的HuksSessionHandle；否则为错误对象。HuksSessionHandle的handle返回initSession生成的handle。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine or Ukey driver.12000010the number of sessions has reached limit.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000018the input parameter is invalid.12000020the provider operation failed.12000021the Ukey PIN is locked.12000023the Ukey PIN not authenticated.12000024the provider or Ukey is busy.

#### huks.initSession9+

initSession(keyAlias: string, options: HuksOptions) : Promise<HuksSessionHandle>

initSession操作密钥接口。使用Promise异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是initSession操作密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是initSession参数集合。

**返回值**：

类型说明Promise<[HuksSessionHandle](#ZH-CN_TOPIC_0000002529445359__hukssessionhandle9)>Promise对象。返回HuksSessionHandle。HuksSessionHandle的handle返回initSession生成的handle。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine or Ukey driver.12000010the number of sessions has reached limit.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000018the input parameter is invalid.12000020the provider operation failed.12000021the Ukey PIN is locked.12000023the Ukey PIN not authenticated.12000024the provider or Ukey is busy.

#### huks.updateSession9+

updateSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

updateSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明handlenumber是updateSession操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是updateSession的参数集合。callbackAsyncCallback<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>是回调函数。当密钥操作update成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine or Ukey driver.12000007this credential is already invalidated permanently.12000008verify auth token failed.12000009auth token is already timeout.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000020the provider operation failed.12000021the Ukey PIN is locked.12000023the Ukey PIN not authenticated.12000024the provider or Ukey is busy.

#### huks.updateSession9+

updateSession(handle: number, options: HuksOptions, token: Uint8Array, callback: AsyncCallback<HuksReturnResult>) : void

支持用户身份认证访问控制的updateSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是updateSession操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是updateSession操作的参数集合。tokenUint8Array是密钥[二次认证密钥访问控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-identity-authentication-overview#二次认证密钥访问控制)的用户鉴权证明(AuthToken)。callbackAsyncCallback<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>是回调函数。当密钥操作update成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000007this credential is already invalidated permanently.12000008verify auth token failed.12000009auth token is already timeout.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

#### huks.updateSession9+

updateSession(handle: number, options: HuksOptions, token?: Uint8Array) : Promise<HuksReturnResult>

updateSession操作密钥接口。使用Promise异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是updateSession操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是updateSession操作的参数集合。tokenUint8Array否密钥[二次认证密钥访问控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-identity-authentication-overview#二次认证密钥访问控制)的用户鉴权证明(AuthToken)，不填表示不进行二次认证密钥访问控制。

**返回值**：

类型说明Promise<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>Promise对象。将updateSession操作的结果添加到回调函数中。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine or Ukey driver.12000007this credential is already invalidated permanently.12000008verify auth token failed.12000009auth token is already timeout.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000020the provider operation failed.12000021the Ukey PIN is locked.12000023the Ukey PIN not authenticated.12000024the provider or Ukey is busy.

#### huks.finishSession9+

finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

finishSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明handlenumber是finishSession操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是finishSession的参数集合。callbackAsyncCallback<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>是回调函数。当密钥操作finish成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000007this credential is already invalidated permanently.12000008verify auth token failed.12000009auth token is already timeout.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000017The key with same alias is already exist.12000020the provider operation failed.12000021the Ukey PIN is locked.12000023the Ukey PIN not authenticated.12000024the provider or Ukey is busy.

#### huks.finishSession9+

finishSession(handle: number, options: HuksOptions, token: Uint8Array, callback: AsyncCallback<HuksReturnResult>) : void

支持用户身份认证访问控制的finishSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是finishSession操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是finishSession的参数集合。tokenUint8Array是密钥[二次认证密钥访问控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-identity-authentication-overview#二次认证密钥访问控制)的用户鉴权证明(AuthToken)。callbackAsyncCallback<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>是回调函数。当密钥操作finish成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000007this credential is already invalidated permanently.12000008verify auth token failed.12000009auth token is already timeout.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000017The key with same alias is already exist.

#### huks.finishSession9+

finishSession(handle: number, options: HuksOptions, token?: Uint8Array) : Promise<HuksReturnResult>

finishSession操作密钥接口。使用Promise异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是finishSession操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是finishSession操作的参数集合。tokenUint8Array否密钥[二次认证密钥访问控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-identity-authentication-overview#二次认证密钥访问控制)的用户鉴权证明(AuthToken)，不填表示不进行二次认证密钥访问控制。

**返回值**：

类型说明Promise<[HuksReturnResult](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)>Promise对象。返回HuksReturnResult。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000001algorithm mode is not supported.12000002algorithm param is missing.12000003algorithm param is invalid.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine.12000007this credential is already invalidated permanently.12000008verify auth token failed.12000009auth token is already timeout.12000011queried entity does not exist.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000017The key with same alias is already exist.12000020the provider operation failed.12000021the Ukey PIN is locked.12000023the Ukey PIN not authenticated.12000024the provider or Ukey is busy.

#### huks.abortSession9+

abortSession(handle: number, options: HuksOptions, callback: AsyncCallback<void>) : void

abortSession终止密钥操作。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

参数名类型必填说明handlenumber是abortSession操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是abortSession操作的参数集合。callbackAsyncCallback<void>是回调函数。当密钥操作abort成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine or Ukey driver.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000020the provider operation failed.12000024the provider or Ukey is busy.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用，
 * 当这三个操作中的任一阶段发生错误时，都需要调用huks.abortSession来终止密钥的使用
 *
 * 以下以RSA2048密钥的callback功能使用为例
 */

let keyAlias = "HuksDemoRSA";
let properties: Array<huks.HuksParam> = []
let options: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(0)
};
let handle: number = 0;

async function huksAbort() {
  properties = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB,
  }];

  huks.generateKeyItem(keyAlias, options, (error, data) => {
    if (error) {
      console.error(`callback: generateKeyItem failed`);
    } else {
      console.info(`callback: generateKeyItem success`);
      huks.initSession(keyAlias, options, (error, data) => { // 以initSession阶段进行abortSession为例
        if (error) {
          console.error(`callback: initSession failed`);
        } else {
          console.info(`callback: initSession success, data = ${JSON.stringify(data)}`);
          handle = data.handle;
          huks.abortSession(handle, options, (error, data) => {
            if (error) {
              console.error(`callback: abortSession failed`);
            } else {
              console.info(`callback: abortSession success`);
            }
          });
        }
      });
    }
  });
}
```

#### huks.abortSession9+

abortSession(handle: number, options: HuksOptions) : Promise<void>

abortSession终止密钥操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是abortSession操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是abortSession操作的参数集合。

**返回值**：

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801api is not supported.12000004operating file failed.12000005IPC communication failed.12000006error occurred in crypto engine or Ukey driver.12000012Device environment or input parameter abnormal.12000014memory is insufficient.12000020the provider operation failed.12000024the provider or Ukey is busy.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用，
 * 当这三个操作中的任一阶段发生错误时，都需要调用huks.abortSession来终止密钥的使用
 *
 * 以下以RSA2048密钥的promise功能使用为例
 */

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let keyAlias = "HuksDemoRSA";
let properties: Array<huks.HuksParam> = [];
let options: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(0)
};
let handle: number = 0;

async function generateKey() {
  properties = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB,
  }];

  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generateKeyItem success`);
    });
}

async function huksInit() {
  console.info('enter huksInit');
  await huks.initSession(keyAlias, options)
    .then((data) => {
      console.info(`promise: initSession success, data = ${JSON.stringify(data)}`);
      handle = data.handle;
    });
}

async function huksUpdate() {
  console.info('enter huksUpdate');
  options.inData = stringToUint8Array("huksHmacTest");
  await huks.updateSession(handle, options)
    .then((data) => {
      console.info(`promise: updateSession success, data = ${JSON.stringify(data)}`);
    });
}

async function huksFinish() {
  console.info('enter huksFinish');
  options.inData = new Uint8Array(0);
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: finishSession success, data = ${JSON.stringify(data)}`);
    });
}

async function huksAbort() {
  console.info('enter huksAbort');
  await huks.abortSession(handle, options)
    .then((data) => {
      console.info(`promise: abortSession success`);
    });
}

async function testAbort() {
  await generateKey();
  await huksInit(); // 以initSession阶段进行abortSession为例
  await huksAbort();
}
```

#### huks.listAliases12+

listAliases(options: HuksOptions): Promise<HuksListAliasesReturnResult>

查询密钥别名集接口。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是listAliases操作的参数集合。

**返回值**：

类型说明Promise<[HuksListAliasesReturnResult](#ZH-CN_TOPIC_0000002529445359__hukslistaliasesreturnresult12)>Promise对象。将listAliases操作的结果添加到回调函数中。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.12000004operating file failed.12000005IPC communication failed.12000012Device environment or input parameter abnormal.12000014memory is insufficient.

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit'

async function testListAliases() {
  let queryProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
      value: huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_DE
    }
  ];
  let queryOptions: huks.HuksOptions = {
    properties: queryProperties
  };

  let result: huks.HuksListAliasesReturnResult = await huks.listAliases(queryOptions);
  console.info(`promise: listAliases success`);
}
```

#### HuksExceptionErrCode9+

表示错误码的枚举以及对应的错误信息，错误码表示错误类型，错误信息展示错误详情。

关于错误码的具体信息，可在[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)中查看。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_ERR_CODE_PERMISSION_FAIL201

权限错误导致失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_NOT_SYSTEM_APP12+202

非系统应用不可以调用系统API。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_ILLEGAL_ARGUMENT401

参数错误导致失败。可能原因：1. 必选参数未指定。2. 参数类型不正确。3. 参数校验失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_NOT_SUPPORTED_API801

不支持的API。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED12000001

不支持的功能/特性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT12000002

缺少密钥算法参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT12000003

无效密钥算法参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_FILE_OPERATION_FAIL12000004

文件操作失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_COMMUNICATION_FAIL12000005

通信失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_CRYPTO_FAIL12000006

算法库操作失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_KEY_AUTH_PERMANENTLY_INVALIDATED12000007

密钥访问失败-密钥访问失效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_KEY_AUTH_VERIFY_FAILED12000008

密钥访问失败-密钥认证失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_KEY_AUTH_TIME_OUT12000009

密钥访问失败-密钥访问超时。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_SESSION_LIMIT12000010

密钥操作会话数已达上限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_ITEM_NOT_EXIST12000011

目标对象不存在。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_EXTERNAL_ERROR12000012

外部错误。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_CREDENTIAL_NOT_EXIST12000013

缺失所需凭据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_INSUFFICIENT_MEMORY12000014

内存不足。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_CALL_SERVICE_FAILED12000015

调用其他系统服务失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_DEVICE_PASSWORD_UNSET11+12000016

需要锁屏密码但未设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_ERR_CODE_KEY_ALREADY_EXIST20+12000017

同名密钥已存在。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_INVALID_ARGUMENT20+12000018

输入参数非法。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_ITEM_EXISTS22+12000019

同名provider已注册。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_EXTERNAL_MODULE22+12000020

依赖的外部模块返回错误。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_PIN_LOCKED22+12000021

Ukey PIN码被锁。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

HUKS_ERR_CODE_PIN_INCORRECT22+12000022

Ukey PIN码错误。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

HUKS_ERR_CODE_PIN_NO_AUTH22+12000023

Ukey PIN码未认证。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

HUKS_ERR_CODE_BUSY22+12000024

设备或资源繁忙。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ERR_CODE_EXCEED_LIMIT22+12000025

资源超过限制。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

#### HuksKeyPurpose

表示密钥用途。

一个密钥仅能用于单类用途，不能既用于加解密又用于签名验签。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_KEY_PURPOSE_ENCRYPT1

表示密钥用于对明文进行加密操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_KEY_PURPOSE_DECRYPT2

表示密钥用于对密文进行解密操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_KEY_PURPOSE_SIGN4

表示密钥用于对数据进行签名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_KEY_PURPOSE_VERIFY8

表示密钥用于验证签名后的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_KEY_PURPOSE_DERIVE16

表示密钥用于派生密钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_KEY_PURPOSE_WRAP32

表示密钥用于加密导出。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_KEY_PURPOSE_UNWRAP64

表示密钥加密导入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_KEY_PURPOSE_MAC128

表示密钥用于生成mac消息验证码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_KEY_PURPOSE_AGREE256

表示密钥用于进行密钥协商。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

#### HuksKeyDigest

表示摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 8-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

名称值说明HUKS_DIGEST_NONE0

表示无摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_DIGEST_MD51

表示MD5摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_DIGEST_SM39+2

表示SM3摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

HUKS_DIGEST_SHA110

表示SHA1摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_DIGEST_SHA22411

表示SHA224摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_DIGEST_SHA25612

表示SHA256摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_DIGEST_SHA38413

表示SHA384摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_DIGEST_SHA51214

表示SHA512摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

#### HuksKeyPadding

表示补齐算法。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_PADDING_NONE0

表示不使用补齐算法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_PADDING_OAEP1

表示使用OAEP补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_PADDING_PSS2

表示使用PSS补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_PADDING_PKCS1_V1_53

表示使用PKCS1_V1_5补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_PADDING_PKCS54

表示使用PKCS5补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_PADDING_PKCS75

表示使用PKCS7补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_PADDING_ISO_IEC_9796_212+6

表示使用ISO_IEC_9796_2填充算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_PADDING_ISO_IEC_9797_112+7

表示使用ISO_IEC_9797_1填充算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

#### HuksCipherMode

表示加密模式。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_MODE_ECB1

表示使用ECB加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_MODE_CBC2

表示使用CBC加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_MODE_CTR3

表示使用CTR加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_MODE_OFB4

表示使用OFB加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_MODE_CFB12+5

表示使用CFB加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_MODE_CCM31

表示使用CCM加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_MODE_GCM32

表示使用GCM加密模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

#### HuksKeySize

表示密钥长度。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_RSA_KEY_SIZE_512512

表示使用RSA算法的密钥长度为512bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_RSA_KEY_SIZE_768768

表示使用RSA算法的密钥长度为768bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_RSA_KEY_SIZE_10241024

表示使用RSA算法的密钥长度为1024bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_RSA_KEY_SIZE_20482048

表示使用RSA算法的密钥长度为2048bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_RSA_KEY_SIZE_30723072

表示使用RSA算法的密钥长度为3072bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_RSA_KEY_SIZE_40964096

表示使用RSA算法的密钥长度为4096bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ECC_KEY_SIZE_224224

表示使用ECC算法的密钥长度为224bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ECC_KEY_SIZE_256256

表示使用ECC算法的密钥长度为256bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ECC_KEY_SIZE_384384

表示使用ECC算法的密钥长度为384bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ECC_KEY_SIZE_521521

表示使用ECC算法的密钥长度为521bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_AES_KEY_SIZE_128128

表示使用AES算法的密钥长度为128bit。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_AES_KEY_SIZE_192192

表示使用AES算法的密钥长度为192bit。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_AES_KEY_SIZE_256256

表示使用AES算法的密钥长度为256bit。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_AES_KEY_SIZE_512(deprecated)512

表示使用AES算法的密钥长度为512bit。

**说明：** 从API version 8开始支持，从API version 11开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_CURVE25519_KEY_SIZE_256256

表示使用CURVE25519算法的密钥长度为256bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_DH_KEY_SIZE_20482048

表示使用DH算法的密钥长度为2048bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_DH_KEY_SIZE_30723072

表示使用DH算法的密钥长度为3072bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_DH_KEY_SIZE_40964096

表示使用DH算法的密钥长度为4096bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_SM2_KEY_SIZE_2569+256

表示SM2算法的密钥长度为256bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

HUKS_SM4_KEY_SIZE_1289+128

表示SM4算法的密钥长度为128bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

HUKS_DES_KEY_SIZE_6412+64

表示DES算法的密钥长度为64bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_3DES_KEY_SIZE_12812+128

表示3DES算法的密钥长度为128bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_3DES_KEY_SIZE_19212+192

表示3DES算法的密钥长度为192bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

#### HuksKeyAlg

表示密钥使用的算法。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_ALG_RSA1

表示使用RSA算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_ECC2

表示使用ECC算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_DSA3

表示使用DSA算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_AES20

表示使用AES算法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ALG_HMAC50

表示使用HMAC算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_HKDF51

表示使用HKDF算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_PBKDF252

表示使用PBKDF2算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_ECDH100

表示使用ECDH算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_X25519101

表示使用X25519算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_ED25519102

表示使用ED25519算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_DH103

表示使用DH算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_ALG_SM29+150

表示使用SM2算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

HUKS_ALG_SM39+151

表示使用SM3算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

HUKS_ALG_SM49+152

表示使用SM4算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

HUKS_ALG_DES12+160

表示使用DES算法（API 12开始支持轻量级智能穿戴，API 18开始支持手机、平板、PC/2in1设备、TV、智能穿戴）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ALG_3DES12+161

表示使用3DES算法（API 12开始支持轻量级智能穿戴，API 18开始支持手机、平板、PC/2in1设备、TV、智能穿戴）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_ALG_CMAC12+162

表示使用CMAC算法（API 12开始支持轻量级智能穿戴，API 18开始支持手机、平板、PC/2in1设备、TV、智能穿戴）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

#### HuksKeyGenerateType

表示生成密钥的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 8-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

名称值说明HUKS_KEY_GENERATE_TYPE_DEFAULT0默认生成的密钥。HUKS_KEY_GENERATE_TYPE_DERIVE1派生生成的密钥。HUKS_KEY_GENERATE_TYPE_AGREE2协商生成的密钥。

#### HuksKeyFlag

表示密钥的产生方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_KEY_FLAG_IMPORT_KEY1表示通过导入公钥接口导入的密钥。HUKS_KEY_FLAG_GENERATE_KEY2表示通过生成密钥接口生成的密钥。HUKS_KEY_FLAG_AGREE_KEY3表示通过生成密钥协商接口生成的密钥。HUKS_KEY_FLAG_DERIVE_KEY4表示通过生成密钥派生接口生成的密钥。

#### HuksKeyStorageType

表示密钥存储方式。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_STORAGE_TEMP(deprecated)0

表示通过本地直接管理密钥。

**说明：** 从API version 8开始支持，从API version 10开始废弃，由于开发者正常使用密钥管理过程中并不需要使用此TAG，故无替代接口。针对密钥派生场景，可使用HUKS_STORAGE_ONLY_USED_IN_HUKS 与 HUKS_STORAGE_KEY_EXPORT_ALLOWED。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_STORAGE_PERSISTENT(deprecated)1

表示通过HUKS service管理密钥。

**说明：** 从API version 8开始支持，从API version 10开始废弃，由于开发者正常使用密钥管理过程中并不需要使用此TAG，故无替代接口。针对密钥派生场景，可使用HUKS_STORAGE_ONLY_USED_IN_HUKS 与 HUKS_STORAGE_KEY_EXPORT_ALLOWED。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_STORAGE_ONLY_USED_IN_HUKS10+2

表示主密钥派生的密钥存储于huks中，由HUKS进行托管。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension10-11

HUKS_STORAGE_KEY_EXPORT_ALLOWED10+3

表示主密钥派生的密钥直接导出给业务方，HUKS不对其进行托管服务。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension10-11

#### HuksSendType

表示发送TAG的方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 8-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

名称值说明HUKS_SEND_TYPE_ASYNC0表示异步发送TAG。HUKS_SEND_TYPE_SYNC1表示同步发送TAG。

#### HuksKeyClassType22+

表示密钥的来源。

**系统能力：** SystemCapability.Security.Huks.Extension

名称值说明HUKS_KEY_CLASS_DEFAULT0表示HUKS本地管理的密钥。HUKS_KEY_CLASS_EXTENSION1表示外部密钥管理扩展管理的密钥。

#### HuksUnwrapSuite9+

表示导入加密密钥的算法套件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

名称值说明HUKS_UNWRAP_SUITE_X25519_AES_256_GCM_NOPADDING1导入加密密钥时，X25519密钥协商后使用AES-256 GCM加密。HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NOPADDING2导入加密密钥时，ECDH密钥协商后使用AES-256 GCM加密。

#### HuksImportKeyType9+

表示导入密钥的密钥类型，默认为导入公钥，导入对称密钥时不需要该字段。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

名称值说明HUKS_KEY_TYPE_PUBLIC_KEY0表示导入的密钥类型为公钥。HUKS_KEY_TYPE_PRIVATE_KEY1表示导入的密钥类型为私钥。HUKS_KEY_TYPE_KEY_PAIR2表示导入的密钥类型为公私钥对。

#### HuksRsaPssSaltLenType10+

表示Rsa在签名验签、padding为pss时需指定的salt_len类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 10-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

名称值说明HUKS_RSA_PSS_SALT_LEN_DIGEST0表示以摘要长度设置salt_len。HUKS_RSA_PSS_SALT_LEN_MAX1表示以最大长度设置salt_len。

#### HuksUserAuthType9+

表示用户认证类型。

**系统能力：** SystemCapability.Security.Huks.Extension

名称值说明HUKS_USER_AUTH_TYPE_FINGERPRINT1 << 0

表示用户认证类型为指纹。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

HUKS_USER_AUTH_TYPE_FACE1 << 1

表示用户认证类型为人脸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

HUKS_USER_AUTH_TYPE_PIN1 << 2

表示用户认证类型为PIN码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

HUKS_USER_AUTH_TYPE_TUI_PIN20+1 << 5表示用户认证类型为TUI PIN码。

#### HuksUserAuthMode12+

表示用户认证模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

名称值说明HUKS_USER_AUTH_MODE_LOCAL0本地认证模式。HUKS_USER_AUTH_MODE_COAUTH1跨端协同认证模式。

#### HuksAuthAccessType9+

表示安全访问控制类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

名称值说明HUKS_AUTH_ACCESS_INVALID_CLEAR_PASSWORD1 << 0表示安全访问控制类型为清除密码后密钥无效。HUKS_AUTH_ACCESS_INVALID_NEW_BIO_ENROLL1 << 1表示安全访问控制类型为新录入生物特征后密钥无效。HUKS_AUTH_ACCESS_ALWAYS_VALID11+1 << 2表示安全访问控制类型为该密钥总是有效。

#### HuksChallengeType9+

表示密钥使用时生成challenge的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

名称值说明HUKS_CHALLENGE_TYPE_NORMAL0表示challenge为普通类型，默认32字节。HUKS_CHALLENGE_TYPE_CUSTOM1表示challenge为用户自定义类型。支持使用多个密钥仅一次认证。HUKS_CHALLENGE_TYPE_NONE2表示免challenge类型。

#### HuksChallengePosition9+

表示challenge类型为用户自定义类型时，生成的challenge有效长度仅为8字节连续的数据，且仅支持4种位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

名称值说明HUKS_CHALLENGE_POS_00表示0~7字节为当前密钥的有效challenge。HUKS_CHALLENGE_POS_11表示8~15字节为当前密钥的有效challenge。HUKS_CHALLENGE_POS_22表示16~23字节为当前密钥的有效challenge。HUKS_CHALLENGE_POS_33表示24~31字节为当前密钥的有效challenge。

#### HuksSecureSignType9+

表示生成或导入密钥时，指定该密钥的签名类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

名称值说明HUKS_SECURE_SIGN_WITH_AUTHINFO1

表示签名类型为携带认证信息。生成或导入密钥时指定该字段，则在使用密钥进行签名时，对待签名的数据添加认证信息后进行签名。

**注意：**

携带的认证信息包含身份信息，开发者需在其隐私声明中对此身份信息的使用目的、存留策略和销毁方式进行说明。

#### HuksAuthStorageLevel11+

表示生成或导入密钥时，指定该密钥的存储安全等级。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

名称值说明HUKS_AUTH_STORAGE_LEVEL_DE0表示密钥仅在开机后可访问。HUKS_AUTH_STORAGE_LEVEL_CE1表示密钥仅在首次解锁后可访问。HUKS_AUTH_STORAGE_LEVEL_ECE2表示密钥仅在解锁状态时可访问。

#### HuksKeyWrapType20+

表示密钥加密类型（加密导出或导入密钥）的枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_KEY_WRAP_TYPE_HUK_BASED2硬件唯一密钥加密类型。

#### HuksTagType

表示Tag的数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_TAG_TYPE_INVALID0 << 28表示非法的Tag类型。HUKS_TAG_TYPE_INT1 << 28表示该Tag的数据类型为int类型的number。HUKS_TAG_TYPE_UINT2 << 28表示该Tag的数据类型为uint类型的number。HUKS_TAG_TYPE_ULONG3 << 28表示该Tag的数据类型为bigint。HUKS_TAG_TYPE_BOOL4 << 28表示该Tag的数据类型为boolean。HUKS_TAG_TYPE_BYTES5 << 28表示该Tag的数据类型为Uint8Array。

#### HuksTag

表示调用参数的Tag。

**系统能力：** SystemCapability.Security.Huks.Core

名称值说明HUKS_TAG_INVALID(deprecated)HuksTagType.HUKS_TAG_TYPE_INVALID | 0

表示非法的Tag。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_ALGORITHMHuksTagType.HUKS_TAG_TYPE_UINT | 1

表示算法的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_PURPOSEHuksTagType.HUKS_TAG_TYPE_UINT | 2

表示密钥用途的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_KEY_SIZEHuksTagType.HUKS_TAG_TYPE_UINT | 3

表示密钥长度的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_DIGESTHuksTagType.HUKS_TAG_TYPE_UINT | 4

表示摘要算法的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_PADDINGHuksTagType.HUKS_TAG_TYPE_UINT | 5

表示填充模式的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_BLOCK_MODEHuksTagType.HUKS_TAG_TYPE_UINT | 6

表示加密模式的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_KEY_TYPEHuksTagType.HUKS_TAG_TYPE_UINT | 7

表示密钥类型的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_ASSOCIATED_DATAHuksTagType.HUKS_TAG_TYPE_BYTES | 8

表示附加身份验证数据的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_NONCEHuksTagType.HUKS_TAG_TYPE_BYTES | 9

表示密钥加解密的NONCE字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_IVHuksTagType.HUKS_TAG_TYPE_BYTES | 10

表示密钥初始化的向量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_INFOHuksTagType.HUKS_TAG_TYPE_BYTES | 11

表示密钥派生时的info。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_SALTHuksTagType.HUKS_TAG_TYPE_BYTES | 12

表示密钥派生时的盐值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_PWD(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 13

表示密钥派生时的password。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_ITERATIONHuksTagType.HUKS_TAG_TYPE_UINT | 14

表示密钥派生时的迭代次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_KEY_GENERATE_TYPEHuksTagType.HUKS_TAG_TYPE_UINT | 15

表示生成密钥类型的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_DERIVE_MAIN_KEY(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 16

表示密钥派生时的主密钥。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_DERIVE_FACTOR(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 17

表示密钥派生时的派生因子。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_DERIVE_ALG(deprecated)HuksTagType.HUKS_TAG_TYPE_UINT | 18

表示密钥派生时的算法类型。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_AGREE_ALGHuksTagType.HUKS_TAG_TYPE_UINT | 19

表示密钥协商时的算法类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_AGREE_PUBLIC_KEY_IS_KEY_ALIASHuksTagType.HUKS_TAG_TYPE_BOOL | 20

表示密钥协商时的公钥别名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_AGREE_PRIVATE_KEY_ALIASHuksTagType.HUKS_TAG_TYPE_BYTES | 21

表示密钥协商时的私钥别名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_AGREE_PUBLIC_KEYHuksTagType.HUKS_TAG_TYPE_BYTES | 22

表示密钥协商时的公钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_KEY_ALIASHuksTagType.HUKS_TAG_TYPE_BYTES | 23

表示密钥别名。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_DERIVE_KEY_SIZEHuksTagType.HUKS_TAG_TYPE_UINT | 24

表示派生密钥的大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_IMPORT_KEY_TYPE9+HuksTagType.HUKS_TAG_TYPE_UINT | 25

表示导入的密钥类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

HUKS_TAG_UNWRAP_ALGORITHM_SUITE9+HuksTagType.HUKS_TAG_TYPE_UINT | 26

表示导入加密密钥的套件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG10+HuksTagType.HUKS_TAG_TYPE_UINT |29

表示派生密钥/协商密钥的存储类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension10-11

HUKS_TAG_RSA_PSS_SALT_LEN_TYPE10+HuksTagType.HUKS_TAG_TYPE_UINT |30

表示rsa_pss_salt_length的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension10-11

HUKS_TAG_ACTIVE_DATETIME(deprecated)HuksTagType.HUKS_TAG_TYPE_ULONG | 201

原为证书业务预留字段，当前证书管理已独立，此字段废弃

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ORIGINATION_EXPIRE_DATETIME(deprecated)HuksTagType.HUKS_TAG_TYPE_ULONG | 202

原为证书业务预留字段，当前证书管理已独立，此字段废弃

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_USAGE_EXPIRE_DATETIME(deprecated)HuksTagType.HUKS_TAG_TYPE_ULONG | 203

原为证书业务预留字段，当前证书管理已独立，此字段废弃

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_CREATION_DATETIME(deprecated)HuksTagType.HUKS_TAG_TYPE_ULONG | 204

原为证书业务预留字段，当前证书管理已独立，此字段废弃

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_ALL_USERSHuksTagType.HUKS_TAG_TYPE_BOOL | 301

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_USER_IDHuksTagType.HUKS_TAG_TYPE_UINT | 302

表示当前密钥属于哪个userID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_NO_AUTH_REQUIREDHuksTagType.HUKS_TAG_TYPE_BOOL | 303

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_USER_AUTH_TYPEHuksTagType.HUKS_TAG_TYPE_UINT | 304

表示用户认证类型。从[HuksUserAuthType](#ZH-CN_TOPIC_0000002529445359__huksuserauthtype9)中选择，需要与安全访问控制类型同时设置。支持同时指定两种用户认证类型，如：安全访问控制类型指定为HUKS_AUTH_ACCESS_INVALID_NEW_BIO_ENROLL时，密钥访问认证类型可以指定以下三种： HUKS_USER_AUTH_TYPE_FACE 、HUKS_USER_AUTH_TYPE_FINGERPRINT、HUKS_USER_AUTH_TYPE_FACE | HUKS_USER_AUTH_TYPE_FINGERPRINT

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_AUTH_TIMEOUTHuksTagType.HUKS_TAG_TYPE_UINT | 305

表示auth token单次有效期。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_AUTH_TOKENHuksTagType.HUKS_TAG_TYPE_BYTES | 306

用于传入authToken的字段。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_KEY_AUTH_ACCESS_TYPE9+HuksTagType.HUKS_TAG_TYPE_UINT | 307

表示安全访问控制类型。从[HuksAuthAccessType](#ZH-CN_TOPIC_0000002529445359__huksauthaccesstype9)中选择，需要和用户认证类型同时设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_KEY_SECURE_SIGN_TYPE9+HuksTagType.HUKS_TAG_TYPE_UINT | 308

表示生成或导入密钥时，指定该密钥的签名类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_CHALLENGE_TYPE9+HuksTagType.HUKS_TAG_TYPE_UINT | 309

表示密钥使用时生成的challenge类型。从[HuksChallengeType](#ZH-CN_TOPIC_0000002529445359__hukschallengetype9)中选择。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_CHALLENGE_POS9+HuksTagType.HUKS_TAG_TYPE_UINT | 310

表示challenge类型为用户自定义类型时，huks产生的challenge有效长度仅为8字节连续的数据。从[HuksChallengePosition](#ZH-CN_TOPIC_0000002529445359__hukschallengeposition9)中选择。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_KEY_AUTH_PURPOSE10+HuksTagType.HUKS_TAG_TYPE_UINT |311

表示密钥认证用途的tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_AUTH_STORAGE_LEVEL11+HuksTagType.HUKS_TAG_TYPE_UINT |316

表示密钥存储安全等级的tag。从[HuksAuthStorageLevel](#ZH-CN_TOPIC_0000002529445359__huksauthstoragelevel11)中选择。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_USER_AUTH_MODE12+HuksTagType.HUKS_TAG_TYPE_UINT | 319

表示用户认证模式。从[HuksUserAuthMode](#ZH-CN_TOPIC_0000002529445359__huksuserauthmode12)中选择。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_CHALLENGEHuksTagType.HUKS_TAG_TYPE_BYTES | 501

表示attestation时的挑战值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_APPLICATION_IDHuksTagType.HUKS_TAG_TYPE_BYTES | 502

表示attestation时拥有该密钥的application的Id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_BRAND(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 503

表示设备的品牌。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_DEVICE(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 504

表示设备的设备ID。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_PRODUCT(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 505

表示设备的产品名。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_SERIAL(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 506

表示设备的SN号。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_IMEI(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 507

表示设备的IMEI号。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_MEID(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 508

表示设备的MEID号。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_MANUFACTURER(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 509

表示设备的制造商。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_MODEL(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 510

表示设备的型号。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_ALIASHuksTagType.HUKS_TAG_TYPE_BYTES | 511

表示attestation时的密钥别名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_SOCID(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 512

表示设备的SOCID。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_UDID(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 513

表示设备的UDID。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFOHuksTagType.HUKS_TAG_TYPE_BYTES | 514

表示attestation时的安全凭据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ATTESTATION_ID_VERSION_INFOHuksTagType.HUKS_TAG_TYPE_BYTES | 515

表示attestation时的版本号。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_KEY_OVERRIDE20+HuksTagType.HUKS_TAG_TYPE_BOOL | 520

表示是否覆写同名密钥。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_AE_TAG_LEN22+HuksTagType.HUKS_TAG_TYPE_UINT | 521

表示指定的AEAD标签长度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_KEY_CLASS22+HuksTagType.HUKS_TAG_TYPE_UINT | 522

表示密钥来源。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_IS_KEY_ALIASHuksTagType.HUKS_TAG_TYPE_BOOL | 1001

表示是否使用生成key时传入的别名的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_KEY_STORAGE_FLAGHuksTagType.HUKS_TAG_TYPE_UINT | 1002

表示密钥存储方式的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_IS_ALLOWED_WRAPHuksTagType.HUKS_TAG_TYPE_BOOL | 1003

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_KEY_WRAP_TYPEHuksTagType.HUKS_TAG_TYPE_UINT | 1004

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_KEY_AUTH_IDHuksTagType.HUKS_TAG_TYPE_BYTES | 1005

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_KEY_ROLEHuksTagType.HUKS_TAG_TYPE_UINT | 1006

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_KEY_FLAGHuksTagType.HUKS_TAG_TYPE_UINT | 1007

表示密钥标志的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_IS_ASYNCHRONIZEDHuksTagType.HUKS_TAG_TYPE_UINT | 1008

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_SECURE_KEY_ALIAS(deprecated)HuksTagType.HUKS_TAG_TYPE_BOOL | 1009

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_SECURE_KEY_UUID(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 1010

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_KEY_DOMAINHuksTagType.HUKS_TAG_TYPE_UINT | 1011

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_IS_DEVICE_PASSWORD_SET11+HuksTagType.HUKS_TAG_TYPE_BOOL | 1012

表示密钥锁屏密码访问控制字段，可限制密钥只有在用户设置了锁屏密码时可用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_PROCESS_NAME(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 10001

表示进程名称的Tag。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_PACKAGE_NAME(deprecated)HuksTagType.HUKS_TAG_TYPE_BYTES | 10002

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_ACCESS_TIME(deprecated)HuksTagType.HUKS_TAG_TYPE_UINT | 10003

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_USES_TIME(deprecated)HuksTagType.HUKS_TAG_TYPE_UINT | 10004

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_CRYPTO_CTX(deprecated)HuksTagType.HUKS_TAG_TYPE_ULONG | 10005

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_KEYHuksTagType.HUKS_TAG_TYPE_BYTES | 10006

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_KEY_VERSION(deprecated)HuksTagType.HUKS_TAG_TYPE_UINT | 10007

表示密钥版本的Tag。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_PAYLOAD_LEN(deprecated)HuksTagType.HUKS_TAG_TYPE_UINT | 10008

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

HUKS_TAG_AE_TAGHuksTagType.HUKS_TAG_TYPE_BYTES | 10009

用于传入GCM模式中的AEAD数据的字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_IS_KEY_HANDLE(deprecated)HuksTagType.HUKS_TAG_TYPE_ULONG | 10010

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_OS_VERSION(deprecated)HuksTagType.HUKS_TAG_TYPE_UINT | 10101

表示操作系统版本的Tag。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_OS_PATCHLEVEL(deprecated)HuksTagType.HUKS_TAG_TYPE_UINT | 10102

表示操作系统补丁级别的Tag。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_SYMMETRIC_KEY_DATAHuksTagType.HUKS_TAG_TYPE_BYTES | 20001

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

HUKS_TAG_ASYMMETRIC_PUBLIC_KEY_DATAHuksTagType.HUKS_TAG_TYPE_BYTES | 20002

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

HUKS_TAG_ASYMMETRIC_PRIVATE_KEY_DATAHuksTagType.HUKS_TAG_TYPE_BYTES | 20003

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

#### huks.getSdkVersion(deprecated)

getSdkVersion(options: HuksOptions) : string

获取当前系统sdk版本。

从API version 8开始支持，从API version 11开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是空对象（此处传空即可）。

**返回值：**

类型说明string返回sdk版本。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions传空 */
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.getSdkVersion(emptyOptions);
```

#### huks.generateKey(deprecated)

generateKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

生成密钥。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.generateKeyItem9+](#ZH-CN_TOPIC_0000002529445359__huksgeneratekeyitem9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于存放生成key所需TAG。callbackAsyncCallback<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>是回调函数。当生成密钥成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 以生成RSA512密钥为例 */

let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_512
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }
];
let options: huks.HuksOptions = {
  properties: properties
};
huks.generateKey(keyAlias, options, (err, data) => {
});
```

#### huks.generateKey(deprecated)

generateKey(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

生成密钥。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.generateKeyItem9+](#ZH-CN_TOPIC_0000002529445359__huksgeneratekeyitem9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于存放生成key所需TAG。

**返回值**：

类型说明Promise<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>Promise对象。返回HuksResult。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 以生成ECC256密钥为例 */

let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }
];
let options: huks.HuksOptions = {
  properties: properties
};
let result = huks.generateKey(keyAlias, options);
```

#### huks.deleteKey(deprecated)

deleteKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

删除密钥。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.deleteKeyItem9+](#ZH-CN_TOPIC_0000002529445359__huksdeletekeyitem9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应为生成key时传入的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于删除时指定密钥的属性TAG。callbackAsyncCallback<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>是回调函数。当删除密钥成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.deleteKey(keyAlias, emptyOptions, (err, data) => {
});
```

#### huks.deleteKey(deprecated)

deleteKey(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

删除密钥。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.deleteKeyItem9+](#ZH-CN_TOPIC_0000002529445359__huksdeletekeyitem9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应为生成key时传入的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于删除时指定密钥的属性TAG。

**返回值：**

类型说明Promise<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>Promise对象。返回HuksResult。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit"

/* 此处options选择emptyOptions传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.deleteKey(keyAlias, emptyOptions).then((data) => {
  console.info('delete key success');
}).catch((err: BusinessError) => {
  console.error("密钥删除失败，错误码是： " + err.code + " 错误码信息： " + err.message);
});
```

#### huks.importKey(deprecated)

importKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

导入明文密钥，使用Callback方式回调异步返回结果。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.importKeyItem9+](#ZH-CN_TOPIC_0000002529445359__huksimportkeyitem9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于导入时所需TAG和需要导入的密钥。callbackAsyncCallback<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>是回调函数。当导入密钥成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 以导入AES256密钥为例 */

let plainTextSize32 = makeRandomArr(32);

function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value:
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let options: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
huks.importKey(keyAlias, options, (err, data) => {
});
```

#### huks.importKey(deprecated)

importKey(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

导入明文密钥。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.importKeyItem9+](#ZH-CN_TOPIC_0000002529445359__huksimportkeyitem9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于导入时所需TAG和需要导入的密钥。

**返回值：**

类型说明Promise<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>Promise对象。返回HuksResult。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 以导入AES128为例 */

function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};

/* 第一步：生成密钥 */
let plainTextSize32 = makeRandomArr(32);
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
/* 第二步：导入密钥 */
let result = huks.importKey(keyAlias, huksOptions);
```

#### huks.exportKey(deprecated)

exportKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

导出密钥，使用Callback方式回调异步返回的结果。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.exportKeyItem9+](#ZH-CN_TOPIC_0000002529445359__huksexportkeyitem9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应与所用密钥生成时使用的别名相同。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是空对象（此处传空即可）。callbackAsyncCallback<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>是回调函数。当导出密钥成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。HuksResult的outData返回从密钥中导出的公钥。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.exportKey(keyAlias, emptyOptions, (err, data) => {
});
```

#### huks.exportKey(deprecated)

exportKey(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

导出密钥。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.exportKeyItem9+](#ZH-CN_TOPIC_0000002529445359__huksexportkeyitem9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应与所用密钥生成时使用的别名相同。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是空对象（此处传空即可）。

**返回值：**

类型说明Promise<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>Promise对象。返回HuksResult。HuksResult的outData返回从HUKS中导出的公钥。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.exportKey(keyAlias, emptyOptions);
```

#### huks.getKeyProperties(deprecated)

getKeyProperties(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

获取密钥属性。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.getKeyItemProperties9+](#ZH-CN_TOPIC_0000002529445359__huksgetkeyitemproperties9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应与所用密钥生成时使用的别名相同。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是空对象（此处传空即可）。callbackAsyncCallback<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>是回调函数。当获取密钥属性成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.getKeyProperties(keyAlias, emptyOptions, (err, data) => {
});
```

#### huks.getKeyProperties(deprecated)

getKeyProperties(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

获取密钥属性。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.getKeyItemProperties9+](#ZH-CN_TOPIC_0000002529445359__huksgetkeyitemproperties9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是密钥别名，应与所用密钥生成时使用的别名相同。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是空对象（此处传空即可）。

**返回值：**

类型说明Promise<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksoptions)>Promise对象。返回HuksResult。HuksResult的properties返回密钥参数。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.getKeyProperties(keyAlias, emptyOptions);
```

#### huks.isKeyExist(deprecated)

isKeyExist(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>) : void

判断密钥是否存在。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.isKeyItemExist9+](#ZH-CN_TOPIC_0000002529445359__huksiskeyitemexist9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是所需查找的密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于查询时指定密钥的属性TAG。callbackAsyncCallback<boolean>是回调函数。false代表密钥不存在，true代表密钥存在。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.isKeyExist(keyAlias, emptyOptions, (err, data) => {
});
```

#### huks.isKeyExist(deprecated)

isKeyExist(keyAlias: string, options: HuksOptions) : Promise<boolean>

判断密钥是否存在。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.isKeyItemExist9+](#ZH-CN_TOPIC_0000002529445359__huksiskeyitemexist9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是所需查找的密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是用于查询时指定密钥的属性TAG。

**返回值：**

类型说明Promise<boolean>Promise对象。false代表密钥不存在，true代表密钥存在。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.isKeyExist(keyAlias, emptyOptions);
```

#### huks.init(deprecated)

init(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksHandle>) : void

init操作密钥接口。使用callback异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.initSession9+](#ZH-CN_TOPIC_0000002529445359__huksinitsession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是Init操作密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是Init操作的参数集合。callbackAsyncCallback<[HuksHandle](#ZH-CN_TOPIC_0000002529445359__hukshandledeprecated)>是回调函数。当密钥操作init成功时，err为undefined，data为获取到的HuksHandle；否则为错误对象。HuksHandle的handle返回init生成的handle。

#### huks.init(deprecated)

init(keyAlias: string, options: HuksOptions) : Promise<HuksHandle>

init操作密钥接口。使用Promise异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.initSession9+](#ZH-CN_TOPIC_0000002529445359__huksinitsession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明keyAliasstring是Init操作密钥的别名。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是Init参数集合。

**返回值**：

类型说明Promise<[HuksHandle](#ZH-CN_TOPIC_0000002529445359__hukshandledeprecated)>Promise对象。返回HuksResult。HuksHandle的handle返回init生成的handle。

#### huks.update(deprecated)

update(handle: number, token?: Uint8Array, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

update操作密钥接口。使用callback异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.updateSession9+](#ZH-CN_TOPIC_0000002529445359__huksupdatesession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是Update操作的uint64类型的handle值。tokenUint8Array否Update操作的token。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是Update操作的参数集合。callbackAsyncCallback<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>是回调函数。当密钥操作update成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。

#### huks.update(deprecated)

update(handle: number, token?: Uint8Array, options: HuksOptions) : Promise<HuksResult>

update操作密钥接口。使用Promise异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.updateSession9+](#ZH-CN_TOPIC_0000002529445359__huksupdatesession9-2)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是Update操作的uint64类型的handle值。tokenUint8Array否Update操作的token。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是Update操作的参数集合。

**返回值**：

类型说明Promise<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>Promise对象。返回HuksResult。

#### huks.finish(deprecated)

finish(handle: number, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

finish操作密钥接口。使用callback异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.finishSession9+](#ZH-CN_TOPIC_0000002529445359__huksfinishsession9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是Finish操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是Finish的参数集合。callbackAsyncCallback<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>是回调函数。当密钥操作finish成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。

#### huks.finish(deprecated)

finish(handle: number, options: HuksOptions) : Promise<HuksResult>

finish操作密钥接口。使用Promise异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.finishSession9+](#ZH-CN_TOPIC_0000002529445359__huksfinishsession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是Finish操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是Finish操作的参数集合。

**返回值**：

类型说明Promise<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>Promise对象。返回HuksResult。

#### huks.abort(deprecated)

abort(handle: number, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

abort终止密钥操作。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.abortSession9+](#ZH-CN_TOPIC_0000002529445359__huksabortsession9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是Abort操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是Abort操作的参数集合。callbackAsyncCallback<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>是回调函数。当密钥操作abort成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* huks.init、huks.update、huks.finish为三段式接口，需要一起使用，
 * 当这三个操作中的任一阶段发生错误时，都需要调用huks.abort来终止密钥的使用
 *
 * 以下以RSA2048密钥的callback操作使用为例
 */

let keyAlias = "HuksDemoRSA";
let properties: Array<huks.HuksParam> = [];
let options: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(0)
};
let handle: number = 0;
let resultMessage = "";

async function generateKey() {
  properties = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  huks.generateKey(keyAlias, options);
}

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

async function huksInit() {
  await huks.init(keyAlias, options).then((data) => {
    console.info(`test init data: ${JSON.stringify(data)}`);
    handle = data.handle;
  });
}

async function huksUpdate() {
  options.inData = stringToUint8Array("huksHmacTest");
  await huks.update(handle, options.inData, options).then((data) => {
    if (data.errorCode === 0) {
      resultMessage += "update success!";
    } else {
      resultMessage += "update fail!";
    }
  });
  console.info(resultMessage);
}

function huksFinish() {
  options.inData = stringToUint8Array("HuksDemoHMAC");
  huks.finish(handle, options).then((data) => {
    if (data.errorCode === 0) {
      resultMessage = "finish success!";
      console.info(resultMessage);
    } else {
      resultMessage = "finish fail errorCode: " + data.errorCode;
      console.error(resultMessage);
    }
  });
}

async function huksAbort() {
  new Promise<huks.HuksResult>((resolve, reject) => {
    huks.abort(handle, options, (err, data) => {
      console.info(`huksAbort data ${JSON.stringify(data)}`);
      console.error(`huksAbort err ${JSON.stringify(err)}`);
    });
  });
}
```

#### huks.abort(deprecated)

abort(handle: number, options: HuksOptions) : Promise<HuksResult>

abort终止密钥操作。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.abortSession9+](#ZH-CN_TOPIC_0000002529445359__huksabortsession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

参数名类型必填说明handlenumber是Abort操作的uint64类型的handle值。options[HuksOptions](#ZH-CN_TOPIC_0000002529445359__huksoptions)是Abort操作的参数集合。

**返回值**：

类型说明Promise<[HuksResult](#ZH-CN_TOPIC_0000002529445359__huksresultdeprecated)>Promise对象。返回HuksResult。

**示例：**

```ets
import { huks } from '@kit.UniversalKeystoreKit';

/* huks.init、huks.update、huks.finish为三段式接口，需要一起使用，
 * 当这三个操作中的任一阶段发生错误时，都需要调用huks.abort来终止密钥的使用
 *
 * 以下以RSA2048密钥的promise操作使用为例
 */
let keyAlias = "HuksDemoRSA";
let properties: Array<huks.HuksParam> = [];
let options: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(0)
};
let handle: number = 0;
let resultMessage = "";

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

async function generateKey() {
  properties = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  huks.generateKey(keyAlias, options, (err, data) => {
    if (data.errorCode === 0) {
      resultMessage = "generate success!";
    } else {
      resultMessage = "generate fail errorCode: " + data.errorCode;
    }
  });
}

async function huksInit() {
  return new Promise<huks.HuksHandle>((resolve, reject) => {
    huks.init(keyAlias, options, async (err, data) => {
      if (data.errorCode === 0) {
        resultMessage = "init success!";
        handle = data.handle;
      } else {
        resultMessage = "init fail errorCode: " + data.errorCode;
      }
    });
  });
}

async function huksUpdate() {
  options.inData = stringToUint8Array("huksHmacTest");
  new Promise<huks.HuksResult>((resolve, reject) => {
    huks.update(handle, options.inData, options, (err, data) => {
      if (data.errorCode === 0) {
        resultMessage += "update success!";
        console.info(resultMessage);
      } else {
        resultMessage += "update fail!";
        console.error(resultMessage);
      }
    });
  });
}

async function huksFinish() {
  options.inData = stringToUint8Array("0");
  new Promise<huks.HuksResult>((resolve, reject) => {
    huks.finish(handle, options, (err, data) => {
      if (data.errorCode === 0) {
        resultMessage = "finish success!";
      } else {
        resultMessage = "finish fail errorCode: " + data.errorCode;
      }
    });
  });
}

function huksAbort() {
  huks.abort(handle, options).then((data) => {
    if (data.errorCode === 0) {
      console.info("abort success!");
    } else {
      console.error("abort fail errorCode: " + data.errorCode);
    }
  });
}
```

#### HuksHandle(deprecated)

huks Handle结构体。

**系统能力：** SystemCapability.Security.Huks.Extension

从API version 9开始废弃，建议使用[HuksSessionHandle9+](#ZH-CN_TOPIC_0000002529445359__hukssessionhandle9)替代。

名称类型只读可选说明errorCodenumber否否表示错误码。handlenumber否否表示无符号整数类型的handle值。tokenUint8Array否是表示[init](#ZH-CN_TOPIC_0000002529445359__huksinitdeprecated)操作之后获取到的challenge信息。默认为空。

#### HuksResult(deprecated)

调用接口返回的result。

**系统能力：** SystemCapability.Security.Huks.Extension

- 从API version 8开始支持，从API version 9开始废弃，建议使用[HuksReturnResult9+](#ZH-CN_TOPIC_0000002529445359__huksreturnresult9)替代。
- errorCode的具体信息，请参考[错误码文档](HUKS错误码.md)。

名称类型只读可选说明errorCodenumber否否表示错误码。outDataUint8Array否是表示输出数据。默认为空。propertiesArray<[HuksParam](#ZH-CN_TOPIC_0000002529445359__huksparam)>否是表示属性信息。默认为空。certChainsArray<string>否是表示证书链数据。默认为空。

#### HuksErrorCode(deprecated)

表示错误码的枚举。

**系统能力：** SystemCapability.Security.Huks.Extension

从API version 9开始废弃，建议使用[HuksExceptionErrCode9+](#ZH-CN_TOPIC_0000002529445359__huksexceptionerrcode9)替代。

名称值说明HUKS_SUCCESS0表示成功。HUKS_FAILURE-1表示失败。HUKS_ERROR_BAD_STATE-2表示错误的状态。HUKS_ERROR_INVALID_ARGUMENT-3表示无效的数据。HUKS_ERROR_NOT_SUPPORTED-4表示不支持。HUKS_ERROR_NO_PERMISSION-5表示没有许可。HUKS_ERROR_INSUFFICIENT_DATA-6表示数据不足。HUKS_ERROR_BUFFER_TOO_SMALL-7表示缓冲区太小。HUKS_ERROR_INSUFFICIENT_MEMORY-8表示内存不足。HUKS_ERROR_COMMUNICATION_FAILURE-9表示通讯失败。HUKS_ERROR_STORAGE_FAILURE-10表示存储故障。HUKS_ERROR_HARDWARE_FAILURE-11表示硬件故障。HUKS_ERROR_ALREADY_EXISTS-12表示已经存在。HUKS_ERROR_NOT_EXIST-13表示不存在。HUKS_ERROR_NULL_POINTER-14表示空指针。HUKS_ERROR_FILE_SIZE_FAIL-15表示文件大小失败。HUKS_ERROR_READ_FILE_FAIL-16表示读取文件失败。HUKS_ERROR_INVALID_PUBLIC_KEY-17表示无效的公钥。HUKS_ERROR_INVALID_PRIVATE_KEY-18表示无效的私钥。HUKS_ERROR_INVALID_KEY_INFO-19表示无效的密钥信息。HUKS_ERROR_HASH_NOT_EQUAL-20表示哈希不相等。HUKS_ERROR_MALLOC_FAIL-21表示MALLOC 失败。HUKS_ERROR_WRITE_FILE_FAIL-22表示写文件失败。HUKS_ERROR_REMOVE_FILE_FAIL-23表示删除文件失败。HUKS_ERROR_OPEN_FILE_FAIL-24表示打开文件失败。HUKS_ERROR_CLOSE_FILE_FAIL-25表示关闭文件失败。HUKS_ERROR_MAKE_DIR_FAIL-26表示创建目录失败。HUKS_ERROR_INVALID_KEY_FILE-27表示无效的密钥文件。HUKS_ERROR_IPC_MSG_FAIL-28表示IPC 信息失败。HUKS_ERROR_REQUEST_OVERFLOWS-29表示请求溢出。HUKS_ERROR_PARAM_NOT_EXIST-30表示参数不存在。HUKS_ERROR_CRYPTO_ENGINE_ERROR-31表示CRYPTO ENGINE错误。HUKS_ERROR_COMMUNICATION_TIMEOUT-32表示通讯超时。HUKS_ERROR_IPC_INIT_FAIL-33表示IPC 初始化失败。HUKS_ERROR_IPC_DLOPEN_FAIL-34表示IPC DLOPEN 失败。HUKS_ERROR_EFUSE_READ_FAIL-35表示EFUSE 读取失败。HUKS_ERROR_NEW_ROOT_KEY_MATERIAL_EXIST-36表示存在新的根密钥材料。HUKS_ERROR_UPDATE_ROOT_KEY_MATERIAL_FAIL-37表示更新根密钥材料失败。HUKS_ERROR_VERIFICATION_FAILED-38表示验证证书链失败。HUKS_ERROR_CHECK_GET_ALG_FAIL-100表示检查获取 ALG 失败。HUKS_ERROR_CHECK_GET_KEY_SIZE_FAIL-101表示检查获取密钥大小失败。HUKS_ERROR_CHECK_GET_PADDING_FAIL-102表示检查获取填充失败。HUKS_ERROR_CHECK_GET_PURPOSE_FAIL-103表示检查获取目的失败。HUKS_ERROR_CHECK_GET_DIGEST_FAIL-104表示检查获取摘要失败。HUKS_ERROR_CHECK_GET_MODE_FAIL-105表示检查获取模式失败。HUKS_ERROR_CHECK_GET_NONCE_FAIL-106表示检查获取随机数失败。HUKS_ERROR_CHECK_GET_AAD_FAIL-107表示检查获取 AAD 失败。HUKS_ERROR_CHECK_GET_IV_FAIL-108表示检查 GET IV 失败。HUKS_ERROR_CHECK_GET_AE_TAG_FAIL-109表示检查获取 AE 标记失败。HUKS_ERROR_CHECK_GET_SALT_FAIL-110表示检查获取SALT失败。HUKS_ERROR_CHECK_GET_ITERATION_FAIL-111表示检查获取迭代失败。HUKS_ERROR_INVALID_ALGORITHM-112表示无效的算法。HUKS_ERROR_INVALID_KEY_SIZE-113表示无效的密钥大小。HUKS_ERROR_INVALID_PADDING-114表示无效的填充。HUKS_ERROR_INVALID_PURPOSE-115表示无效的目的。HUKS_ERROR_INVALID_MODE-116表示无效模式。HUKS_ERROR_INVALID_DIGEST-117表示无效的摘要。HUKS_ERROR_INVALID_SIGNATURE_SIZE-118表示签名大小无效。HUKS_ERROR_INVALID_IV-119表示无效的 IV。HUKS_ERROR_INVALID_AAD-120表示无效的 AAD。HUKS_ERROR_INVALID_NONCE-121表示无效的随机数。HUKS_ERROR_INVALID_AE_TAG-122表示无效的 AE 标签。HUKS_ERROR_INVALID_SALT-123表示无效SALT。HUKS_ERROR_INVALID_ITERATION-124表示无效的迭代。HUKS_ERROR_INVALID_OPERATION-125表示无效操作。HUKS_ERROR_INTERNAL_ERROR-999表示内部错误。HUKS_ERROR_UNKNOWN_ERROR-1000表示未知错误。