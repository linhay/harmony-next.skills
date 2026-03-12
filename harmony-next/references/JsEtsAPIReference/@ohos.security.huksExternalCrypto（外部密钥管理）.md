# @ohos.security.huksExternalCrypto（外部密钥管理）

模块提供外部密钥管理扩展功能的注册与注销，PIN码认证与认证状态获取等。

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
```

#### HuksExternalCryptoTagType

表示外部加密数据类型的枚举。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

名称值说明HUKS_EXT_CRYPTO_TAG_TYPE_INT1 << 28表示TAG的值为整数类型。HUKS_EXT_CRYPTO_TAG_TYPE_BYTES5 << 28表示TAG的值为字节数组。

#### HuksExternalCryptoTag

表示指定参数tag类型的枚举。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

名称值说明HUKS_EXT_CRYPTO_TAG_UKEY_PINHuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_BYTES | 200001表示PIN码的TAG。HUKS_EXT_CRYPTO_TAG_ABILITY_NAMEHuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_BYTES | 200002表示[CryptoExtensionAbility](@ohos.security.CryptoExtensionAbility (密钥扩展能力).md)的名称。HUKS_EXT_CRYPTO_TAG_EXTRA_DATAHuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_BYTES | 200003外部数据，在通用查询场景，表示返回的数据。HUKS_EXT_CRYPTO_TAG_UIDHuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_INT | 200004表示调用方的uid。HUKS_EXT_CRYPTO_TAG_PURPOSEHuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_INT | 200005表示证书链对应密钥的使用类型，具体类型详见[CertificatePurpose定义](@ohos.security.certManager (证书管理模块).md#ZH-CN_TOPIC_0000002529445349__certificatepurpose22)。

#### HuksExternalCryptoParam

表示传入的参数类型定义。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

名称类型只读可选说明tag[HuksExternalCryptoTag](#ZH-CN_TOPIC_0000002497605394__huksexternalcryptotag)否否参数标签，用于区分参数。valueboolean|number|bigint|Uint8Array否否标签对应值。

#### HuksExternalPinAuthState

表示Ukey PIN码管理的状态值的枚举。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

名称值说明HUKS_EXT_CRYPTO_PIN_NO_AUTH0Ukey PIN未认证。HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED1Ukey PIN认证成功。HUKS_EXT_CRYPTO_PIN_LOCKED2Ukey PIN已锁定。

#### huksExternalCrypto.registerProvider

registerProvider(providerName: string, params: Array<HuksExternalCryptoParam>): Promise<void>

注册指定外部provider。使用Promise异步回调。

**需要权限**：ohos.permission.CRYPTO_EXTENSION_REGISTER

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

参数名类型必填说明providerNamestring是

provider名称，最大长度为128。建议包含厂商信息，全局唯一，不要包含个人联系方式等敏感数据。

最多支持注册10个provider。

paramsArray<[HuksExternalCryptoParam](#ZH-CN_TOPIC_0000002497605394__huksexternalcryptoparam)>是操作时需传入的参数，必选TAG：[HUKS_EXT_CRYPTO_TAG_ABILITY_NAME](#ZH-CN_TOPIC_0000002497605394__huksexternalcryptotag)，表示ability的名字，根据业务自己内部定义按照实际填写。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息201check permission failed.801api is not supported.12000002the ability name param is missing.12000005IPC communication failed.12000014memory is insufficient.12000018the input parameter is invalid.12000019the provider is already registered.12000020an error occurred in the dependent module.12000025the number of providers exceeds the limit.

**示例：**

```ets
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

const providerName = "testProviderName";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
  {
    tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
    value: StringToUint8Array("CryptoExtension")
  }
];
huksExternalCrypto.registerProvider(providerName, extProperties)
    .then((data) => {
        console.info(`promise: registerProvider success`);
    });
```

#### huksExternalCrypto.unregisterProvider

unregisterProvider(providerName: string, params?: Array<HuksExternalCryptoParam>): Promise<void>

注销provider。使用Promise异步回调。

**需要权限**：ohos.permission.CRYPTO_EXTENSION_REGISTER

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

参数名类型必填说明providerNamestring是provider名称，最大长度为128。建议包含厂商信息，全局唯一，不要包含个人联系方式等敏感数据。如果provider注册了多个扩展能力，则该provider下的扩展能力都会被注销。paramsArray<[HuksExternalCryptoParam](#ZH-CN_TOPIC_0000002497605394__huksexternalcryptoparam)>否

操作时需传入的参数。

可以在param参数中指定[HUKS_EXT_CRYPTO_TAG_ABILITY_NAME](#ZH-CN_TOPIC_0000002497605394__huksexternalcryptotag)，将根据“包名 + providerName + abilityName”注销对应的cryptoExtensionAbility。

如果未在params参数中指定[HUKS_EXT_CRYPTO_TAG_ABILITY_NAME](#ZH-CN_TOPIC_0000002497605394__huksexternalcryptotag)，或者未传入params参数，则注销对应的providerName下的所有Provider。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息201check permission failed.801api is not supported.12000005IPC communication failed.12000011the provider is not found.12000014memory is insufficient.12000018the input parameter is invalid.12000020an error occurred in the dependent module.

**示例：**

```ets
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

const providerName = "testProviderName";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
  {
    tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
    value: StringToUint8Array("CryptoExtension")
  }
];
huksExternalCrypto.unregisterProvider(providerName, extProperties)
    .then((data) => {
        console.info(`promise: unregisterProvider success`);
    });
```

#### huksExternalCrypto.getUkeyPinAuthState

getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>

获取PIN码认证状态。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

参数名类型必填说明resourceIdstring是资源ID，可通过[导出证书的接口](@ohos.security.certManagerDialog (证书管理对话框模块).md#ZH-CN_TOPIC_0000002497605384__certificatemanagerdialogopenauthorizedialog22)获取，其结果中附带资源ID。paramsArray<[HuksExternalCryptoParam](#ZH-CN_TOPIC_0000002497605394__huksexternalcryptoparam)>否操作的属性。

**返回值：**

类型说明Promise<[HuksExternalPinAuthState](#ZH-CN_TOPIC_0000002497605394__huksexternalpinauthstate)>

Promise对象，返回认证结果。

HUKS_EXT_CRYPTO_PIN_NO_AUTH 表示未认证；HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED 表示认证成功；HUKS_EXT_CRYPTO_PIN_LOCKED 表示PIN被锁定。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息801api is not supported.12000005IPC communication failed.12000006the Ukey driver operation failed.12000014memory is insufficient.12000018the input parameter is invalid.12000020the provider operation failed.12000024the provider or Ukey is busy.

**示例：**

```ets
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

const testResourceId = "{\"providerName\":\"testProviderName\", \"bundleName\":\"com.example.cryptoapplication\", \"userid\":100, \"abilityName\":\"CryptoExtension\",\"index\":{\"key\":\"testKey\"}}";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
huksExternalCrypto.getUkeyPinAuthState(testResourceId, extProperties)
    .then((data) => {
      console.info(`promise: getUkeyPinAuthState success, data: ${data}`);
    });
```

#### huksExternalCrypto.getProperty

getProperty(resourceId: string, propertyId: string, params?: Array<HuksExternalCryptoParam>): Promise<Array<HuksExternalCryptoParam>>

调用此接口获取属性值并返回结果。使用Promise异步回调。propertyId表示查询属性的ID信息，当前仅支持GMT 0016-2023中定义的SKF接口名作为属性ID，支持的ID包括如下：

- SKF_EnumDev
- SKF_GetDevInfo
- SKF_EnumApplication
- SKF_EnumContainer
- SKF_ExportPublicKey

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

参数名类型必填说明resourceIdstring是资源ID，可通过[导出证书的接口](@ohos.security.certManagerDialog (证书管理对话框模块).md#ZH-CN_TOPIC_0000002497605384__certificatemanagerdialogopenauthorizedialog22)获取，该接口的返回结果中附带resourceId。propertyIdstring是查找操作的属性名称，是GMT 0016-2023中定义的SKF接口名，应用开发者需要针对接口名进行适配。paramsArray<[HuksExternalCryptoParam](#ZH-CN_TOPIC_0000002497605394__huksexternalcryptoparam)>否需要传递给Extension Ability的输入参数。

**返回值：**

类型说明Promise<Array<[HuksExternalCryptoParam](#ZH-CN_TOPIC_0000002497605394__huksexternalcryptoparam)>>param数组，包含要查询的属性结果。

**错误码：**

以下错误码的详细介绍请参见[HUKS错误码](HUKS错误码.md)。

错误码ID错误信息12000006the Ukey driver operation failed.12000011if not found the cached resource id.12000014memory is insufficient.12000018the input parameter is invalid.12000020the provider operation failed.12000024the provider or Ukey is busy.

**示例：**

```ets
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

const testResourceId = JSON.stringify({
  providerName: "testProviderName",
  bundleName: "com.example.cryptoapplication",
  abilityName: "CryptoExtension",
  userid: 100,
  index: {
    key: "testKey"
  } as ESObject
});

let propertyId = "SKF_EnumDev";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

console.info(`promise: await huksExternalCrypto getProperty`);
async function testFunction() : Promise<void>
{
  try {
    await huksExternalCrypto.getProperty(testResourceId, propertyId, extProperties)
      .then((data) => {
        console.info(`promise: getProperty success, data: ` + JSON.stringify(data));
      });
  } catch (error) {
    console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
  }
}
```