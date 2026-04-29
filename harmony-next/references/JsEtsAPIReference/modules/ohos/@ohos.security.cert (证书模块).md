# @ohos.security.cert (证书模块)

证书算法库框架提供证书相关接口。其中，依赖加解密算法库框架的基础算法能力的部分，详细接口说明可参考[cryptoFramework API参考](@ohos.security.cryptoFramework (加解密算法库框架).md)。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

#### CertResult

表示执行结果的枚举。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID_PARAMS | 401 | 非法入参。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| NOT_SUPPORT | 801 | 操作不支持。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_OUT_OF_MEMORY | 19020001 | 内存错误。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_RUNTIME_ERROR | 19020002 | 运行时外部错误。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_PARAMETER_CHECK_FAILED20+ | 19020003 | 参数检查失败。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| ERR_CRYPTO_OPERATION | 19030001 | 调用三方算法库API出错。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_CERT_SIGNATURE_FAILURE | 19030002 | 证书签名验证错误。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_CERT_NOT_YET_VALID | 19030003 | 证书尚未生效。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_CERT_HAS_EXPIRED | 19030004 | 证书过期。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY | 19030005 | 无法获取证书的颁发者。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_KEYUSAGE_NO_CERTSIGN | 19030006 | 证书的密钥用途不含证书签名。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE | 19030007 | 证书的密钥用途不含数字签名。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_MAYBE_WRONG_PASSWORD18+ | 19030008 | 私钥密码错误。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

#### DataBlob

二进制数据的封装接口，核心字段data为Uint8Array类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 数据。 |

#### DataArray

buffer数组的列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Array<Uint8Array> | 否 | 否 | 数据列表。 |

#### EncodingFormat

表示证书编码格式的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FORMAT_DER | 0 | DER格式。 |
| FORMAT_PEM | 1 | PEM格式。 |
| FORMAT_PKCS711+ | 2 | PKCS7格式。 |

#### EncodingBaseFormat18+

表示生成CSR的编码格式的枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEM | 0 | PEM格式。 |
| DER | 1 | DER格式。 |

#### CsrAttribute18+

表示生成CSR的编码格式配置参数中的扩展。

openssl中规定了扩展类型，例如challengePassword、keyUsage等。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | openssl指定的扩展类型。 |
| value | string | 否 | 否 | 扩展值。 |

#### CsrGenerationConfig18+

RSA私钥生成CSR时的配置参数，包含主体、扩展、摘要算法、输出格式等。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| subject | X500DistinguishedName | 否 | 否 | X509定义的Name类型的对象。 |
| mdName | string | 否 | 否 | 摘要算法名。 |
| attributes | Array<CsrAttribute> | 否 | 是 | 扩展。 |
| outFormat | EncodingBaseFormat | 否 | 是 | 输出类型。 |


-

subject是X509定义的Name类型的对象。

-

mdName是摘要算法名，当前支持SHA1、SHA256、SHA384、SHA512。

-

attributes是可选参数，指定openssl中规定的扩展类型跟扩展值生成CSR。例如challengePassword、keyUsage等。

-

outFormat指定输出CSR的格式，若不指定默认为PEM格式。

#### CertItemType10+

表示获取证书字段的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CERT_ITEM_TYPE_TBS | 0 | 表示获取证书的待签名信息。 |
| CERT_ITEM_TYPE_PUBLIC_KEY | 1 | 表示获取证书的公钥信息。 |
| CERT_ITEM_TYPE_ISSUER_UNIQUE_ID | 2 | 表示获取证书的颁发者唯一编号。 |
| CERT_ITEM_TYPE_SUBJECT_UNIQUE_ID | 3 | 表示获取证书的主体唯一编号。 |
| CERT_ITEM_TYPE_EXTENSIONS | 4 | 表示获取证书的扩展域信息。 |

#### ExtensionOidType10+

表示获取扩展域中对象标识符类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXTENSION_OID_TYPE_ALL | 0 | 表示获取扩展域中所有的对象标识符。 |
| EXTENSION_OID_TYPE_CRITICAL | 1 | 表示获取扩展域中critical为true的对象标识符。 |
| EXTENSION_OID_TYPE_UNCRITICAL | 2 | 表示获取扩展域中critical为false的对象标识符。 |

#### ExtensionEntryType10+

表示获取扩展域中对象类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXTENSION_ENTRY_TYPE_ENTRY | 0 | 表示获取整个对象。 |
| EXTENSION_ENTRY_TYPE_ENTRY_CRITICAL | 1 | 表示获取对象的critical属性。 |
| EXTENSION_ENTRY_TYPE_ENTRY_VALUE | 2 | 表示获取对象的数据。 |

#### EncodingType12+

表示获取编码格式的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENCODING_UTF8 | 0 | UTF8编码格式。 |

#### EncodingBlob

带编码格式的证书二进制数组。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 传入的证书数据。 |
| encodingFormat | EncodingFormat | 否 | 否 | 指明证书编码格式。 |

#### CertChainData

证书链数据，在证书链校验时，作为入参传入。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 证书数据，按照长度（2字节）-数据的形式传入。如：08ABCDEFGH07ABCDEFG，第一本证书，前2个字节表示证书的长度为8字节，后面附加8字节的证书数据；第2本证书前2个字节表示证书的长度为7字节，后面附加7字节的证书数据。 |
| count | number | 否 | 否 | 传入的数据中，包含的证书数量。 |
| encodingFormat | EncodingFormat | 否 | 否 | 指明证书编码格式。 |

#### GeneralNameType12+

表示证书主体用途的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GENERAL_NAME_TYPE_OTHER_NAME | 0 | 表示其他名称。 |
| GENERAL_NAME_TYPE_RFC822_NAME | 1 | 表示电子邮件地址。 |
| GENERAL_NAME_TYPE_DNS_NAME | 2 | 表示一个DNS名称。 |
| GENERAL_NAME_TYPE_X400_ADDRESS | 3 | 表示X.400地址。 |
| GENERAL_NAME_TYPE_DIRECTORY_NAME | 4 | 表示一个目录名称。 |
| GENERAL_NAME_TYPE_EDI_PARTY_NAME | 5 | 表示特定的EDI实体。 |
| GENERAL_NAME_TYPE_UNIFORM_RESOURCE_ID | 6 | 表示一个统一资源标识符。 |
| GENERAL_NAME_TYPE_IP_ADDRESS | 7 | 表示一个IP地址。 |
| GENERAL_NAME_TYPE_REGISTERED_ID | 8 | 表示一个已注册的对象标识符。 |

#### GeneralName12+

用于表示证书主体信息对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | GeneralNameType | 否 | 否 | 指定具体的证书主体类型。 |
| name | Uint8Array | 否 | 是 | 指定具体的证书主体DER格式内容。 |

#### X509CertMatchParameters11+

用于匹配证书的过滤参数。如果参数中任一项都未指定，则匹配所有证书。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x509Cert | X509Cert | 否 | 是 | 指定具体的证书对象。 |
| validDate | string | 否 | 是 | 指定证书有效期。 |
| issuer | Uint8Array | 否 | 是 | 指定证书颁发者，为DER编码格式。 |
| keyUsage | Array<boolean> | 否 | 是 | 指定是否需要匹配密钥用途。true为需要，false为不需要。 |
| serialNumber | bigint | 否 | 是 | 指定证书的序列号。 |
| subject | Uint8Array | 否 | 是 | 指定证书主题，DER编码格式。 |
| publicKey | DataBlob | 否 | 是 | 指定证书公钥，DER编码格式。 |
| publicKeyAlgID | string | 否 | 是 | 指定证书公钥的算法。 |
| subjectAlternativeNames12+ | Array<GeneralName> | 否 | 是 | 指定证书主体名称。 |
| matchAllSubjectAltNames12+ | boolean | 否 | 是 | 指定是否需要匹配证书主体名称。true为需要，false为不需要。 |
| authorityKeyIdentifier12+ | Uint8Array | 否 | 是 | 指定证书颁发机构密钥。 |
| minPathLenConstraint12+ | number | 否 | 是 | 指定证书CA路径长度。 |
| extendedKeyUsage12+ | Array<string> | 否 | 是 | 指定证书扩展用途。 |
| nameConstraints12+ | Uint8Array | 否 | 是 | 指定证书的使用者名称。 |
| certPolicy12+ | Array<string> | 否 | 是 | 指定证书策略。 |
| privateKeyValid12+ | string | 否 | 是 | 指定证书私钥有效期。 |
| subjectKeyIdentifier12+ | Uint8Array | 否 | 是 | 指定证书公钥。 |

#### X509CRLMatchParameters11+

用于匹配证书吊销列表的过滤参数。如果参数中任一项都未指定，则匹配所有证书吊销列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| issuer | Array<Uint8Array> | 否 | 是 | 指定颁发者作为过滤条件, 至少要匹配到其中一个issuer。 |
| x509Cert | X509Cert | 否 | 是 | 指定具体的证书对象作为过滤条件, 判断该证书是否在CRL列表中。 |
| updateDateTime12+ | string | 否 | 是 | 指定证书更新时间。 |
| maxCRL12+ | bigint | 否 | 是 | 指定CRL个数最大值。 |
| minCRL12+ | bigint | 否 | 是 | 指定CRL个数最小值。 |

#### CertChainBuildParameters12+

用于指定证书链创建参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certMatchParameters | X509CertMatchParameters | 否 | 否 | 指定过滤条件。 |
| maxLength | number | 否 | 是 | 指定最终证书链中CA证书的最大长度。 |
| validationParameters | CertChainValidationParameters | 否 | 否 | 指定验证条件。 |

#### CertChainBuildResult12+

用于指定证书链创建结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certChain | X509CertChain | 是 | 否 | 生成的证书链对象。 |
| validationResult | CertChainValidationResult | 是 | 否 | 指定最终证书链的最大长度。 |

#### X509TrustAnchor11+

表示X509信任锚，用于校验证书链。使用信任锚中的证书或者公钥作为可信根，对证书链进行校验。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| CACert | X509Cert | 否 | 是 | 信任的CA证书。如果配置了CACert，则校验证书链时只使用CACert，不再使用CAPubKey和CASubject。 |
| CAPubKey | Uint8Array | 否 | 是 | 信任的CA证书公钥，DER格式。仅在未配置CACert时生效。 |
| CASubject | Uint8Array | 否 | 是 | 信任的CA证书主题，DER格式。仅在配置了CAPubKey时生效。校验对象根据CAPubKey类型（自签或上级）决定是校验根证书的主题还是颁发者。 |
| nameConstraints12+ | Uint8Array | 否 | 是 | 名称约束，DER格式。只校验当前证书链的叶子证书。 |

#### RevocationCheckOptions12+

表示证书链在线校验证书吊销状态选项的枚举。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REVOCATION_CHECK_OPTION_PREFER_OCSP | 0 | 优先采用OCSP进行校验，默认采用CRL校验。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| REVOCATION_CHECK_OPTION_ACCESS_NETWORK | 1 | 支持通过访问网络获取CRL或OCSP响应进行吊销状态的校验，默认为关闭。仅支持通过证书中的CDP扩展中获取首个CRL分发点地址以检查证书吊销状态，或通过AIA扩展获取首个OCSP服务器地址以进行吊销状态验证，且仅支持http协议。必须声明ohos.permission.INTERNET权限。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| REVOCATION_CHECK_OPTION_FALLBACK_NO_PREFER | 2 | 当ACCESS_NETWORK选项打开时有效，如果优选的校验方法由于网络原因导致无法校验证书状态，则采用备选的方案进行校验。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| REVOCATION_CHECK_OPTION_FALLBACK_LOCAL | 3 | 当ACCESS_NETWORK选项打开时有效，如果在线获取CRL和OCSP响应都由于网络的原因导致无法校验证书状态，则采用本地设置的CRL和OCSP响应进行校验。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| REVOCATION_CHECK_OPTION_CHECK_INTERMEDIATE_CA_ONLINE22+ | 4 | 当ACCESS_NETWORK选项打开时有效。如果开启了该能力，对终端实体证书OCSP或CRL校验失败，则会继续校验中间证书的吊销情况。默认关闭。 注意：当前能力与REVOCATION_CHECK_OPTION_LOCAL_CRL_ONLY_CHECK_END_ENTITY_CERT不能同时开启。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| REVOCATION_CHECK_OPTION_LOCAL_CRL_ONLY_CHECK_END_ENTITY_CERT22+ | 5 | 如果开启了该能力，则会拿本地吊销列表校验终端实体证书的吊销情况。默认关闭。 注意：当前能力与REVOCATION_CHECK_OPTION_CHECK_INTERMEDIATE_CA_ONLINE不能同时开启。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| REVOCATION_CHECK_OPTION_IGNORE_NETWORK_ERROR23+ | 6 | 如果开启了该能力，通过访问网络获取CRL或OCSP响应进行吊销状态的校验时，忽略网络不可达错误。默认关闭，默认情况下，网络不可达可能导致证书链校验失败。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |

#### ValidationPolicyType12+

表示证书链在线校验策略的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VALIDATION_POLICY_TYPE_X509 | 0 | 默认值，不需要校验证书中的sslHostname或dNSName。 |
| VALIDATION_POLICY_TYPE_SSL | 1 | 需要校验证书中的sslHostname或dNSName。 |

#### KeyUsageType12+

表示证书中密钥用途的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| KEYUSAGE_DIGITAL_SIGNATURE | 0 | 证书持有者可以用证书中包含的私钥进行数字签名操作。 |
| KEYUSAGE_NON_REPUDIATION | 1 | 证书持有者不可否认使用证书中包含的私钥进行的数字签名操作。 |
| KEYUSAGE_KEY_ENCIPHERMENT | 2 | 证书持有者可以使用证书中包含的公钥进行密钥加密操作。 |
| KEYUSAGE_DATA_ENCIPHERMENT | 3 | 证书持有者可以使用证书中包含的公钥进行数据加密操作。 |
| KEYUSAGE_KEY_AGREEMENT | 4 | 证书持有者可以使用证书中包含的私钥进行密钥协商操作。 |
| KEYUSAGE_KEY_CERT_SIGN | 5 | 证书持有者可以使用证书中包含的私钥对其他证书进行签名。 |
| KEYUSAGE_CRL_SIGN | 6 | 证书持有者可以使用证书中包含的私钥对证书吊销列表（CRL）进行签名。 |
| KEYUSAGE_ENCIPHER_ONLY | 7 | 证书持有者只能进行加密操作，不能进行解密操作。 |
| KEYUSAGE_DECIPHER_ONLY | 8 | 证书持有者只能进行解密操作，不能进行加密操作。 |

#### RevocationCheckParameter12+

表示证书链校验证书吊销状态的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ocspRequestExtension | Array<Uint8Array> | 否 | 是 | 表示发送OCSP请求的扩展字段。 |
| ocspResponderURI | string | 否 | 是 | 表示用于OCSP请求的备选服务器URI地址，支持HTTP/HTTPS，具体配置由与服务器协商决定。 说明：当前URI只针对实体证书生效。 |
| ocspResponderCert | X509Cert | 否 | 是 | 表示用于OCSP响应的签名校验的签名证书。 |
| ocspResponses | Uint8Array | 否 | 是 | 表示用于OCSP服务器响应的备选数据。 |
| crlDownloadURI | string | 否 | 是 | 表示用于CRL请求的备选下载地址。 说明：当前URI只针对实体证书生效。 |
| options | Array<RevocationCheckOptions> | 否 | 是 | 表示证书吊销状态查询的策略组合。 |
| ocspDigest | string | 否 | 是 | 表示OCSP通信时创建证书ID使用的哈希算法。默认为SHA256，支持可配置MD5、SHA1、SHA224、SHA256、SHA384、SHA512算法。 |

#### CertChainValidationParameters11+

表示证书链校验的参数。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| date | string | 否 | 是 | 表示需要校验证书的有效期。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| trustAnchors | Array<X509TrustAnchor> | 否 | 否 | 表示信任锚列表。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| trustSystemCa20+ | boolean | 否 | 是 | 表示是否使用系统预置CA证书校验证书链。true表示使用；false表示不使用。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| allowDownloadIntermediateCa23+ | boolean | 否 | 是 | 表示是否允许尝试从网络下载缺失的中间CA证书。 true表示允许；false表示不允许。默认值为false。 下载地址将从证书AIA扩展中获取，仅支持http，如需使用网络下载，需申请ohos.permission.INTERNET权限。配置方式请参见声明权限。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |
| certCRLs | Array<CertCRLCollection> | 否 | 是 | 表示需要校验证书是否在证书吊销列表中。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| revocationCheckParam12+ | RevocationCheckParameter | 否 | 是 | 表示需要在线校验证证书吊销状态的参数对象。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| policy12+ | ValidationPolicyType | 否 | 是 | 表示需要校验证书的策略类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| sslHostname12+ | string | 否 | 是 | 表示需要校验证书中主机名，与policy配合使用。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| keyUsage12+ | Array<KeyUsageType> | 否 | 是 | 表示需要校验证书中的密钥用途。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### CertChainValidationResult11+

表示证书链校验的返回值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trustAnchor | X509TrustAnchor | 是 | 否 | 表示信任锚。 |
| entityCert | X509Cert | 是 | 否 | 表示实体证书。 |

#### EncodingBaseFormat18+

编码基础格式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEM | 0 | 表示PEM格式。 |
| DER | 1 | 表示DER格式。 |

#### Pkcs12Data18+

表示返回P12文件的解析后的证书、私钥及其他证书合集。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| privateKey | string | Uint8Array | 否 | 是 | 表示P12文件解析后的私钥。 |
| cert | X509Cert | 否 | 是 | 表示P12文件解析后的证书。 |
| otherCerts | Array<X509Cert> | 否 | 是 | 表示P12文件解析后的其他证书合集。 |

#### Pkcs12ParsingConfig18+

表示解析P12文件的配置。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| password | string | 否 | 否 | 表示P12文件的密码。 |
| needsPrivateKey | boolean | 否 | 是 | 表示是否获取私钥。默认为true。 true为获取，返回PKCS8编码的私钥数据；false为不获取。 |
| privateKeyFormat | EncodingBaseFormat | 否 | 是 | 表示获取私钥的格式，当前支持PEM和DER格式。参数缺省时，默认为PEM格式。 注意：当needsPrivateKey值为true时，该参数生效。 |
| needsCert | boolean | 否 | 是 | 表示是否获取证书。默认为true。true为获取，false为不获取。 |
| needsOtherCerts | boolean | 否 | 是 | 表示是否获取其他证书合集。默认为false。true为获取，false为不获取。 |

#### PbesEncryptionAlgorithm21+

表示基于密码的加密算法枚举。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AES_128_CBC | 0 | AES-128-CBC加密算法。 |
| AES_192_CBC | 1 | AES-192-CBC加密算法。 |
| AES_256_CBC | 2 | AES-256-CBC加密算法。 |

#### PbesParams21+

表示基于密码的加密算法参数，当前仅支持PBES2。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| saltLen | number | 否 | 是 | 表示盐值长度。默认为16，最小值为8。 |
| iterations | number | 否 | 是 | 表示迭代次数。默认为2048。 |
| encryptionAlgorithm | PbesEncryptionAlgorithm | 否 | 是 | 表示PBES加密算法类型。默认为AES_256_CBC。 |

#### Pkcs12MacDigestAlgorithm21+

表示PKCS12 MAC摘要算法枚举。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHA256 | 0 | SHA256摘要算法。 |
| SHA384 | 1 | SHA384摘要算法。 |
| SHA512 | 2 | SHA512摘要算法。 |

#### Pkcs12CreationConfig21+

表示创建P12文件的配置。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| password | string | 否 | 否 | 表示P12文件的密码。最小长度为4。 |
| keyEncParams | PbesParams | 否 | 是 | 表示私钥加密的算法参数。 |
| encryptCert | boolean | 否 | 是 | 表示是否加密证书。默认为true。true为加密，false为不加密。 |
| certEncParams | PbesParams | 否 | 是 | 表示证书加密的算法参数。 |
| macSaltLen | number | 否 | 是 | 表示P12 MAC的盐值长度。最小值为8，默认为16。 |
| macIterations | number | 否 | 是 | 表示P12 MAC的迭代次数。默认为2048。 |
| macDigestAlgorithm | Pkcs12MacDigestAlgorithm | 否 | 是 | 表示P12 MAC的摘要算法。默认为SHA256。 |

#### CmsContentType18+

表示Cms内容类型的枚举。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIGNED_DATA | 0 | 签名数据。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| ENVELOPED_DATA22+ | 1 | 封装数据。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |

#### CmsContentDataFormat18+

表示Cms内容数据格式的枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BINARY | 0 | 表示二进制数据格式。 |
| TEXT | 1 | 表示文本数据格式。 |

#### CmsFormat18+

表示Cms签名格式的枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEM | 0 | 表示PEM格式。 |
| DER | 1 | 表示DER格式。 |

#### CmsRsaSignaturePadding22+

表示RSA类型CMS签名填充方式的枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PKCS1_PADDING | 0 | PKCS1填充方式。 |
| PKCS1_PSS_PADDING | 1 | PKCS1 PSS填充方式。 |

#### CmsKeyAgreeRecipientDigestAlgorithm22+

CMS KeyAgree类型接收者摘要算法的枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHA256 | 0 | SHA256 算法 |
| SHA384 | 1 | SHA384 算法 |
| SHA512 | 2 | SHA512 算法 |

#### CmsRecipientEncryptionAlgorithm22+

CMS接收者对称算法的枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AES_128_CBC | 0 | AES_128_CBC 算法 |
| AES_192_CBC | 1 | AES_192_CBC 算法 |
| AES_256_CBC | 2 | AES_256_CBC 算法 |
| AES_128_GCM | 3 | AES_128_GCM 算法 |
| AES_192_GCM | 4 | AES_192_GCM 算法 |
| AES_256_GCM | 5 | AES_256_GCM 算法 |

#### CmsCertType22+

从CMS中获取证书不同类型的枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIGNER_CERTS | 0 | 签名者证书 |
| ALL_CERTS | 1 | 全部证书 |

#### PrivateKeyInfo18+

表示私钥信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | Uint8Array | 否 | 否 | 未加密或加密的私钥，支持PEM或DER格式。 |
| password | string | 否 | 是 | 私钥的密码，如果私钥是加密的。 |

#### CmsSignerConfig18+

表示Cms签名者的配置选项。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mdName | string | 否 | 否 | 消息摘要算法的名称，例如 "SHA384", 当前支持"SHA1"、"SHA256"、"SHA384"、"SHA512"。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| rsaSignaturePadding22+ | CmsRsaSignaturePadding | 否 | 是 | RSA 签名填充方式。默认值为：PKCS1_PADDING。 当设置为 PKCS1_PSS_PADDING 时，mdName 必须为 "SHA256"、"SHA384" 或 "SHA512"。 说明：仅当签名者私钥类型为RSA时有效。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| addCert | boolean | 否 | 是 | 是否添加证书。默认为true。true为需要，false为不需要。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| addAttr | boolean | 否 | 是 | 是否添加签名属性。默认为true。true为需要，false为不需要。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| addSmimeCapAttr | boolean | 否 | 是 | 是否将SMIME能力添加到Cms对象。默认为true。true为需要，false为不需要。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

#### CmsKeyTransRecipientInfo22+

CMS封装数据的KeyTrans接收方信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cert | X509Cert | 否 | 否 | RSA证书。 |

#### CmsKeyAgreeRecipientInfo22+

CMS封装数据的KeyAgree接收方信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cert | X509Cert | 否 | 否 | EC证书。 |
| digestAlgorithm | CmsKeyAgreeRecipientDigestAlgorithm | 否 | 是 | KDF摘要算法，默认为SHA256。 |

#### CmsRecipientInfo22+

CMS封装数据的接收者信息。

至少需要设置一个接收者。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyTransInfo | CmsKeyTransRecipientInfo | 否 | 是 | keyTrans接收者信息。 |
| keyAgreeInfo | CmsKeyAgreeRecipientInfo | 否 | 是 | keyAgree接收者信息。 |

#### CmsGeneratorOptions18+

表示生成Cms签名结果的配置选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| contentDataFormat | CmsContentDataFormat | 否 | 是 | 内容数据的格式。默认为CmsContentDataFormat.BINARY。 |
| outFormat | CmsFormat | 否 | 是 | Cms最终数据的输出格式。默认为DER。 |
| isDetached | boolean | 否 | 是 | Cms最终数据是否不包含原始数据。默认为false。true为包含，false为不包含。 |

#### CmsVerificationConfig22+

CMS验证的配置。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trustCerts | Array<X509Cert> | 否 | 否 | 信任证书。 说明：需要配置所有签名者的信任证书。 |
| signerCerts | Array<X509Cert> | 否 | 是 | 签名证书。默认为空。 |
| contentData | Uint8Array | 否 | 是 | 内容数据，如果是detached模式，则需要指定明文数据。attached模式可以不传。 |
| contentDataFormat | CmsContentDataFormat | 否 | 是 | 内容数据的格式。默认为CmsContentDataFormat.BINARY。 |

#### CmsEnvelopedDecryptionConfig22+

CMS解封装的配置。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyInfo | PrivateKeyInfo | 否 | 是 | 私钥参数。默认为空。 |
| cert | X509Cert | 否 | 是 | 公钥证书。默认为空。 |
| encryptedContentData | Uint8Array | 否 | 是 | 加密的内容数据，如果CMS不包含指定数据。默认为空。 |
| contentDataFormat | CmsContentDataFormat | 否 | 是 | 内容数据的格式。默认为CmsContentDataFormat.BINARY。 |

#### cert.createX509Cert

createX509Cert(inStream : EncodingBlob, callback : AsyncCallback<X509Cert>) : void

表示创建X509证书对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | X509证书序列化数据。 |
| callback | AsyncCallback<X509Cert> | 是 | 回调函数，表示X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码]([证书错误码](../../errors/证书错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
  }
});
```

#### cert.createX509Cert

createX509Cert(inStream : EncodingBlob) : Promise<X509Cert>

表示创建X509证书对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | X509证书序列化数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<X509Cert> | 表示X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob).then(x509Cert => {
  console.info('createX509Cert result: success.');
}).catch((error: BusinessError) => {
  console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### X509Cert

X509证书类。

#### verify

verify(key : cryptoFramework.PubKey, callback : AsyncCallback<void>) : void

表示对证书验签。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | 是 | 用于验签的公钥对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数，使用AsyncCallback的第一个error参数判断是否验签成功，error为null表示成功，不为null表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');

    // 业务需通过上级X509Cert证书对象（或当前证书对象为自签名的证书）的getPublicKey获取PubKey。
    try {
      let pubKey = x509Cert.getPublicKey();

      // 验证证书签名。
      x509Cert.verify(pubKey, (err, data) => {
        if (err) {
          console.error(`verify failed, errCode: ${err.code}, errMsg: ${err.message}`);
        } else {
          console.info('verify result: success.');
        }
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getPublicKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### verify

verify(key : cryptoFramework.PubKey) : Promise<void>

表示对证书验签。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | 是 | 用于验签的公钥对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob).then(x509Cert => {
  console.info('createX509Cert result: success.');

  try {
    // 业务需通过上级X509Cert证书对象（或当前证书对象为自签名的证书）的getPublicKey获取PubKey。
    let pubKey = x509Cert.getPublicKey();
    x509Cert.verify(pubKey).then(result => {
      console.info('verify result: success.');
    }).catch((error: BusinessError) => {
      console.error(`verify failed, errCode: ${error.code}, errMsg: ${error.message}`);
    });
  } catch (error) {
    console.error(`getPublicKey failed: errCode: ${error.code}, errMsg: ${error.message}`);
  }
}).catch((error: BusinessError) => {
  console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### getEncoded

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取X509证书序列化数据。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<EncodingBlob> | 是 | 回调函数，表示X509证书序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    x509Cert.getEncoded((error, data) => {
      if (error) {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        console.info('getEncoded result: success.');
      }
    });
  }
});
```

#### getEncoded

getEncoded() : Promise<EncodingBlob>

表示获取X509证书序列化数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<EncodingBlob> | 表示X509证书序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
  'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
  'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
  'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
  'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
  '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
  'BetUokslUfjT6+s/X4ByaxycAA==\n' +
  '-----END CERTIFICATE-----\n';

// 证书二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};
cert.createX509Cert(encodingBlob).then(x509Cert => {
  console.info('createX509Cert result: success.');
  x509Cert.getEncoded().then(result => {
    console.info('getEncoded result: success.');
  }).catch((error: BusinessError) => {
    console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
  });
}).catch((error: BusinessError) => {
  console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### getPublicKey

getPublicKey() : cryptoFramework.PubKey

表示获取X509证书公钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| cryptoFramework.PubKey | X509证书公钥对象：仅用于X509Cert的verify接口。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let pubKey = x509Cert.getPublicKey();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getPublicKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
});
```

#### checkValidityWithDate

checkValidityWithDate(date: string) : void

表示检查X509证书有效期。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.Cert

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | string | 是 | 日期，为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |

示例：

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');

    let date = '231001000001Z';
    // Verify the certificate validity period.
    try {
      x509Cert.checkValidityWithDate(date);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`checkValidityWithDate failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
});
```

#### getVersion

getVersion() : number

表示获取X509证书版本。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.Cert

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 表示X509证书版本。 |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};
cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    let version = x509Cert.getVersion();
  }
});
```

#### getSerialNumber(deprecated)

getSerialNumber() : number

表示获取X509证书序列号。


从API version 9开始支持，从API version 10开始废弃，建议使用[getCertSerialNumber](#ZH-CN_TOPIC_0000002522081410__getcertserialnumber10)替代。

系统能力： SystemCapability.Security.Cert

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 表示X509证书序列号。 |

示例：

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    let serialNumber = x509Cert.getSerialNumber();
  }
});
```

#### getCertSerialNumber10+

getCertSerialNumber() : bigint

表示获取X509证书序列号。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.Cert

返回值：

| 类型 | 说明 |
| --- | --- |
| bigint | 表示X509证书序列号。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |

示例：

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let serialNumber = x509Cert.getCertSerialNumber();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getCertSerialNumber failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
});
```

#### getIssuerName

getIssuerName() : DataBlob

表示获取X509证书颁发者名称。

获取到的X509证书颁发者名称数据带字符串结束符。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.Cert

返回值：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书颁发者名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |

示例：

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let issuerName = x509Cert.getIssuerName();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getIssuerName20+

getIssuerName(encodingType: EncodingType): string

根据编码类型获取X509证书颁发者名称。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | EncodingType | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书颁发者名称，使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The value of encodingType is not in the EncodingType enumeration range. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIDgTCCAmmgAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMFcxCzAJBgNVBAYT\n' +
    'AkNOMQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG\n' +
    '5rWL6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwMzA1MDk1MTIzWhcN\n' +
    'MzUwMzAzMDk1MTIzWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8w\n' +
    'DQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH\n' +
    '5rWL6K+VMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkonJ4UIuxRzX\n' +
    'gr8fLU1PjadDWJp/GrxkYGe30TXqQHDh7O14Rc0xxacj3aLMNffzj+rhxUzl3C9p\n' +
    'wLzIVO2e3iC3Fx2csRzOSIdbimR8879/3uaW8CPkgqlKQw8FDwrGk0S26sdDV8of\n' +
    '8AAHlrnUO2yyL53rAunn4ZKo4EyxHrvHmZKuv006onj0SByu8RNHx97v+4KaaY7p\n' +
    'HngTC55F0KVALiNGygJHeKP7GGxS7kpYV/CvBuABpA00WMqc7nmo2vCa4yC/mIk2\n' +
    '5CF7l860rQ50HLjrmlDYJHpc8p88NJ2BEyHQWiN4YkSKDAKNr+SssD3Tf2wHSYxA\n' +
    'UwdgsatGlwIDAQABo1MwUTAdBgNVHQ4EFgQUMFEfTXLVm7D6fsC7LYtTMhIgVQUw\n' +
    'HwYDVR0jBBgwFoAUMFEfTXLVm7D6fsC7LYtTMhIgVQUwDwYDVR0TAQH/BAUwAwEB\n' +
    '/zANBgkqhkiG9w0BAQsFAAOCAQEABCr9+iK30OSp67ksK1qhkKCzwKYDH2E5KEF4\n' +
    '1E1/o4haXIR14V+5DGcX/1OH3Znd863TecQdNnCFMGArWygq8j7O0uStbWMb3Rhu\n' +
    '+7RJ9GOCbBSeR3v2fC6+T3LI0Sm1G77xIYADmHGt33IW0DRKr44iOalwi6IbcqzD\n' +
    's9XlNO8e6ht2apeL656fjv1gCo/PA7e+A0QHn6zapggzEccEwKdFixCsw5ZMZaHm\n' +
    'adGz3lBCK+0QKYXYL1CtX/6wcDgQ9PuZSgdQgrudLKRN+843m3LJSUJ7AIyL1kQW\n' +
    'kY1ah7eSx4wwaKrLOM06ZkzORMnY5GAy8Aup+UCh6mWU3dPv3w==\n' +
    '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let issuerName = x509Cert.getIssuerName(cert.EncodingType.ENCODING_UTF8);
      console.info('issuerName output is ' + issuerName);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSubjectName

getSubjectName(encodingType?: EncodingType) : DataBlob

表示获取X509证书主体名称。

获取到的X509证书主体名称数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | EncodingType | 否 | 编码类型。设置参数表示获取UTF8格式编码；不设置默认获取ASCII格式编码。 API 12后支持设置此参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书主体名称，转化成字符串后使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let subjectName = x509Cert.getSubjectName();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSubjectName failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
    try {
      let subjectNameutf8 = x509Cert.getSubjectName(cert.EncodingType.ENCODING_UTF8);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSubjectNameUtf8 failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getNotBeforeTime

getNotBeforeTime() : string

表示获取X509证书有效期起始时间。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书有效期起始时间，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let notBefore = x509Cert.getNotBeforeTime();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getNotBeforeTime failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getNotAfterTime

getNotAfterTime() : string

表示获取X509证书有效期截止时间。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书有效期截止时间，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let notAfter = x509Cert.getNotAfterTime();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getNotAfterTime failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignature

getSignature() : DataBlob

表示获取X509证书签名数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书签名数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let signature = x509Cert.getSignature();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignature failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignatureAlgName

getSignatureAlgName() : string

表示获取X509证书签名算法名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书签名算法名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let sigAlgName = x509Cert.getSignatureAlgName();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignatureAlgName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignatureAlgOid

getSignatureAlgOid() : string

表示获取X509证书签名算法的对象标志符OID(Object Identifier)。OID是由国际标准组织(ISO)的名称注册机构分配。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书签名算法对象标志符OID。若OID长度超过128字节，则会被截断。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let sigAlgOid = x509Cert.getSignatureAlgOid();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignatureAlgOid failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignatureAlgParams

getSignatureAlgParams() : DataBlob

表示获取X509证书签名算法参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书签名算法参数。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIEETCCAs6gAwIBAgIUKRqK4hH6D1p3NSuChKOwHnIVx74wOAYJKoZIhvcNAQEK\n' +
  'MCugDTALBglghkgBZQMEAgGhGjAYBgkqhkiG9w0BAQgwCwYJYIZIAWUDBAIBMG0x\n' +
  'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDAR0ZXN0MQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
  'VQQKDAR0ZXN0MQ0wCwYDVQQLDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MRMwEQYJKoZI\n' +
  'hvcNAQkBFgR0ZXN0MB4XDTI1MTAzMDAxNDAzMVoXDTI2MTAzMDAxNDAzMVowbTEL\n' +
  'MAkGA1UEBhMCRU4xDTALBgNVBAgMBHRlc3QxDTALBgNVBAcMBHhpYW4xDTALBgNV\n' +
  'BAoMBHRlc3QxDTALBgNVBAsMBHRlc3QxDTALBgNVBAMMBHRlc3QxEzARBgkqhkiG\n' +
  '9w0BCQEWBHRlc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaHZMj\n' +
  'UCQm53hgVYQq+kbmgKOH4e+vrsoAeOaX8KEgCbJfwLVpF7lj3Ld2c52X31JxziJx\n' +
  'D6rmGIk0Tp13/rNA/AZrmhbO/+PKKQiWQJpUbNI4A4scxELn9emLk8B3x76k8KGh\n' +
  'E7Re0XgKxfbZXU4AOZ0+9sXAZrSOPc8hYEfpwkGl09EojRuqQ4uSzjN3ikasfkZx\n' +
  'xM4twRPXiumC34+ep8Z1uxZy6MUClT2plNM8fAdfUwRY0lnKh2RjAJcK1lQBlPlW\n' +
  'Qc7S0/ifFXxgh+sBt+4dq+pphm5R/i6MIMWZ0JUg6tUlh1iY3nLVMVz0Z+LT7JUS\n' +
  '5ILjwwybwhtatFh5AgMBAAGjUzBRMB0GA1UdDgQWBBQM3AOhyH6sHP7CJAB/Z5Xy\n' +
  '4VQxJzAfBgNVHSMEGDAWgBQM3AOhyH6sHP7CJAB/Z5Xy4VQxJzAPBgNVHRMBAf8E\n' +
  'BTADAQH/MDgGCSqGSIb3DQEBCjAroA0wCwYJYIZIAWUDBAIBoRowGAYJKoZIhvcN\n' +
  'AQEIMAsGCWCGSAFlAwQCAQOCAQEAXhXExMyEnkBs9c6syxL4H98b9VtatezhKsMY\n' +
  'c4vTxw5D5IoN+SM+YS6wNKN1fh0fO8nZm7kHmB/KyxtdKja5cwGfhqwsY2NHOkK7\n' +
  'X5jWkbS0hbGPjj0UZkYRfC63d76lEPqz/bvf5Lgsv+W/J3ZFFBCV4tiBVr1ubpEy\n' +
  '/n+C1r2NMxOKfGOEdE8tPa5LiR85/MYFaaAvzHVX4irXsQmzXPJMaMWt2DJAAze3\n' +
  'ro0L1Hcd3VKyh5fYowA6nCDpNkKtQnVG/102SOM8HBH7wMSMHpsDzZbTuWRNJ35J\n' +
  'ach83y13Yx4Td+DVsZgNjl/7yeA+XdusunygAnqHqx2brCTaNw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let sigAlgParams = x509Cert.getSignatureAlgParams();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignatureAlgParams failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getKeyUsage

getKeyUsage() : DataBlob

表示获取X509证书密钥用途。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书密钥用途。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIDIjCCAgqgAwIBAgIUUb7sok900ODOxkyE1FzstJbKCSQwDQYJKoZIhvcNAQEL\n' +
    'BQAwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTI1MTAzMDAxNTQ0NFoX\n' +
    'DTI2MTAzMDAxNTQ0NFowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMIIBIjAN\n' +
    'BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv3+V/0Nl4rytCHNcb7PMpRbsxvOX\n' +
    '8zxwfb+5McmJ8ZZj59My3oqF7YgFM1VgZjjwaz8HljXvoaxrUJWQEu6AYjIa5ywN\n' +
    'duySyyNNgfbqiwUOVdUICh3WsEjvvxK+8f55L3xU0LybZxyEf0+31pc15SzCvTvv\n' +
    'E0OC8n3bYr2Nn0mvwtMHIl0Dr6AZbP10B/KKk68oX9UYOlsp4y0GTEXVDt/9bScx\n' +
    'PV2WvaKPWcrQoJVz1ys2RtyUgcwPiWugQdx54xHG6zIAMYptKxDaHgsOEtUR4J1p\n' +
    'xP1Ih7fY2wFZkeyRZG05ivYVqSHzHQV9Z42i+KjzfJUsMQt9TosuSsDi1wIDAQAB\n' +
    'o2AwXjAdBgNVHQ4EFgQUKF6T271JCNpwjwyCSzTSN66T95EwHwYDVR0jBBgwFoAU\n' +
    'KF6T271JCNpwjwyCSzTSN66T95EwDwYDVR0TAQH/BAUwAwEB/zALBgNVHQ8EBAMC\n' +
    'BaAwDQYJKoZIhvcNAQELBQADggEBACa9A6d/cdFb7h8EMmjs0l+3aIAI10EskgRT\n' +
    '+WHZ8zi+Q94/WEsOJW8CXIquJ2SxjXvl/A4UgrnfQyN+4kgEg7hLyuugg1QTk0so\n' +
    'Kj6tlG82Oxr/gjzxf3MMFhkzLpi2nUYu66HnskzAfI1XLuLz995qY0hCj9r2gUiX\n' +
    '6GR0H4p9pO5h9Fx7pbyosr2sn/JZbo9j6fWSuuvqoedjEuIb8aRmB6kbUkjhh/Iz\n' +
    '5htY+aYZz0pRSm2F93WLy6HBhPNdAmWOCpNXrynsRXDgCPKqeIasba8MBjXTsqvI\n' +
    'mgbc4MCLhLciWi34u9NpkAGbkwYVLE6URw/o373mD9fqe214Jdw=\n' +
    '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let keyUsage = x509Cert.getKeyUsage();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getKeyUsage failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getExtKeyUsage

getExtKeyUsage() : DataArray

表示获取X509证书扩展密钥用途。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataArray | 表示X509证书扩展密钥用途。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIDNDCCAhygAwIBAgIUJBLt/gmdgnDAq21wWU4R7rzgE5cwDQYJKoZIhvcNAQEL\n' +
    'BQAwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTI1MTAzMDAyMzMxOVoX\n' +
    'DTI2MTAzMDAyMzMxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMIIBIjAN\n' +
    'BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0p3wb2jK23w+mihsah0w4wRaJ1TC\n' +
    'YC20ODjSHyyCL75XfR6n87DdXvb15a71hkD/1cdgDRxIO91hNu04Ru4MFL0CqgTM\n' +
    'ERSwZZGVo9DzJSG5q22FgbIFPi+XpTPtKk7mOCggPsfIrV1G0OH9zTREWoZ2/fJD\n' +
    'Pj0MiaPlYtS4Jolu0qDnRZjgP8yVdaV4Upvni1PNX60rZfhf5YC4yvkMmpnyoUOZ\n' +
    'IS3I/QucXZaiwXAO4ziHjYXtlp2aeUnrWSoRs3sFrsIVGB9x0ZYjwCwiih9TqaBK\n' +
    'SY1CKSQE5xjVP1uY5JwJ6A5N648J3JjGosYEsXT+WieJ4SGHafGa2DGd2wIDAQAB\n' +
    'o3IwcDAdBgNVHQ4EFgQUDyuOK1aix/tBR3QViD7TYdrDUQEwHwYDVR0jBBgwFoAU\n' +
    'DyuOK1aix/tBR3QViD7TYdrDUQEwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHSUEFjAU\n' +
    'BggrBgEFBQcDAQYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAC0A7HqO/OL0\n' +
    'Ve8HTUqM31hFxXYiqDum/gPiegXDA+9ixEP2Fjz8vmhe75FX5XOvCk0+FWRayoVw\n' +
    'lc7TD7SfV/oHRZVY58H8+Qxe5Rf4xQfOBNpG81uz73gfq3zIbzfJXxWlUpnBs6Tf\n' +
    'P44NZboLpgaA0eMI7NwZJyomZ98qOK3PmxBL9qATmDep2GM6VlOuapYh2fo8wFhY\n' +
    'DSp2EmcbIN9F+RPNrP+BvM/x2ZBtBoSFLh8jQ+GnP6g26DL57JBuBemt00BuYLOg\n' +
    'fF00YBUgwK9tIFfI5IAfrwEF8Y49XIzpXrHuMZZXbuESzQMBsAZAYqIgi2p5dAon\n' +
    'gdg3C4I6QRY=\n' +
    '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let extKeyUsage = x509Cert.getExtKeyUsage();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getExtKeyUsage failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getBasicConstraints

getBasicConstraints() : number

表示获取X509证书基本约束。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示X509证书基本约束。 |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    let basicConstraints = x509Cert.getBasicConstraints();
  }
});
```

#### getSubjectAltNames

getSubjectAltNames() : DataArray

表示获取X509证书主体可选名称。

获取到的X509证书主体可选名称数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataArray | 表示X509证书主体可选名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIDRjCCAi6gAwIBAgIUU3RfsnV6Ur2a514YvAygbMvcjaowDQYJKoZIhvcNAQEL\n' +
    'BQAwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTI1MTAzMDAyNDIyM1oX\n' +
    'DTI2MTAzMDAyNDIyM1owGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMIIBIjAN\n' +
    'BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5yQDXUKnsNTPkqwVzCjtaE+Q8Tla\n' +
    'Qod6tb0fo044DLrYFvly6W10sqfvqZpuEfUuyzh/cs7279SoP8FYjnrykcE3yxqu\n' +
    '3N6vNn6iXm3CQnjlqBVB7ChTcoXv8GEwHNXcjNTaX3FZQW62WAYLLER4I9/ZwE/N\n' +
    'iqf+rJu5O2eRzZ4AFappCLquFSp6Yw5yyhenhNFd026dBf58ggpUs0H9DThxS3N3\n' +
    'GFUs6JDiOJpxjbv+p7ns9MsryqewB8i5TCJjMJkcCg+2YyKFKYDv3mC4eoV71MU0\n' +
    'DVoy7sBhs1naTV7joM+wGSOLcW3ee6K9qCp8zXmqN1tRJOYxm/JkVvi5oQIDAQAB\n' +
    'o4GDMIGAMB0GA1UdDgQWBBTXIqHf66clGd8UhAr2SJSaukwphDAfBgNVHSMEGDAW\n' +
    'gBTXIqHf66clGd8UhAr2SJSaukwphDAPBgNVHRMBAf8EBTADAQH/MC0GA1UdEQQm\n' +
    'MCSCC2V4YW1wbGUuY29tgg93d3cuZXhhbXBsZS5jb22HBH8AAAEwDQYJKoZIhvcN\n' +
    'AQELBQADggEBABI/bnHX9xqw/3RfvEqXp/ocmI0Dm7XwQZ6MS9XlTgYVp9rPYFbz\n' +
    'eS79q47nV1SMKc6LDeLoDcHT04aYGsKrA0O/9VVFhb50S1JBoa3HrEe0Q5WD4k48\n' +
    'GUJE2CaaO+MG3P9ZF4P3qxvPZ1PLoHr2B2YkaIMapjlNDUyTGLyWwPEuJSraBiXj\n' +
    'hnl1C9D5Y7ss8zuh4zzJl8MtU36kk19BbBglZVE0H7KDGGhqqvEbIFBNZmqy2vb3\n' +
    '7xSbXJL0/SQV+nr2Qvv8DU4XZJliJKVJHr3GkrqXRSFVVZ0ADNpEdLxFT0IF1X/T\n' +
    'JiAZrIdZPozWsjUVtQ4KVMJj+D7canRVuCg=\n' +
    '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let subjectAltNames = x509Cert.getSubjectAltNames();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSubjectAltNames failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getIssuerAltNames

getIssuerAltNames() : DataArray

表示获取X509证书颁发者可选名称。

获取到的X509证书颁发者可选名称数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataArray | 表示X509证书颁发者可选名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIC9zCCAd+gAwIBAgIUS3GIfzu10vWzw2RSLbxTxxMfz/wwDQYJKoZIhvcNAQEL\n' +
    'BQAwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTI1MTAzMDAyNDkzNFoX\n' +
    'DTI2MTAzMDAyNDkzNFowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMIIBIjAN\n' +
    'BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvKGnKn9NZoFOzdffrCIE01dTCiIo\n' +
    'XPweKanLs49ZaxpEJ48OCP4vs8qmedsW1pUMpe7kQQyRINZ5tvXyFbiBS1u4clN/\n' +
    'nU+E8rhNMa+2LA2YOUH/fC1ikussXq+acqjEqRbM900QdkmPzJX3NcloGYwdVfAe\n' +
    '3ENEXHaXvj1qrf6pF5mbdelnlp1TrjpnXT4sSQaKbFjZrNl+zTT4xbIxTHR0cB8S\n' +
    'oOVc3jI57rtP6x0FcLWzE/LX1E8eUkCIHEapPjqsGzLNtJTJI8z9QLinFIRmjdSI\n' +
    '0xS8Qj/QitrOswzjHie2fgaz1LZx76CZGExC5f6f3Em5hJx6rjYysmEZBQIDAQAB\n' +
    'ozUwMzAxBgNVHRIEKjAogRJpc3N1ZXJAZXhhbXBsZS5jb22CEmlzc3Vlci5leGFt\n' +
    'cGxlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAI5UjPssP3VzV2m47ke2nytAsTt9Y\n' +
    'DNYKhqM4qZVVaIj5BRmca1jJXnWAgV4uUbad92E7R8askfSuJkBVtLJD5kSMTQrK\n' +
    '5vYPbZ/WSRKthSbMotcynz/vWjBh4XY7bmiZC71ZNBCq9ybWRNzv61D9N1CJOlr6\n' +
    'W+1zCYq9dFDYf1nJ60qvkYHmzX3o0a1LHdiTHHvUZIIFXkJ50+NDIbruh8j8Lijk\n' +
    'Eed63QMcrSfLuIIAgoPoWo8WK2+AmA3k3EoTRvci5Ck+HDlLULBhyCrp+QUvn6OR\n' +
    'B7ZBoW+U/OIpNTI4rvsn3rcdkZAVcwRI0vV04IDB52jRzUArSi+08ggCiQ==\n' +
    '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let issuerAltNames = x509Cert.getIssuerAltNames();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getIssuerAltNames failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getItem10+

getItem(itemType: CertItemType) : DataBlob

表示获取X509证书对应的字段。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | CertItemType | 是 | 表示需要获取的证书字段。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书对应的字段，返回值为DER格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    try {
      let tbs = x509Cert.getItem(cert.CertItemType.CERT_ITEM_TYPE_TBS);
      let pubKey = x509Cert.getItem(cert.CertItemType.CERT_ITEM_TYPE_PUBLIC_KEY);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getItem failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### match11+

match(param: X509CertMatchParameters): boolean

判断证书是否与输入参数匹配。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | X509CertMatchParameters | 是 | 表示需要匹配的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 当参数匹配时，该方法返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509Cert(): Promise<cert.X509Cert> {
  let certData =  '-----BEGIN CERTIFICATE-----\n' +
  'MIIDTTCCAjWgAwIBAgIBAzANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
  'IENBMB4XDTI0MDMxOTAyMDM1NFoXDTM0MDMxNzAyMDM1NFowETEPMA0GA1UEAwwG\n' +
  'ZGV2aWNlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuoGk2J0aKWTP\n' +
  'J3D7lS3oFdME3MMA1z0Y0ftthrtUKybE2xh8P90ztMV73bewmgAPqiApqhaWEZM/\n' +
  '6DSLc/MxbOeYjg6njveJIu721gchiuB2PFikDFSWlcLOJNw+CgBx77Ct3KllivHs\n' +
  'oi/gjuxrWiF/3VhbBErPNj/fw9se3pVrFRXIFdkcybtom2mUmkcxDfSg587SO14i\n' +
  'ZzXGM6nhMzYWXxLho6SJrsnzfs4pD6ifksWmY4089zitqsN+9jQXafY1+/sh1mgu\n' +
  'FvAwg9IbigGOBIiF8t5qdNGpqCHXbEHblNCWfT4fVNDV0Vc9pByjZaMYEGMhpz+6\n' +
  'lxlc2CqbNQIDAQABo4GuMIGrMAkGA1UdEwQCMAAwHQYDVR0OBBYEFAEVpuP+pPpg\n' +
  'kr3dA3aV2XdFZ9rGMB8GA1UdIwQYMBaAFHRb+SgJu8O0UYdRBkszePocqxbYMB0G\n' +
  'A1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjALBgNVHQ8EBAMCB4AwMgYIKwYB\n' +
  'BQUHAQEEJjAkMCIGCCsGAQUFBzABhhZodHRwczovLzEyNy4wLjAuMTo5OTk5MA0G\n' +
  'CSqGSIb3DQEBCwUAA4IBAQBjM1agcDcgVHsD0dS39gxtlyRbZRvDcW3YsdwgpN6S\n' +
  'e4wGzdZbhsiZv7y3+PSuozKwp5Yjn+UqnnEz7QuTGJRt/pzHDVY3QceNvlx2HPRe\n' +
  'fECS4bpGLcM5B17oZZjE4HenIrGmigXnnwYL5TjhC4ybtddXPYv/M6z2eFCnfQNa\n' +
  'zFwz8LJ7ukWvf5koBqcHq2zsuVByOIPXLIrAJPtMmBb/pHCFt8hxOxwqujdrxz16\n' +
  'pe5LQUYzvG1YCxw3Ye9OrM1yXJQr/4KYncQC1yQQo+UK7NsDRK30PsMEYxhierLA\n' +
  'JKyPn1xSlOJiGa2rRn/uevmEOhfagj5TtprU9Gu1+nZo\n' +
  '-----END CERTIFICATE-----\n';

  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509Cert;
}

async function matchX509Cert() {
  const x509Cert = await createX509Cert();
  try {
    // 需业务自行赋值。
    const param: cert.X509CertMatchParameters = {
      x509Cert,
      validDate: '20241121074700Z',
      keyUsage: [true, false, false, false, false, false, false, false, false],
      publicKeyAlgID: '1.2.840.113549.1.1.1'
    };
    const result = x509Cert.match(param);
    console.info('call x509Cert match result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`call x509Cert match failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getCRLDistributionPoint12+

getCRLDistributionPoint(): DataArray

获取X509证书CRL的分发点统一资源标识符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataArray | 表示X509证书CRL的分发点统一资源标识符。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIB/jCCAaSgAwIBAgICA+gwCgYIKoZIzj0EAwIwLDELMAkGA1UEBhMCQ04xDTAL\n' +
  'BgNVBAoMBHRlc3QxDjAMBgNVBAMMBXN1YmNhMB4XDTIzMTAwNzA0MDEwOFoXDTMz\n' +
  'MTAwNDA0MDEwOFowLDELMAkGA1UEBhMCQ04xDTALBgNVBAoMBHRlc3QxDjAMBgNV\n' +
  'BAMMBWxvY2FsMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEZDPvdlJI6Yv4fiaR\n' +
  'nQHcusXVbukk90mQ0rBGOYRikFvgvm5cjTdaUGcQKEtwYIKDQl5n6Pf7ElCJ7GRz\n' +
  'raWZ+qOBtTCBsjAJBgNVHRMEAjAAMCwGCWCGSAGG+EIBDQQfFh1PcGVuU1NMIEdl\n' +
  'bmVyYXRlZCBDZXJ0aWZpY2F0ZTAdBgNVHQ4EFgQU63Gbl8gIsUn0VyZ4rya3PCjm\n' +
  'sfEwHwYDVR0jBBgwFoAU77mynM0rz1SD43DQjleWM7bF+MEwNwYDVR0fBDAwLjAs\n' +
  'oCqgKIYmaHR0cDovL3Rlc3QudGVzdENSTGRwLmNvbS9DUkxfRFBfMS5jcmwwCgYI\n' +
  'KoZIzj0EAwIDSAAwRQIhAISKHH9u221mBgdDWfll3loLvEHJ3or9NUO5Zn6SrX6L\n' +
  'AiAtRlOa6/mTD68faQTdhsAaQP955QfW34B4yFqU2Bq72A==\n' +
  '-----END CERTIFICATE-----\n';

  // 证书二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function certGetCRLDistributionPoint() {
  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
    console.info('createX509Cert result: success.');
    let point = x509Cert.getCRLDistributionPoint();
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getIssuerX500DistinguishedName12+

getIssuerX500DistinguishedName(): X500DistinguishedName

获取颁发者的X509可分辨名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| X500DistinguishedName | X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
  'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
  'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
  'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
  'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
  'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
  'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
  'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
  'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
  'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
  '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
  'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
  '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
  'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
  'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
  'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
  'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
  '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
  'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
  'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
  'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
  '-----END CERTIFICATE-----\n'

  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

async function certGetIssuerX500DistinguishedName() {
  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
    console.info('createX509Cert result: success.');
    let name = x509Cert.getIssuerX500DistinguishedName();
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getSubjectX500DistinguishedName12+

getSubjectX500DistinguishedName(): X500DistinguishedName

获取证书主题的X509可分辨名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| X500DistinguishedName | X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
  'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
  'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
  'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
  'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
  'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
  'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
  'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
  'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
  'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
  '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
  'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
  '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
  'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
  'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
  'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
  'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
  '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
  'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
  'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
  'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
  '-----END CERTIFICATE-----\n'

  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

async function certGetSubjectX500DistinguishedName() {
  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
    console.info('createX509Cert result: success.');
    let name = x509Cert.getSubjectX500DistinguishedName();
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### toString12+

toString(): string

获取对象的字符串类型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
  'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
  'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
  'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
  'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
  'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
  'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
  'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
  'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
  'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
  '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
  'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
  '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
  'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
  'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
  'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
  'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
  '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
  'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
  'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
  'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
  '-----END CERTIFICATE-----\n'

  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

async function certToString() {
  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
    console.info('createX509Cert result: success.');
    console.info('certToString success: ' + x509Cert.toString());
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### toString20+

toString(encodingType: EncodingType): string

根据编码类型获取对象的字符串类型数据。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | EncodingType | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The value of encodingType is not in the EncodingType enumeration range. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIDgTCCAmmgAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMFcxCzAJBgNVBAYT\n' +
    'AkNOMQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG\n' +
    '5rWL6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwMzA1MDk1MTIzWhcN\n' +
    'MzUwMzAzMDk1MTIzWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8w\n' +
    'DQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH\n' +
    '5rWL6K+VMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkonJ4UIuxRzX\n' +
    'gr8fLU1PjadDWJp/GrxkYGe30TXqQHDh7O14Rc0xxacj3aLMNffzj+rhxUzl3C9p\n' +
    'wLzIVO2e3iC3Fx2csRzOSIdbimR8879/3uaW8CPkgqlKQw8FDwrGk0S26sdDV8of\n' +
    '8AAHlrnUO2yyL53rAunn4ZKo4EyxHrvHmZKuv006onj0SByu8RNHx97v+4KaaY7p\n' +
    'HngTC55F0KVALiNGygJHeKP7GGxS7kpYV/CvBuABpA00WMqc7nmo2vCa4yC/mIk2\n' +
    '5CF7l860rQ50HLjrmlDYJHpc8p88NJ2BEyHQWiN4YkSKDAKNr+SssD3Tf2wHSYxA\n' +
    'UwdgsatGlwIDAQABo1MwUTAdBgNVHQ4EFgQUMFEfTXLVm7D6fsC7LYtTMhIgVQUw\n' +
    'HwYDVR0jBBgwFoAUMFEfTXLVm7D6fsC7LYtTMhIgVQUwDwYDVR0TAQH/BAUwAwEB\n' +
    '/zANBgkqhkiG9w0BAQsFAAOCAQEABCr9+iK30OSp67ksK1qhkKCzwKYDH2E5KEF4\n' +
    '1E1/o4haXIR14V+5DGcX/1OH3Znd863TecQdNnCFMGArWygq8j7O0uStbWMb3Rhu\n' +
    '+7RJ9GOCbBSeR3v2fC6+T3LI0Sm1G77xIYADmHGt33IW0DRKr44iOalwi6IbcqzD\n' +
    's9XlNO8e6ht2apeL656fjv1gCo/PA7e+A0QHn6zapggzEccEwKdFixCsw5ZMZaHm\n' +
    'adGz3lBCK+0QKYXYL1CtX/6wcDgQ9PuZSgdQgrudLKRN+843m3LJSUJ7AIyL1kQW\n' +
    'kY1ah7eSx4wwaKrLOM06ZkzORMnY5GAy8Aup+UCh6mWU3dPv3w==\n' +
    '-----END CERTIFICATE-----\n';

  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

async function certToString() {
  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
    console.info('createX509Cert result: success.');
    console.info('certToString success: ' + x509Cert.toString(cert.EncodingType.ENCODING_UTF8));
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### hashCode12+

hashCode(): Uint8Array

获取DER格式数据的哈希值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | DER格式数据的哈希值。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
  'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
  'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
  'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
  'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
  'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
  'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
  'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
  'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
  'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
  '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
  'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
  '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
  'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
  'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
  'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
  'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
  '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
  'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
  'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
  'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
  '-----END CERTIFICATE-----\n'

  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

async function certHashCode() {
  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
    console.info('createX509Cert result: success.');
    console.info('certHashCode success: ' + x509Cert.hashCode());
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getExtensionsObject12+

getExtensionsObject(): CertExtension

获取对应实体的扩展域DER格式数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| CertExtension | 证书扩展域段类对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIID1TCCAr2gAwIBAgIITXr1++kFUU4wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\n' +
  'BhMCQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xEjAQ\n' +
  'BgNVBAoTCXRlc3RTZWNDYTESMBAGA1UECxMJdGVzdFNlY0NhMRIwEAYDVQQDEwl0\n' +
  'ZXN0U2VjQ2EwHhcNMjMxMjIxMDAwMDAwWhcNMjcxMjIwMjM1OTU5WjBxMQswCQYD\n' +
  'VQQGEwJDTjEOMAwGA1UECBMFZ2Fuc3UxEDAOBgNVBAcTB2xhbnpob3UxFDASBgNV\n' +
  'BAoTC3Rlc3RUaGlyZENhMRQwEgYDVQQLEwt0ZXN0VGhpcmRDYTEUMBIGA1UEAxML\n' +
  'dGVzdFRoaXJkQ2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDJMKSq\n' +
  'Fn4G4EJATauw+4s+n/JbINBAiuhzURzzdt2T8JJQLDV9RHj4mZt84yv6lqEpl2fm\n' +
  'gIClfu173pEV51/PSq5IaV481u/Dz/OTy9TwfxmIXAWdNpyodDOg4I9K7LC01ge8\n' +
  'xxyKFi7k7m2eTGA4dYQM0E0AEXzCpg2JN3IIIPhzHCIVJmYjcbVxiaFkvT4ZFFUk\n' +
  '4rDSbAQdn6dJ29msrFm8iGhMGC/bzq9Bii38Qg4y4o89QYiboRWCxv3XfuibT+jw\n' +
  'O3pmfsFuT8/bKOWVm94FmRxiKuj6iE8UVewxtByzDgAsBtJKDjaCv3IkqfbIu+sq\n' +
  '/eeJkVJRJXAP3ZpLAgMBAAGjcjBwMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYE\n' +
  'FIxvPSwEmjOMW10H+gn2gy5HvMmMMAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEE\n' +
  'BAMCAAcwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0B\n' +
  'AQsFAAOCAQEAWu0u72g5y1weexPoJQnUgcwVtuC+/tTS9YvyCtKYE91gn97LSWn9\n' +
  'mXXGmLceU27B8JwhER9JeiQO1SUdDcvlfb5vt6eB+5cbZcgeERUBP8t0znh7DbMg\n' +
  '4TFjt9gZ970PZ1OlTBNPoZNRBKIox61KVUhiVKTVSbXlVP1yUF1uSlSq+0NYayHw\n' +
  'MnX1BeLxbAcAsTPYHjoeFJIrGkKlydLyt/8hDQzpLRW5uEUTjjqLh7vef0OaOP80\n' +
  'MmADt6ojRYvwdMDHF0ASJyupLQ+hiRLVadciK8Z5W34JGN2jwEw5X3nXyAgErIJZ\n' +
  'pqdTflnFLnSwy5M3QHB+xjYAcS9l1br2LA==\n' +
  '-----END CERTIFICATE-----\n'

  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

async function certGetExtensionsObject() {
  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
    console.info('createX509Cert result: success.');
    let object = x509Cert.getExtensionsObject();
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cert.createCertExtension10+

createCertExtension(inStream : EncodingBlob, callback : AsyncCallback<CertExtension>) : void

表示创建证书扩展域段的对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | 表示证书扩展域段序列化数据。 |
| callback | AsyncCallback<CertExtension> | 是 | 回调函数，表示扩展域段对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob, (error, certExt) => {
  if (error) {
    console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createCertExtension result: success.');
  }
});
```

#### cert.createCertExtension10+

createCertExtension(inStream : EncodingBlob) : Promise<CertExtension>

表示创建证书扩展域段的对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | 表示证书扩展域段序列化数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<CertExtension> | 表示证书扩展域段对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob).then(certExt => {
  console.info('createCertExtension result: success.');
}).catch((error: BusinessError) => {
  console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### CertExtension10+

证书扩展域段类。

#### getEncoded10+

getEncoded() : EncodingBlob

表示获取证书扩展域段序列化数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| EncodingBlob | 表示证书扩展域段序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob, (error, certExt) => {
  if (error) {
    console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createCertExtension result: success.');
    try {
      let extEncodedBlob = certExt.getEncoded();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`ext getEncoded failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getOidList10+

getOidList(valueType : ExtensionOidType) : DataArray

表示获取证书扩展域段对象标识符列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| valueType | ExtensionOidType | 是 | 表示证书扩展域段对象标识符类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataArray | 表示证书扩展域段对象标识符列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob, (error, certExt) => {
  if (error) {
    console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createCertExtension result: success.');
    try {
      let oidList = certExt.getOidList(cert.ExtensionOidType.EXTENSION_OID_TYPE_ALL);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`ext getOidList failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getEntry10+

getEntry(valueType: ExtensionEntryType, oid : DataBlob) : DataBlob

表示获取证书扩展域段对象信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| valueType | ExtensionEntryType | 是 | 表示证书扩展域段获取的类型。 |
| oid | DataBlob | 是 | 表示证书扩展域段获取的对象标识符。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示证书扩展域段对象的数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob, (error, certExt) => {
  if (error) {
    console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createCertExtension result: success.');
    let oid = new Uint8Array([0x32, 0x2e, 0x35, 0x2e, 0x32, 0x39, 0x2e, 0x31, 0x35]);
    let oidBlob: cert.DataBlob = {
      data: oid
    }
    try {
      let entry = certExt.getEntry(cert.ExtensionEntryType.EXTENSION_ENTRY_TYPE_ENTRY, oidBlob);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`ext getEntry failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### checkCA10+

checkCA() : number

表示校验证书是否为CA证书。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 当证书扩展域段中密钥用途包含签名用途，并且基本约束中cA字段为true时，表示证书为CA证书。如果不是CA，则返回-1；否则返回基本约束中的路径长度。如果证书是CA证书，但是基本约束中未给定路径长度，则返回-2，表示无路径长度限制。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};
cert.createCertExtension(encodingBlob, (error, certExt) => {
  if (error) {
    console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createCertExtension result: success.');
    try {
      let res = certExt.checkCA();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`ext checkCA failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### hasUnsupportedCriticalExtension11+

hasUnsupportedCriticalExtension(): boolean

判断是否存在不支持的关键扩展。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 当存在不支持的关键扩展时，该方法返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let encodingData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);
let encodingBlob: cert.EncodingBlob = {
  data: new Uint8Array(encodingData),
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob).then((extensionObj) => {
  console.info('createCertExtension result: success.');
  const result = extensionObj.hasUnsupportedCriticalExtension()
  console.info('has unsupported critical extension result =' + result);
}).catch((err: BusinessError) => {
  console.error(`createCertExtension failed, errCode: ${err.code}, errMsg: ${err.message}`);
});
```

#### cert.createX509Crl(deprecated)

createX509Crl(inStream : EncodingBlob, callback : AsyncCallback<X509Crl>) : void

表示创建X509证书吊销列表的对象。使用callback异步回调。


从API version 9开始支持，从API version 11开始废弃，建议使用[cert.createX509CRL](#ZH-CN_TOPIC_0000002522081410__certcreatex509crl11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | 表示证书吊销列表序列化数据。 |
| callback | AsyncCallback<X509Crl> | 是 | 回调函数，表示证书吊销列表对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
  }
});
```

#### cert.createX509Crl(deprecated)

createX509Crl(inStream : EncodingBlob) : Promise<X509Crl>

表示创建X509证书吊销列表的对象。使用Promise异步回调。


从API version 9开始支持，从API version 11开始废弃，建议使用[cert.createX509CRL](#ZH-CN_TOPIC_0000002522081410__certcreatex509crl11-1)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | 表示证书吊销列表序列化数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<X509Crl> | 表示证书吊销列表对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob).then(x509Crl => {
  console.info('createX509Crl result: success.');
}).catch((error: BusinessError) => {
  console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### cert.createX509CRL11+

createX509CRL(inStream : EncodingBlob, callback : AsyncCallback<X509CRL>) : void

表示创建X509证书吊销列表的对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | 表示证书吊销列表序列化数据。当前支持的数据长度不超过8192字节。 |
| callback | AsyncCallback<X509CRL> | 是 | 回调函数，表示证书吊销列表对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, X509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
  }
});
```

#### cert.createX509CRL11+

createX509CRL(inStream : EncodingBlob) : Promise<X509CRL>

表示创建X509证书吊销列表的对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | 表示证书吊销列表序列化数据。当前支持的数据长度不超过8192字节。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<X509CRL> | 表示证书吊销列表对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob).then(X509CRL => {
  console.info('createX509CRL result: success.');
}).catch((error: BusinessError) => {
  console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### X509Crl(deprecated)

X509证书吊销列表对象。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL](#ZH-CN_TOPIC_0000002522081410__x509crl11)替代。

#### isRevoked(deprecated)

isRevoked(cert : X509Cert) : boolean

表示检查证书是否吊销。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.isRevoked](#ZH-CN_TOPIC_0000002522081410__isrevoked11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | X509Cert | 是 | 表示被检查的证书对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 表示证书吊销状态，true表示已吊销，false表示未吊销。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
  'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
  'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
  'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
  'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
  '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
  'BetUokslUfjT6+s/X4ByaxycAA==\n' +
  '-----END CERTIFICATE-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

let certEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    // Create an X509Cert instance.
    cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
      if (error) {
        console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        try {
          let revokedFlag = x509Crl.isRevoked(x509Cert);
        } catch (error) {
          let e: BusinessError = error as BusinessError;
          console.error(`isRevoked failed, errCode: ${e.code}, errMsg: ${e.message}`);
      }
    });
  }
});
```

#### getType(deprecated)

getType() : string

表示获取证书吊销列表类型。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getType](#ZH-CN_TOPIC_0000002522081410__gettype11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示证书吊销列表类型。 |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    let type = x509Crl.getType();
  }
});
```

#### getEncoded(deprecated)

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取X509证书吊销列表的序列化数据。使用callback异步回调。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getEncoded](#ZH-CN_TOPIC_0000002522081410__getencoded11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<EncodingBlob> | 是 | 回调函数，表示X509证书吊销列表的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    x509Crl.getEncoded((error, data) => {
      if (error) {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        console.info('getEncoded result: success.');
      }
    });
  }
});
```

#### getEncoded(deprecated)

getEncoded() : Promise<EncodingBlob>

表示获取X509证书吊销列表的序列化数据。使用Promise异步回调。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getEncoded](#ZH-CN_TOPIC_0000002522081410__getencoded11-1)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<EncodingBlob> | 表示X509证书吊销列表的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob).then(x509Crl => {
  console.info('createX509Crl result: success.');
  x509Crl.getEncoded().then(result => {
    console.info('getEncoded result: success.');
  }).catch((error: BusinessError) => {
    console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
  });
}).catch((error: BusinessError) => {
  console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### verify(deprecated)

verify(key : cryptoFramework.PubKey, callback : AsyncCallback<void>) : void

表示对X509证书吊销列表进行验签。使用callback异步回调。验签支持RSA算法。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.verify](#ZH-CN_TOPIC_0000002522081410__verify11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | 是 | 表示用于验签的公钥对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数,使用AsyncCallback的第一个error参数判断是否验签成功，error为null表示成功，error不为null表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let pubKeyData = new Uint8Array([
  0x30, 0x81, 0x9F, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01,
  0x05, 0x00, 0x03, 0x81, 0x8D, 0x00, 0x30, 0x81, 0x89, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D,
  0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED, 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE,
  0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67, 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C,
  0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20, 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66,
  0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4, 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0,
  0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23, 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C,
  0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22, 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65,
  0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14, 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA,
  0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91, 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01,
  0x00, 0x01
]);

let priKeyData = new Uint8Array([
  0x30, 0x82, 0x02, 0x77, 0x02, 0x01, 0x00, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
  0x0D, 0x01, 0x01, 0x01, 0x05, 0x00, 0x04, 0x82, 0x02, 0x61, 0x30, 0x82, 0x02, 0x5D, 0x02, 0x01,
  0x00, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D, 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED,
  0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE, 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67,
  0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C, 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20,
  0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66, 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4,
  0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0, 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23,
  0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C, 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22,
  0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65, 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14,
  0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA, 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91,
  0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01, 0x00, 0x01, 0x02, 0x81, 0x80, 0x5A, 0xCF, 0x0F,
  0xF5, 0xA6, 0x1C, 0x19, 0x65, 0x8C, 0x94, 0x40, 0xF6, 0x84, 0x28, 0x74, 0x40, 0x42, 0x34, 0xDE,
  0xC3, 0x00, 0x5E, 0x72, 0x4D, 0x96, 0xE9, 0x4C, 0xBD, 0xC9, 0xDB, 0x14, 0x9F, 0xD5, 0xBB, 0xA9,
  0x0C, 0x20, 0xC2, 0xBE, 0x7A, 0x80, 0x89, 0xEC, 0x99, 0x04, 0xF0, 0xEE, 0x7B, 0x83, 0x20, 0x1D,
  0x37, 0x19, 0x55, 0x85, 0xF6, 0x8E, 0x3B, 0xFB, 0x16, 0xF3, 0xD3, 0x6F, 0xEE, 0x73, 0x12, 0x53,
  0xCA, 0x77, 0xD7, 0x6C, 0x29, 0xF5, 0x08, 0xA3, 0x09, 0x01, 0x0B, 0x00, 0x05, 0x57, 0xAD, 0x4D,
  0xF0, 0x92, 0xB2, 0x5A, 0x8B, 0x19, 0x09, 0x81, 0x86, 0xFE, 0x66, 0xB9, 0x33, 0x88, 0x28, 0xF3,
  0x37, 0x73, 0x09, 0x5F, 0xD7, 0xC9, 0xC6, 0xFA, 0x13, 0x74, 0xFE, 0xAE, 0x53, 0xA9, 0x71, 0x67,
  0xCE, 0x3A, 0xE6, 0x8D, 0x35, 0xD1, 0xB8, 0xFD, 0x6F, 0x0D, 0x43, 0xC2, 0xD1, 0x02, 0x41, 0x00,
  0xF7, 0x33, 0xE5, 0x6C, 0x29, 0x5A, 0x30, 0x58, 0xA4, 0x52, 0x65, 0xA0, 0x39, 0xC2, 0xE8, 0xAE,
  0x5F, 0xA3, 0x2D, 0x0C, 0x65, 0xB1, 0x7B, 0xFD, 0x92, 0xBF, 0x47, 0x87, 0x97, 0x40, 0xCB, 0x54,
  0xF9, 0xBB, 0x50, 0x27, 0x70, 0x51, 0xD0, 0xD8, 0x48, 0x0D, 0xC6, 0x47, 0x60, 0xF8, 0x4E, 0x0A,
  0x32, 0x76, 0x6D, 0xA4, 0xBA, 0x40, 0xE5, 0x58, 0xF8, 0x4A, 0x39, 0x4E, 0xF8, 0x3F, 0x4E, 0x2D,
  0x02, 0x41, 0x00, 0xE4, 0x23, 0x2A, 0x5F, 0x59, 0xCF, 0x7C, 0x91, 0x24, 0x0D, 0xA2, 0x44, 0x17,
  0xCD, 0x37, 0xDE, 0x1F, 0x53, 0x4D, 0x33, 0x9F, 0x90, 0x4D, 0xD9, 0x72, 0x64, 0x25, 0xBA, 0xAB,
  0x47, 0x91, 0xC4, 0x99, 0x95, 0x86, 0xB5, 0x8A, 0xEA, 0x77, 0xF7, 0x64, 0x72, 0x5E, 0xB7, 0xBB,
  0x16, 0xA1, 0x64, 0xA4, 0xE1, 0x2D, 0x76, 0x6D, 0xEF, 0xB1, 0x5E, 0xD6, 0x17, 0xE8, 0xAA, 0xB6,
  0xA0, 0xD9, 0x85, 0x02, 0x41, 0x00, 0xDF, 0xC8, 0x5B, 0x28, 0x4F, 0x47, 0x15, 0xFD, 0x28, 0xC4,
  0x6E, 0xBB, 0x5D, 0x8E, 0xD4, 0x95, 0x06, 0x7E, 0xF1, 0x89, 0x07, 0x86, 0x64, 0x78, 0x69, 0x20,
  0x3F, 0xE0, 0xBF, 0x4C, 0x28, 0xC6, 0x04, 0x4D, 0x4D, 0x82, 0x66, 0x6B, 0xAA, 0x64, 0x20, 0xD6,
  0x57, 0x68, 0xC6, 0xA0, 0x02, 0x05, 0xB9, 0x28, 0xFC, 0x98, 0xE3, 0x03, 0x5C, 0x9B, 0xEE, 0x29,
  0x43, 0x37, 0xFA, 0x03, 0x55, 0x01, 0x02, 0x40, 0x69, 0x5B, 0x7C, 0x24, 0x10, 0xDB, 0xEB, 0x91,
  0x33, 0xEF, 0x3F, 0xF2, 0xE6, 0x73, 0x15, 0xCB, 0xF4, 0xF7, 0x89, 0x7D, 0xBF, 0xC0, 0xEA, 0xD2,
  0xF3, 0x2B, 0x20, 0xE9, 0x76, 0x54, 0x55, 0x13, 0x50, 0x42, 0x67, 0xB5, 0xCB, 0x73, 0xC0, 0xF7,
  0x75, 0x62, 0x04, 0x30, 0x21, 0xAC, 0xAF, 0xD8, 0x44, 0xF4, 0xE1, 0x04, 0x02, 0x7D, 0x61, 0x92,
  0x84, 0x99, 0x02, 0x10, 0x64, 0xCB, 0x1F, 0xE9, 0x02, 0x41, 0x00, 0xAB, 0x4B, 0x7D, 0x90, 0x7C,
  0x57, 0x08, 0x6B, 0xC0, 0x43, 0x72, 0x09, 0x8A, 0x18, 0x35, 0x36, 0x64, 0x9D, 0x84, 0x8D, 0xF1,
  0x84, 0x94, 0x48, 0xC6, 0x80, 0x9D, 0xB9, 0xA2, 0x58, 0x0A, 0x4D, 0x0A, 0xCA, 0x1E, 0xD6, 0x05,
  0x55, 0x5B, 0xFE, 0xD7, 0xAA, 0x70, 0xED, 0x76, 0xB3, 0x40, 0x2E, 0xA0, 0xB3, 0x32, 0x37, 0xB0,
  0xA0, 0xB9, 0x96, 0x2D, 0xC4, 0x70, 0xE9, 0x99, 0x10, 0x67, 0x8D
]);

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      // Generate the public key by AsyKeyGenerator.
      let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
      console.info('createAsyKeyGenerator result: success.');
      let priEncodingBlob: cryptoFramework.DataBlob = {
        data: priKeyData,
      };
      let pubEncodingBlob: cryptoFramework.DataBlob = {
        data: pubKeyData,
      };
      keyGenerator.convertKey(pubEncodingBlob, priEncodingBlob, (e, keyPair) => {
        if (e) {
          console.error(`convert key failed, errCode: ${e.code}, errMsg: ${e.message}`);
        } else {
          console.info('convert key result: success.');
          x509Crl.verify(keyPair.pubKey, (err, data) => {
            if (err) {
              console.error(`verify failed, errCode: ${err.code}, errMsg: ${err.message}`);
            } else  {
              console.info('verify result: success.');
            }
          });
        }
      })
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### verify(deprecated)

verify(key : cryptoFramework.PubKey) : Promise<void>

表示对X509证书吊销列表进行验签。使用Promise异步回调。验签支持RSA算法。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.verify](#ZH-CN_TOPIC_0000002522081410__verify11-1)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | 是 | 表示用于验签的公钥对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit'
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let pubKeyData = new Uint8Array([
  0x30, 0x81, 0x9F, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01,
  0x05, 0x00, 0x03, 0x81, 0x8D, 0x00, 0x30, 0x81, 0x89, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D,
  0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED, 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE,
  0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67, 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C,
  0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20, 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66,
  0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4, 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0,
  0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23, 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C,
  0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22, 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65,
  0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14, 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA,
  0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91, 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01,
  0x00, 0x01
]);

let priKeyData = new Uint8Array([
  0x30, 0x82, 0x02, 0x77, 0x02, 0x01, 0x00, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
  0x0D, 0x01, 0x01, 0x01, 0x05, 0x00, 0x04, 0x82, 0x02, 0x61, 0x30, 0x82, 0x02, 0x5D, 0x02, 0x01,
  0x00, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D, 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED,
  0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE, 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67,
  0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C, 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20,
  0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66, 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4,
  0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0, 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23,
  0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C, 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22,
  0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65, 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14,
  0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA, 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91,
  0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01, 0x00, 0x01, 0x02, 0x81, 0x80, 0x5A, 0xCF, 0x0F,
  0xF5, 0xA6, 0x1C, 0x19, 0x65, 0x8C, 0x94, 0x40, 0xF6, 0x84, 0x28, 0x74, 0x40, 0x42, 0x34, 0xDE,
  0xC3, 0x00, 0x5E, 0x72, 0x4D, 0x96, 0xE9, 0x4C, 0xBD, 0xC9, 0xDB, 0x14, 0x9F, 0xD5, 0xBB, 0xA9,
  0x0C, 0x20, 0xC2, 0xBE, 0x7A, 0x80, 0x89, 0xEC, 0x99, 0x04, 0xF0, 0xEE, 0x7B, 0x83, 0x20, 0x1D,
  0x37, 0x19, 0x55, 0x85, 0xF6, 0x8E, 0x3B, 0xFB, 0x16, 0xF3, 0xD3, 0x6F, 0xEE, 0x73, 0x12, 0x53,
  0xCA, 0x77, 0xD7, 0x6C, 0x29, 0xF5, 0x08, 0xA3, 0x09, 0x01, 0x0B, 0x00, 0x05, 0x57, 0xAD, 0x4D,
  0xF0, 0x92, 0xB2, 0x5A, 0x8B, 0x19, 0x09, 0x81, 0x86, 0xFE, 0x66, 0xB9, 0x33, 0x88, 0x28, 0xF3,
  0x37, 0x73, 0x09, 0x5F, 0xD7, 0xC9, 0xC6, 0xFA, 0x13, 0x74, 0xFE, 0xAE, 0x53, 0xA9, 0x71, 0x67,
  0xCE, 0x3A, 0xE6, 0x8D, 0x35, 0xD1, 0xB8, 0xFD, 0x6F, 0x0D, 0x43, 0xC2, 0xD1, 0x02, 0x41, 0x00,
  0xF7, 0x33, 0xE5, 0x6C, 0x29, 0x5A, 0x30, 0x58, 0xA4, 0x52, 0x65, 0xA0, 0x39, 0xC2, 0xE8, 0xAE,
  0x5F, 0xA3, 0x2D, 0x0C, 0x65, 0xB1, 0x7B, 0xFD, 0x92, 0xBF, 0x47, 0x87, 0x97, 0x40, 0xCB, 0x54,
  0xF9, 0xBB, 0x50, 0x27, 0x70, 0x51, 0xD0, 0xD8, 0x48, 0x0D, 0xC6, 0x47, 0x60, 0xF8, 0x4E, 0x0A,
  0x32, 0x76, 0x6D, 0xA4, 0xBA, 0x40, 0xE5, 0x58, 0xF8, 0x4A, 0x39, 0x4E, 0xF8, 0x3F, 0x4E, 0x2D,
  0x02, 0x41, 0x00, 0xE4, 0x23, 0x2A, 0x5F, 0x59, 0xCF, 0x7C, 0x91, 0x24, 0x0D, 0xA2, 0x44, 0x17,
  0xCD, 0x37, 0xDE, 0x1F, 0x53, 0x4D, 0x33, 0x9F, 0x90, 0x4D, 0xD9, 0x72, 0x64, 0x25, 0xBA, 0xAB,
  0x47, 0x91, 0xC4, 0x99, 0x95, 0x86, 0xB5, 0x8A, 0xEA, 0x77, 0xF7, 0x64, 0x72, 0x5E, 0xB7, 0xBB,
  0x16, 0xA1, 0x64, 0xA4, 0xE1, 0x2D, 0x76, 0x6D, 0xEF, 0xB1, 0x5E, 0xD6, 0x17, 0xE8, 0xAA, 0xB6,
  0xA0, 0xD9, 0x85, 0x02, 0x41, 0x00, 0xDF, 0xC8, 0x5B, 0x28, 0x4F, 0x47, 0x15, 0xFD, 0x28, 0xC4,
  0x6E, 0xBB, 0x5D, 0x8E, 0xD4, 0x95, 0x06, 0x7E, 0xF1, 0x89, 0x07, 0x86, 0x64, 0x78, 0x69, 0x20,
  0x3F, 0xE0, 0xBF, 0x4C, 0x28, 0xC6, 0x04, 0x4D, 0x4D, 0x82, 0x66, 0x6B, 0xAA, 0x64, 0x20, 0xD6,
  0x57, 0x68, 0xC6, 0xA0, 0x02, 0x05, 0xB9, 0x28, 0xFC, 0x98, 0xE3, 0x03, 0x5C, 0x9B, 0xEE, 0x29,
  0x43, 0x37, 0xFA, 0x03, 0x55, 0x01, 0x02, 0x40, 0x69, 0x5B, 0x7C, 0x24, 0x10, 0xDB, 0xEB, 0x91,
  0x33, 0xEF, 0x3F, 0xF2, 0xE6, 0x73, 0x15, 0xCB, 0xF4, 0xF7, 0x89, 0x7D, 0xBF, 0xC0, 0xEA, 0xD2,
  0xF3, 0x2B, 0x20, 0xE9, 0x76, 0x54, 0x55, 0x13, 0x50, 0x42, 0x67, 0xB5, 0xCB, 0x73, 0xC0, 0xF7,
  0x75, 0x62, 0x04, 0x30, 0x21, 0xAC, 0xAF, 0xD8, 0x44, 0xF4, 0xE1, 0x04, 0x02, 0x7D, 0x61, 0x92,
  0x84, 0x99, 0x02, 0x10, 0x64, 0xCB, 0x1F, 0xE9, 0x02, 0x41, 0x00, 0xAB, 0x4B, 0x7D, 0x90, 0x7C,
  0x57, 0x08, 0x6B, 0xC0, 0x43, 0x72, 0x09, 0x8A, 0x18, 0x35, 0x36, 0x64, 0x9D, 0x84, 0x8D, 0xF1,
  0x84, 0x94, 0x48, 0xC6, 0x80, 0x9D, 0xB9, 0xA2, 0x58, 0x0A, 0x4D, 0x0A, 0xCA, 0x1E, 0xD6, 0x05,
  0x55, 0x5B, 0xFE, 0xD7, 0xAA, 0x70, 0xED, 0x76, 0xB3, 0x40, 0x2E, 0xA0, 0xB3, 0x32, 0x37, 0xB0,
  0xA0, 0xB9, 0x96, 0x2D, 0xC4, 0x70, 0xE9, 0x99, 0x10, 0x67, 0x8D
]);

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob).then(x509Crl => {
  console.info('createX509Crl result: success.');

  try {
    // 生成公钥对象。
    let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
    console.info('createAsyKeyGenerator result: success.');
    let priEncodingBlob: cryptoFramework.DataBlob = {
      data: priKeyData,
    };
    let pubEncodingBlob: cryptoFramework.DataBlob = {
      data: pubKeyData,
    };
    keyGenerator.convertKey(pubEncodingBlob, priEncodingBlob).then((keyPair) => {
      console.info('convert key result: success.');
      x509Crl.verify(keyPair.pubKey).then(result => {
        console.info('verify result: success.');
      }).catch((error: BusinessError) => {
        console.error(`verify failed, errCode: ${error.code}, errMsg: ${error.message}`);
      });
    }).catch((error: BusinessError) => {
      console.error(`convert key failed, errCode: ${error.code}, errMsg: ${error.message}`);
    });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}).catch((error: BusinessError) => {
  console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### getVersion(deprecated)

getVersion() : number

表示获取X509证书吊销列表的版本号。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getVersion](#ZH-CN_TOPIC_0000002522081410__getversion11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示获取X509证书吊销列表的版本号。 |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    let version = x509Crl.getVersion();
  }
});
```

#### getIssuerName(deprecated)

getIssuerName() : DataBlob

表示获取X509证书吊销列表颁发者名称。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getIssuerName](#ZH-CN_TOPIC_0000002522081410__getissuername11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书吊销列表颁发者名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      let issuerName = x509Crl.getIssuerName();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getLastUpdate(deprecated)

getLastUpdate() : string

表示获取X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getLastUpdate](#ZH-CN_TOPIC_0000002522081410__getlastupdate11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      let lastUpdate = x509Crl.getLastUpdate();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getLastUpdate failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getNextUpdate(deprecated)

getNextUpdate() : string

表示获取证书吊销列表下一次更新的日期，日期为ASN.1时间格式。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getNextUpdate](#ZH-CN_TOPIC_0000002522081410__getnextupdate11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表下一次更新的日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      let nextUpdate = x509Crl.getNextUpdate();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getNextUpdate failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getRevokedCert(deprecated)

getRevokedCert(serialNumber : number) : X509CrlEntry

表示通过指定证书序列号获取被吊销X509证书对象。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getRevokedCert](#ZH-CN_TOPIC_0000002522081410__getrevokedcert11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 表示证书序列号。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| X509CrlEntry | 表示被吊销X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    let serialNumber = 1000;
    try {
      let entry = x509Crl.getRevokedCert(serialNumber);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getRevokedCertWithCert(deprecated)

getRevokedCertWithCert(cert : X509Cert) : X509CrlEntry

表示通过指定证书对象获取被吊销X509证书对象。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getRevokedCertWithCert](#ZH-CN_TOPIC_0000002522081410__getrevokedcertwithcert11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | X509Cert | 是 | 表示证书对象。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| X509CrlEntry | 表示被吊销X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIIBjjB4AgEBMA0GCSqGSIb3DQEBCwUAMBIxEDAOBgNVBAMMB1Jvb3QgQ0EXDTI0\n' +
  'MDMxOTAyMDQwN1oXDTI0MDQxODAyMDQwN1owIjAgAgEEFw0yNDAzMTkwMjA0MDZa\n' +
  'MAwwCgYDVR0VBAMKAQGgDjAMMAoGA1UdFAQDAgEAMA0GCSqGSIb3DQEBCwUAA4IB\n' +
  'AQCbjvmHxC8dW6WCS/ga73kx2b7f8I/2eVuDYyReuBiGWeJ9vDmGqimJ9VwOk+ph\n' +
  'LvG/2Zvh9I8qXxnOWeseA2C0bEshJGvXpquIjm00OUyLlK6jdfRbhXT8OyvDjqZs\n' +
  'e1IsMV7Zo11SUc8nR2d0QQ7EVDCN/XFKPsmoK7PhJnRh5gc8W3FKQ6b8H9kdjgTa\n' +
  'KQUap1OIDReVsjPBmRAbwMMLtbrAMllF7E6x7uHgHTGaK1ZPJDtsnCJ45ur3mk/o\n' +
  'HAJFwHNjNDltiEfvMSs76/X0cwitpeW4dFk6c3QtqhxJrHDD4gl8di+xHOyHXpzX\n' +
  '+i2osvdPWRia0dJCL1PCA14k\n' +
  '-----END X509 CRL-----\n';

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
  'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
  'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
  'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
  'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
  'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
  'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
  '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
  '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
  'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
  'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
  'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
  'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
  '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
  'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
  'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
  'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
  'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
  '-----END CERTIFICATE-----\n';

let certEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    // 创建X509证书对象。
    cert.createX509Cert(certEncodingBlob).then((x509Cert) => {
      try {
        let entry = x509Crl.getRevokedCertWithCert(x509Cert);
        console.info('getRevokedCertWithCert result: success.');
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error(`getRevokedCertWithCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
      }
    }).catch((error: BusinessError) => {
      console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
    })
  }
});
```

#### getRevokedCerts(deprecated)

getRevokedCerts(callback : AsyncCallback<Array<X509CrlEntry>>) : void

表示获取被吊销X509证书列表。使用callback异步回调。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getRevokedCerts](#ZH-CN_TOPIC_0000002522081410__getrevokedcerts11)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<X509CrlEntry>> | 是 | 回调函数，表示被吊销X509证书列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    x509Crl.getRevokedCerts((error, array) => {
      if (error) {
        console.error(`getRevokedCerts failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        console.info('getRevokedCerts result: success.');
      }
    });
  }
});
```

#### getRevokedCerts(deprecated)

getRevokedCerts() : Promise<Array<X509CrlEntry>>

表示获取被吊销X509证书列表。使用Promise异步回调。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getRevokedCerts](#ZH-CN_TOPIC_0000002522081410__getrevokedcerts11-1)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**:

| 类型 | 说明 |
| --- | --- |
| Promise<Array<X509CrlEntry>> | 表示被吊销X509证书列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob).then(x509Crl => {
  console.info('createX509Crl result: success.');
  x509Crl.getRevokedCerts().then(array => {
    console.info('getRevokedCerts result: success.');
  }).catch((error: BusinessError) => {
    console.error(`getRevokedCerts failed, errCode: ${error.code}, errMsg: ${error.message}`);
  });
}).catch((error: BusinessError) => {
  console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### getTbsInfo(deprecated)

getTbsInfo() : DataBlob

表示获取证书吊销列表的tbsCertList信息。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getTBSInfo](#ZH-CN_TOPIC_0000002522081410__gettbsinfo11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**:

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示证书吊销列表的tbsCertList信息。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      let tbsInfo = x509Crl.getTbsInfo();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getTbsInfo failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignature(deprecated)

getSignature() : DataBlob

表示获取X509证书吊销列表的签名数据。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getSignature](#ZH-CN_TOPIC_0000002522081410__getsignature11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书吊销列表的签名数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      let signature = x509Crl.getSignature();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignature failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignatureAlgName(deprecated)

getSignatureAlgName() : string

表示获取X509证书吊销列表签名的算法名称。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getSignatureAlgName](#ZH-CN_TOPIC_0000002522081410__getsignaturealgname11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表签名的算法名。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      let sigAlgName = x509Crl.getSignatureAlgName();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignatureAlgName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignatureAlgOid(deprecated)

getSignatureAlgOid() : string

表示获取X509证书吊销列表签名算法的对象标志符OID(Object Identifier)。OID是由国际标准组织(ISO)的名称注册机构分配。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getSignatureAlgOid](#ZH-CN_TOPIC_0000002522081410__getsignaturealgoid11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表签名算法的对象标志符OID。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      let sigAlgOid = x509Crl.getSignatureAlgOid();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignatureAlgOid failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignatureAlgParams(deprecated)

getSignatureAlgParams() : DataBlob

表示获取X509证书吊销列表签名的算法参数。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRL.getSignatureAlgParams](#ZH-CN_TOPIC_0000002522081410__getsignaturealgparams11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书吊销列表签名的算法参数。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      let sigAlgParams = x509Crl.getSignatureAlgParams();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignatureAlgParams failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### X509CRL11+

被吊销证书列表对象。

#### isRevoked11+

isRevoked(cert : X509Cert) : boolean

表示检查证书是否吊销。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | X509Cert | 是 | 表示被检查的证书对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 表示证书吊销状态，true表示已吊销，false表示未吊销。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
  'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
  'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
  'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
  'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
  '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
  'BetUokslUfjT6+s/X4ByaxycAA==\n' +
  '-----END CERTIFICATE-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

let certEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    // Create an X509Cert instance.
    cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
      if (error) {
        console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        try {
          let revokedFlag = x509CRL.isRevoked(x509Cert);
        } catch (error) {
          let e: BusinessError = error as BusinessError;
          console.error(`isRevoked failed, errCode: ${e.code}, errMsg: ${e.message}`);
      }
    });
  }
});
```

#### getType11+

getType() : string

表示获取证书吊销列表类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示证书吊销列表类型。 |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    let type = x509CRL.getType();
  }
});
```

#### getEncoded11+

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取X509证书吊销列表的序列化数据。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<EncodingBlob> | 是 | 回调函数，表示X509证书吊销列表的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    x509CRL.getEncoded((error, data) => {
      if (error) {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        console.info('getEncoded result: success.');
      }
    });
  }
});
```

#### getEncoded11+

getEncoded() : Promise<EncodingBlob>

表示获取X509证书吊销列表的序列化数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<EncodingBlob> | 表示X509证书吊销列表的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob).then(x509CRL => {
  console.info('createX509CRL result: success.');
  x509CRL.getEncoded().then(result => {
    console.info('getEncoded result: success.');
  }).catch((error: BusinessError) => {
    console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
  });
}).catch((error: BusinessError) => {
  console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### verify11+

verify(key : cryptoFramework.PubKey, callback : AsyncCallback<void>) : void

表示对X509证书吊销列表进行验签。使用callback异步回调。验签支持RSA算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | 是 | 表示用于验签的公钥对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数,使用AsyncCallback的第一个error参数判断是否验签成功，error为null表示成功，error不为null表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let pubKeyData = new Uint8Array([
  0x30, 0x81, 0x9F, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01,
  0x05, 0x00, 0x03, 0x81, 0x8D, 0x00, 0x30, 0x81, 0x89, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D,
  0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED, 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE,
  0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67, 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C,
  0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20, 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66,
  0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4, 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0,
  0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23, 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C,
  0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22, 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65,
  0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14, 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA,
  0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91, 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01,
  0x00, 0x01
]);

let priKeyData = new Uint8Array([
  0x30, 0x82, 0x02, 0x77, 0x02, 0x01, 0x00, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
  0x0D, 0x01, 0x01, 0x01, 0x05, 0x00, 0x04, 0x82, 0x02, 0x61, 0x30, 0x82, 0x02, 0x5D, 0x02, 0x01,
  0x00, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D, 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED,
  0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE, 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67,
  0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C, 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20,
  0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66, 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4,
  0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0, 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23,
  0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C, 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22,
  0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65, 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14,
  0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA, 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91,
  0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01, 0x00, 0x01, 0x02, 0x81, 0x80, 0x5A, 0xCF, 0x0F,
  0xF5, 0xA6, 0x1C, 0x19, 0x65, 0x8C, 0x94, 0x40, 0xF6, 0x84, 0x28, 0x74, 0x40, 0x42, 0x34, 0xDE,
  0xC3, 0x00, 0x5E, 0x72, 0x4D, 0x96, 0xE9, 0x4C, 0xBD, 0xC9, 0xDB, 0x14, 0x9F, 0xD5, 0xBB, 0xA9,
  0x0C, 0x20, 0xC2, 0xBE, 0x7A, 0x80, 0x89, 0xEC, 0x99, 0x04, 0xF0, 0xEE, 0x7B, 0x83, 0x20, 0x1D,
  0x37, 0x19, 0x55, 0x85, 0xF6, 0x8E, 0x3B, 0xFB, 0x16, 0xF3, 0xD3, 0x6F, 0xEE, 0x73, 0x12, 0x53,
  0xCA, 0x77, 0xD7, 0x6C, 0x29, 0xF5, 0x08, 0xA3, 0x09, 0x01, 0x0B, 0x00, 0x05, 0x57, 0xAD, 0x4D,
  0xF0, 0x92, 0xB2, 0x5A, 0x8B, 0x19, 0x09, 0x81, 0x86, 0xFE, 0x66, 0xB9, 0x33, 0x88, 0x28, 0xF3,
  0x37, 0x73, 0x09, 0x5F, 0xD7, 0xC9, 0xC6, 0xFA, 0x13, 0x74, 0xFE, 0xAE, 0x53, 0xA9, 0x71, 0x67,
  0xCE, 0x3A, 0xE6, 0x8D, 0x35, 0xD1, 0xB8, 0xFD, 0x6F, 0x0D, 0x43, 0xC2, 0xD1, 0x02, 0x41, 0x00,
  0xF7, 0x33, 0xE5, 0x6C, 0x29, 0x5A, 0x30, 0x58, 0xA4, 0x52, 0x65, 0xA0, 0x39, 0xC2, 0xE8, 0xAE,
  0x5F, 0xA3, 0x2D, 0x0C, 0x65, 0xB1, 0x7B, 0xFD, 0x92, 0xBF, 0x47, 0x87, 0x97, 0x40, 0xCB, 0x54,
  0xF9, 0xBB, 0x50, 0x27, 0x70, 0x51, 0xD0, 0xD8, 0x48, 0x0D, 0xC6, 0x47, 0x60, 0xF8, 0x4E, 0x0A,
  0x32, 0x76, 0x6D, 0xA4, 0xBA, 0x40, 0xE5, 0x58, 0xF8, 0x4A, 0x39, 0x4E, 0xF8, 0x3F, 0x4E, 0x2D,
  0x02, 0x41, 0x00, 0xE4, 0x23, 0x2A, 0x5F, 0x59, 0xCF, 0x7C, 0x91, 0x24, 0x0D, 0xA2, 0x44, 0x17,
  0xCD, 0x37, 0xDE, 0x1F, 0x53, 0x4D, 0x33, 0x9F, 0x90, 0x4D, 0xD9, 0x72, 0x64, 0x25, 0xBA, 0xAB,
  0x47, 0x91, 0xC4, 0x99, 0x95, 0x86, 0xB5, 0x8A, 0xEA, 0x77, 0xF7, 0x64, 0x72, 0x5E, 0xB7, 0xBB,
  0x16, 0xA1, 0x64, 0xA4, 0xE1, 0x2D, 0x76, 0x6D, 0xEF, 0xB1, 0x5E, 0xD6, 0x17, 0xE8, 0xAA, 0xB6,
  0xA0, 0xD9, 0x85, 0x02, 0x41, 0x00, 0xDF, 0xC8, 0x5B, 0x28, 0x4F, 0x47, 0x15, 0xFD, 0x28, 0xC4,
  0x6E, 0xBB, 0x5D, 0x8E, 0xD4, 0x95, 0x06, 0x7E, 0xF1, 0x89, 0x07, 0x86, 0x64, 0x78, 0x69, 0x20,
  0x3F, 0xE0, 0xBF, 0x4C, 0x28, 0xC6, 0x04, 0x4D, 0x4D, 0x82, 0x66, 0x6B, 0xAA, 0x64, 0x20, 0xD6,
  0x57, 0x68, 0xC6, 0xA0, 0x02, 0x05, 0xB9, 0x28, 0xFC, 0x98, 0xE3, 0x03, 0x5C, 0x9B, 0xEE, 0x29,
  0x43, 0x37, 0xFA, 0x03, 0x55, 0x01, 0x02, 0x40, 0x69, 0x5B, 0x7C, 0x24, 0x10, 0xDB, 0xEB, 0x91,
  0x33, 0xEF, 0x3F, 0xF2, 0xE6, 0x73, 0x15, 0xCB, 0xF4, 0xF7, 0x89, 0x7D, 0xBF, 0xC0, 0xEA, 0xD2,
  0xF3, 0x2B, 0x20, 0xE9, 0x76, 0x54, 0x55, 0x13, 0x50, 0x42, 0x67, 0xB5, 0xCB, 0x73, 0xC0, 0xF7,
  0x75, 0x62, 0x04, 0x30, 0x21, 0xAC, 0xAF, 0xD8, 0x44, 0xF4, 0xE1, 0x04, 0x02, 0x7D, 0x61, 0x92,
  0x84, 0x99, 0x02, 0x10, 0x64, 0xCB, 0x1F, 0xE9, 0x02, 0x41, 0x00, 0xAB, 0x4B, 0x7D, 0x90, 0x7C,
  0x57, 0x08, 0x6B, 0xC0, 0x43, 0x72, 0x09, 0x8A, 0x18, 0x35, 0x36, 0x64, 0x9D, 0x84, 0x8D, 0xF1,
  0x84, 0x94, 0x48, 0xC6, 0x80, 0x9D, 0xB9, 0xA2, 0x58, 0x0A, 0x4D, 0x0A, 0xCA, 0x1E, 0xD6, 0x05,
  0x55, 0x5B, 0xFE, 0xD7, 0xAA, 0x70, 0xED, 0x76, 0xB3, 0x40, 0x2E, 0xA0, 0xB3, 0x32, 0x37, 0xB0,
  0xA0, 0xB9, 0x96, 0x2D, 0xC4, 0x70, 0xE9, 0x99, 0x10, 0x67, 0x8D
]);

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    try {
      // Generate the public key by AsyKeyGenerator.
      let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
      console.info('createAsyKeyGenerator result: success.');
      let priEncodingBlob: cryptoFramework.DataBlob = {
        data: priKeyData,
      };
      let pubEncodingBlob: cryptoFramework.DataBlob = {
        data: pubKeyData,
      };
      keyGenerator.convertKey(pubEncodingBlob, priEncodingBlob, (e, keyPair) => {
        if (e) {
          console.error(`convert key failed, errCode: ${e.code}, errMsg: ${e.message}`);
        } else {
          console.info('convert key result: success.');
          x509CRL.verify(keyPair.pubKey, (err, data) => {
            if (err) {
              console.error(`verify failed, errCode: ${err.code}, errMsg: ${err.message}`);
            } else {
              console.info('verify result: success.');
            }
          });
        }
      })
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### verify11+

verify(key : cryptoFramework.PubKey) : Promise<void>

表示对X509证书吊销列表进行验签。使用Promise异步回调。验签支持RSA算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | 是 | 表示用于验签的公钥对象。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit'
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let pubKeyData = new Uint8Array([
  0x30, 0x81, 0x9F, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01,
  0x05, 0x00, 0x03, 0x81, 0x8D, 0x00, 0x30, 0x81, 0x89, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D,
  0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED, 0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE,
  0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67, 0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C,
  0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20, 0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66,
  0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4, 0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0,
  0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23, 0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C,
  0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22, 0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65,
  0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14, 0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA,
  0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91, 0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01,
  0x00, 0x01
]);

let priKeyData = new Uint8Array([
  0x30, 0x82, 0x02, 0x77, 0x02, 0x01, 0x00, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
  0x0D, 0x01, 0x01, 0x01, 0x05, 0x00, 0x04, 0x82, 0x02, 0x61, 0x30, 0x82, 0x02, 0x5D, 0x02, 0x01,
  0x00, 0x02, 0x81, 0x81, 0x00, 0xDC, 0x4C, 0x2D, 0x57, 0x49, 0x3D, 0x42, 0x52, 0x1A, 0x09, 0xED,
  0x3E, 0x90, 0x29, 0x51, 0xF7, 0x70, 0x15, 0xFE, 0x76, 0xB0, 0xDB, 0xDF, 0xA1, 0x2C, 0x6C, 0x67,
  0x95, 0xDA, 0x63, 0x3D, 0x4F, 0x71, 0x48, 0x8C, 0x3E, 0xFA, 0x24, 0x79, 0xE9, 0xF2, 0xF2, 0x20,
  0xCB, 0xF1, 0x59, 0x6B, 0xED, 0xC8, 0x72, 0x66, 0x6E, 0x31, 0xD4, 0xF3, 0xCE, 0x0B, 0x12, 0xC4,
  0x17, 0x39, 0xB4, 0x52, 0x16, 0xD3, 0xE3, 0xC0, 0xF8, 0x48, 0xB3, 0xF6, 0x40, 0xD5, 0x47, 0x23,
  0x30, 0x7F, 0xA7, 0xC5, 0x5A, 0x5A, 0xBB, 0x5C, 0x7B, 0xEF, 0x69, 0xE2, 0x74, 0x35, 0x24, 0x22,
  0x25, 0x45, 0x7E, 0xFC, 0xE8, 0xC4, 0x52, 0x65, 0xA0, 0x4E, 0xBC, 0xFD, 0x3F, 0xD9, 0x85, 0x14,
  0x8A, 0x5A, 0x93, 0x02, 0x24, 0x6C, 0x19, 0xBA, 0x81, 0xBE, 0x65, 0x2E, 0xCB, 0xBB, 0xE9, 0x91,
  0x7B, 0x7C, 0x47, 0xC2, 0x61, 0x02, 0x03, 0x01, 0x00, 0x01, 0x02, 0x81, 0x80, 0x5A, 0xCF, 0x0F,
  0xF5, 0xA6, 0x1C, 0x19, 0x65, 0x8C, 0x94, 0x40, 0xF6, 0x84, 0x28, 0x74, 0x40, 0x42, 0x34, 0xDE,
  0xC3, 0x00, 0x5E, 0x72, 0x4D, 0x96, 0xE9, 0x4C, 0xBD, 0xC9, 0xDB, 0x14, 0x9F, 0xD5, 0xBB, 0xA9,
  0x0C, 0x20, 0xC2, 0xBE, 0x7A, 0x80, 0x89, 0xEC, 0x99, 0x04, 0xF0, 0xEE, 0x7B, 0x83, 0x20, 0x1D,
  0x37, 0x19, 0x55, 0x85, 0xF6, 0x8E, 0x3B, 0xFB, 0x16, 0xF3, 0xD3, 0x6F, 0xEE, 0x73, 0x12, 0x53,
  0xCA, 0x77, 0xD7, 0x6C, 0x29, 0xF5, 0x08, 0xA3, 0x09, 0x01, 0x0B, 0x00, 0x05, 0x57, 0xAD, 0x4D,
  0xF0, 0x92, 0xB2, 0x5A, 0x8B, 0x19, 0x09, 0x81, 0x86, 0xFE, 0x66, 0xB9, 0x33, 0x88, 0x28, 0xF3,
  0x37, 0x73, 0x09, 0x5F, 0xD7, 0xC9, 0xC6, 0xFA, 0x13, 0x74, 0xFE, 0xAE, 0x53, 0xA9, 0x71, 0x67,
  0xCE, 0x3A, 0xE6, 0x8D, 0x35, 0xD1, 0xB8, 0xFD, 0x6F, 0x0D, 0x43, 0xC2, 0xD1, 0x02, 0x41, 0x00,
  0xF7, 0x33, 0xE5, 0x6C, 0x29, 0x5A, 0x30, 0x58, 0xA4, 0x52, 0x65, 0xA0, 0x39, 0xC2, 0xE8, 0xAE,
  0x5F, 0xA3, 0x2D, 0x0C, 0x65, 0xB1, 0x7B, 0xFD, 0x92, 0xBF, 0x47, 0x87, 0x97, 0x40, 0xCB, 0x54,
  0xF9, 0xBB, 0x50, 0x27, 0x70, 0x51, 0xD0, 0xD8, 0x48, 0x0D, 0xC6, 0x47, 0x60, 0xF8, 0x4E, 0x0A,
  0x32, 0x76, 0x6D, 0xA4, 0xBA, 0x40, 0xE5, 0x58, 0xF8, 0x4A, 0x39, 0x4E, 0xF8, 0x3F, 0x4E, 0x2D,
  0x02, 0x41, 0x00, 0xE4, 0x23, 0x2A, 0x5F, 0x59, 0xCF, 0x7C, 0x91, 0x24, 0x0D, 0xA2, 0x44, 0x17,
  0xCD, 0x37, 0xDE, 0x1F, 0x53, 0x4D, 0x33, 0x9F, 0x90, 0x4D, 0xD9, 0x72, 0x64, 0x25, 0xBA, 0xAB,
  0x47, 0x91, 0xC4, 0x99, 0x95, 0x86, 0xB5, 0x8A, 0xEA, 0x77, 0xF7, 0x64, 0x72, 0x5E, 0xB7, 0xBB,
  0x16, 0xA1, 0x64, 0xA4, 0xE1, 0x2D, 0x76, 0x6D, 0xEF, 0xB1, 0x5E, 0xD6, 0x17, 0xE8, 0xAA, 0xB6,
  0xA0, 0xD9, 0x85, 0x02, 0x41, 0x00, 0xDF, 0xC8, 0x5B, 0x28, 0x4F, 0x47, 0x15, 0xFD, 0x28, 0xC4,
  0x6E, 0xBB, 0x5D, 0x8E, 0xD4, 0x95, 0x06, 0x7E, 0xF1, 0x89, 0x07, 0x86, 0x64, 0x78, 0x69, 0x20,
  0x3F, 0xE0, 0xBF, 0x4C, 0x28, 0xC6, 0x04, 0x4D, 0x4D, 0x82, 0x66, 0x6B, 0xAA, 0x64, 0x20, 0xD6,
  0x57, 0x68, 0xC6, 0xA0, 0x02, 0x05, 0xB9, 0x28, 0xFC, 0x98, 0xE3, 0x03, 0x5C, 0x9B, 0xEE, 0x29,
  0x43, 0x37, 0xFA, 0x03, 0x55, 0x01, 0x02, 0x40, 0x69, 0x5B, 0x7C, 0x24, 0x10, 0xDB, 0xEB, 0x91,
  0x33, 0xEF, 0x3F, 0xF2, 0xE6, 0x73, 0x15, 0xCB, 0xF4, 0xF7, 0x89, 0x7D, 0xBF, 0xC0, 0xEA, 0xD2,
  0xF3, 0x2B, 0x20, 0xE9, 0x76, 0x54, 0x55, 0x13, 0x50, 0x42, 0x67, 0xB5, 0xCB, 0x73, 0xC0, 0xF7,
  0x75, 0x62, 0x04, 0x30, 0x21, 0xAC, 0xAF, 0xD8, 0x44, 0xF4, 0xE1, 0x04, 0x02, 0x7D, 0x61, 0x92,
  0x84, 0x99, 0x02, 0x10, 0x64, 0xCB, 0x1F, 0xE9, 0x02, 0x41, 0x00, 0xAB, 0x4B, 0x7D, 0x90, 0x7C,
  0x57, 0x08, 0x6B, 0xC0, 0x43, 0x72, 0x09, 0x8A, 0x18, 0x35, 0x36, 0x64, 0x9D, 0x84, 0x8D, 0xF1,
  0x84, 0x94, 0x48, 0xC6, 0x80, 0x9D, 0xB9, 0xA2, 0x58, 0x0A, 0x4D, 0x0A, 0xCA, 0x1E, 0xD6, 0x05,
  0x55, 0x5B, 0xFE, 0xD7, 0xAA, 0x70, 0xED, 0x76, 0xB3, 0x40, 0x2E, 0xA0, 0xB3, 0x32, 0x37, 0xB0,
  0xA0, 0xB9, 0x96, 0x2D, 0xC4, 0x70, 0xE9, 0x99, 0x10, 0x67, 0x8D
]);

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob).then(x509CRL => {
  console.info('createX509Crl result: success.');

  try {
    // 生成公钥对象。
    let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
    console.info('createAsyKeyGenerator result: success.');
    let priEncodingBlob: cryptoFramework.DataBlob = {
      data: priKeyData,
    };
    let pubEncodingBlob: cryptoFramework.DataBlob = {
      data: pubKeyData,
    };
    keyGenerator.convertKey(pubEncodingBlob, priEncodingBlob).then((keyPair) => {
      console.info('convert key result: success.');
      x509CRL.verify(keyPair.pubKey).then(result => {
        console.info('verify result: success.');
      }).catch((error: BusinessError) => {
        console.error(`verify failed, errCode: ${error.code}, errMsg: ${error.message}`);
      });
    }).catch((error: BusinessError) => {
      console.error(`convert key failed, errCode: ${error.code}, errMsg: ${error.message}`);
    });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}).catch((error: BusinessError) => {
  console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### getVersion11+

getVersion() : number

表示获取X509证书吊销列表的版本号。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示获取X509证书吊销列表的版本号。 |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    let version = x509CRL.getVersion();
  }
});
```

#### getIssuerName11+

getIssuerName() : DataBlob

表示获取X509证书吊销列表颁发者名称。

获取到的X509证书吊销列表颁发者名称数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书吊销列表颁发者名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let issuerName = x509CRL.getIssuerName();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getIssuerName20+

getIssuerName(encodingType: EncodingType): string

根据编码类型获取X509证书吊销列表颁发者名称。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | EncodingType | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表颁发者名称，使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The value of encodingType is not in the EncodingType enumeration range. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIIByzCBtAIBATANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJDTjEPMA0GA1UE\n' +
  'CAwG6ZmV6KW/MQ8wDQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMG\n' +
  'A1UEAwwM5Lit5paH5rWL6K+VFw0yNDEwMTYwODUwMDlaFw0yNDExMTUwODUwMDla\n' +
  'MBkwFwIGAXKnJjrAFw0yNDEwMTYwODQ5NDBaoA4wDDAKBgNVHRQEAwIBADANBgkq\n' +
  'hkiG9w0BAQsFAAOCAQEAU0JPK/DnGmjCi5lKyun506JE+FVDuQsEWuF5CZPqE2um\n' +
  'hA04Qffi+8AfwLpG2KPBaAYTteU4fx30y8Wm0kLutalk32FgrbQX0VQ7EaCOmkMU\n' +
  '2dnQMmFmaFiVcOTaRzgqDOYKuzSAptCo6hqtk9kgjbda5HnsNiVC7dNMRp1Jlzwr\n' +
  'k/42mqZ3fFIy3wYLaxRlq368BX3u94J9Cx754V2V/XEApiRI/FsiSRzRX+jfUBa4\n' +
  '+wwu3WhWxisQj6z3bBkQD4RTg3S+ic8hhP44wt/1MmSLG946Dc9uVYJKUVZqTco9\n' +
  'QDoDwYfBJBzcXjManSkPsGCb7RfTAr5HqcEtIHsK+w==\n' +
  '-----END X509 CRL-----\n';
// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let issuerName = x509CRL.getIssuerName(cert.EncodingType.ENCODING_UTF8);
      console.info('issuerName output = ' + issuerName);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getIssuerName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getLastUpdate11+

getLastUpdate() : string

表示获取X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let lastUpdate  = x509CRL.getLastUpdate();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getLastUpdate failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getNextUpdate11+

getNextUpdate() : string

表示获取证书吊销列表下一次更新的日期，日期为ASN.1时间格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表下一次更新的日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let nextUpdate = x509CRL.getNextUpdate();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getNextUpdate failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getRevokedCert11+

getRevokedCert(serialNumber : bigint) : X509CRLEntry

表示通过指定证书序列号获取被吊销X509证书对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | bigint | 是 | 表示证书序列号。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| X509CRLEntry | 表示被吊销X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    let serialNumber = BigInt(1000);
    try {
      let entry = x509CRL.getRevokedCert(serialNumber);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getRevokedCertWithCert11+

getRevokedCertWithCert(cert : X509Cert) : X509CRLEntry

表示通过指定证书对象获取被吊销X509证书对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | X509Cert | 是 | 表示证书对象。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| X509CRLEntry | 表示被吊销X509证书对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIIBjjB4AgEBMA0GCSqGSIb3DQEBCwUAMBIxEDAOBgNVBAMMB1Jvb3QgQ0EXDTI0\n' +
  'MDMxOTAyMDQwN1oXDTI0MDQxODAyMDQwN1owIjAgAgEEFw0yNDAzMTkwMjA0MDZa\n' +
  'MAwwCgYDVR0VBAMKAQGgDjAMMAoGA1UdFAQDAgEAMA0GCSqGSIb3DQEBCwUAA4IB\n' +
  'AQCbjvmHxC8dW6WCS/ga73kx2b7f8I/2eVuDYyReuBiGWeJ9vDmGqimJ9VwOk+ph\n' +
  'LvG/2Zvh9I8qXxnOWeseA2C0bEshJGvXpquIjm00OUyLlK6jdfRbhXT8OyvDjqZs\n' +
  'e1IsMV7Zo11SUc8nR2d0QQ7EVDCN/XFKPsmoK7PhJnRh5gc8W3FKQ6b8H9kdjgTa\n' +
  'KQUap1OIDReVsjPBmRAbwMMLtbrAMllF7E6x7uHgHTGaK1ZPJDtsnCJ45ur3mk/o\n' +
  'HAJFwHNjNDltiEfvMSs76/X0cwitpeW4dFk6c3QtqhxJrHDD4gl8di+xHOyHXpzX\n' +
  '+i2osvdPWRia0dJCL1PCA14k\n' +
  '-----END X509 CRL-----\n';

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
  'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
  'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
  'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
  'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
  'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
  'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
  '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
  '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
  'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
  'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
  'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
  'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
  '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
  'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
  'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
  'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
  'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
  '-----END CERTIFICATE-----\n';

let certEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    // 创建X509证书对象。
    cert.createX509Cert(certEncodingBlob).then((x509Cert) => {
      try {
        let entry = x509CRL.getRevokedCertWithCert(x509Cert);
        console.info('getRevokedCertWithCert result: success.');
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error(`getRevokedCertWithCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
      }
    }).catch((error: BusinessError) => {
      console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
    })
  }
});
```

#### getRevokedCerts11+

getRevokedCerts(callback : AsyncCallback<Array<X509CRLEntry>>) : void

表示获取被吊销X509证书列表。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<X509CRLEntry>> | 是 | 回调函数，表示被吊销X509证书列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    x509CRL.getRevokedCerts((error, array) => {
      if (error) {
        console.error(`getRevokedCerts failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        console.info('getRevokedCerts result: success.');
      }
    });
  }
});
```

#### getRevokedCerts11+

getRevokedCerts() : Promise<Array<X509CRLEntry>>

表示获取被吊销X509证书列表。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**:

| 类型 | 说明 |
| --- | --- |
| Promise<Array<X509CRLEntry>> | 表示被吊销X509证书列表。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob).then(x509CRL => {
  console.info('createX509CRL result: success.');
  x509CRL.getRevokedCerts().then(array => {
    console.info('getRevokedCerts result: success.');
  }).catch((error: BusinessError) => {
    console.error(`getRevokedCerts failed, errCode: ${error.code}, errMsg: ${error.message}`);
  });
}).catch((error: BusinessError) => {
  console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### getSignature11+

getSignature() : DataBlob

表示获取X509证书吊销列表的签名数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书吊销列表的签名数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let signature = x509CRL.getSignature();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignature failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignatureAlgName11+

getSignatureAlgName() : string

表示获取X509证书吊销列表签名的算法名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表签名的算法名。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let sigAlgName = x509CRL.getSignatureAlgName();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignatureAlgName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignatureAlgOid11+

getSignatureAlgOid() : string

表示获取X509证书吊销列表签名算法的对象标志符OID(Object Identifier)。OID是由国际标准组织(ISO)的名称注册机构分配。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示X509证书吊销列表签名算法的对象标志符OID。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let sigAlgOid = x509CRL.getSignatureAlgOid();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignatureAlgOid failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getSignatureAlgParams11+

getSignatureAlgParams() : DataBlob

表示获取X509证书吊销列表签名的算法参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509证书吊销列表签名的算法参数。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let sigAlgParams = x509CRL.getSignatureAlgParams();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getSignatureAlgParams failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getTBSInfo11+

getTBSInfo() : DataBlob

表示获取证书吊销列表的tbsCertList信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**:

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示证书吊销列表的tbsCertList信息。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let tbsInfo = x509CRL.getTBSInfo();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getTBSInfo failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### getExtensions11+

getExtensions(): DataBlob

表示获取CRL的扩展。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509CRL扩展用途。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIIBjjB4AgEBMA0GCSqGSIb3DQEBCwUAMBIxEDAOBgNVBAMMB1Jvb3QgQ0EXDTI0\n' +
  'MDMxOTAyMDQwN1oXDTI0MDQxODAyMDQwN1owIjAgAgEEFw0yNDAzMTkwMjA0MDZa\n' +
  'MAwwCgYDVR0VBAMKAQGgDjAMMAoGA1UdFAQDAgEAMA0GCSqGSIb3DQEBCwUAA4IB\n' +
  'AQCbjvmHxC8dW6WCS/ga73kx2b7f8I/2eVuDYyReuBiGWeJ9vDmGqimJ9VwOk+ph\n' +
  'LvG/2Zvh9I8qXxnOWeseA2C0bEshJGvXpquIjm00OUyLlK6jdfRbhXT8OyvDjqZs\n' +
  'e1IsMV7Zo11SUc8nR2d0QQ7EVDCN/XFKPsmoK7PhJnRh5gc8W3FKQ6b8H9kdjgTa\n' +
  'KQUap1OIDReVsjPBmRAbwMMLtbrAMllF7E6x7uHgHTGaK1ZPJDtsnCJ45ur3mk/o\n' +
  'HAJFwHNjNDltiEfvMSs76/X0cwitpeW4dFk6c3QtqhxJrHDD4gl8di+xHOyHXpzX\n' +
  '+i2osvdPWRia0dJCL1PCA14k\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    try {
      let extensions = x509CRL.getExtensions();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getExtensions failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### match11+

match(param: X509CRLMatchParameters): boolean

判断证书吊销列表是否与输入参数匹配。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | X509CRLMatchParameters | 是 | 表示需要匹配的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 当参数匹配时，该方法返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let crlEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

const certData = '-----BEGIN CERTIFICATE-----\r\n' +
  'MIIC8TCCAdmgAwIBAgIIFB75m06RTHwwDQYJKoZIhvcNAQELBQAwWDELMAkGA1UE\r\n' +
  'BhMCQ04xEDAOBgNVBAgTB0ppYW5nc3UxEDAOBgNVBAcTB05hbmppbmcxCzAJBgNV\r\n' +
  'BAoTAnRzMQswCQYDVQQLEwJ0czELMAkGA1UEAxMCdHMwHhcNMjMxMTIzMDMzMjAw\r\n' +
  'WhcNMjQxMTIzMDMzMjAwWjBhMQswCQYDVQQGEwJDTjEQMA4GA1UECBMHSmlhbmdz\r\n' +
  'dTEQMA4GA1UEBxMHTmFuamluZzEMMAoGA1UEChMDdHMxMQwwCgYDVQQLEwN0czEx\r\n' +
  'EjAQBgNVBAMTCTEyNy4wLjAuMTAqMAUGAytlcAMhALsWnY9cMNC6jzduM69vI3Ej\r\n' +
  'pUlgHtEHS8kRfmYBupJSo4GvMIGsMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNSg\r\n' +
  'poQvfxR8A1Y4St8NjOHkRpm4MAsGA1UdDwQEAwID+DAnBgNVHSUEIDAeBggrBgEF\r\n' +
  'BQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEyNy4wLjAuMTAR\r\n' +
  'BglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0\r\n' +
  'ZTANBgkqhkiG9w0BAQsFAAOCAQEAfnLmPF6BtAUCZ9pjt1ITdXc5M4LJfMw5IPcv\r\n' +
  'fUAvhdaUXtqBQcjGCWtDdhyb1n5Xp+N7oKz/Cnn0NGFTwVArtFiQ5NEP2CmrckLh\r\n' +
  'Da4VnsDFU+zx2Bbfwo5Ms7iArxyx0fArbMZzN9D1lZcVjiIxp1+3k1/0sdCemcY/\r\n' +
  'y7mw5NwkcczLWLBZl1/Ho8b4dlo1wTA7TZk9uu8UwYBwXDrQe6S9rMcvMcRKiJ9e\r\n' +
  'V4SYZIO7ihr8+n4LQDQP+spvX4cf925a3kyZrftfvGCJ2ZNwvsPhyumYhaBqAgSy\r\n' +
  'Up2BImymAqPi157q9EeYcQz170TtDZHGmjYzdQxhOAHRb6/IdQ==\r\n' +
  '-----END CERTIFICATE-----\r\n';
const certEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  encodingFormat: cert.EncodingFormat.FORMAT_PEM,
};

async function crlMatch() {
  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(certEncodingBlob);
    console.info('createX509Cert result: success.');
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }

  cert.createX509CRL(crlEncodingBlob, (error, x509CRL) => {
    if (error) {
      console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
    } else {
      console.info('createX509CRL result: success.');
      try {
        const param: cert.X509CRLMatchParameters = {
          issuer: [new Uint8Array([0x30, 0x58, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x43,
            0x4E, 0x31, 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x4A, 0x69, 0x61, 0x6E, 0x67, 0x73,
            0x75, 0x31, 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x07, 0x4E, 0x61, 0x6E, 0x6A, 0x69, 0x6E,
            0x67, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x0A, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09,
            0x06, 0x03, 0x55, 0x04, 0x0B, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x03,
            0x13, 0x02, 0x74, 0x73])],
          x509Cert: x509Cert
        }
        const result = x509CRL.match(param);
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error(`x509CRL match failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  });
}
```

#### getIssuerX500DistinguishedName12+

getIssuerX500DistinguishedName(): X500DistinguishedName

获取颁发者的X509可分辨名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| X500DistinguishedName | X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let crlEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function crlGetIssuerX500DistinguishedName() {
  let x509Crl: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509Crl = await cert.createX509CRL(crlEncodingBlob);
    console.info('createX509CRL result: success.');
    let name = x509Crl.getIssuerX500DistinguishedName();
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### toString12+

toString(): string

获取对象的字符串类型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let crlEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function crlToString() {
  let x509Crl: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509Crl = await cert.createX509CRL(crlEncodingBlob);
    console.info('createX509CRL result: success.');
    console.info('crlToString success: ' + x509Crl.toString());
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### toString20+

toString(encodingType: EncodingType): string

根据编码类型获取对象的字符串类型数据。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | EncodingType | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The value of encodingType is not in the EncodingType enumeration range. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIIByzCBtAIBATANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJDTjEPMA0GA1UE\n' +
  'CAwG6ZmV6KW/MQ8wDQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMG\n' +
  'A1UEAwwM5Lit5paH5rWL6K+VFw0yNDEwMTYwODUwMDlaFw0yNDExMTUwODUwMDla\n' +
  'MBkwFwIGAXKnJjrAFw0yNDEwMTYwODQ5NDBaoA4wDDAKBgNVHRQEAwIBADANBgkq\n' +
  'hkiG9w0BAQsFAAOCAQEAU0JPK/DnGmjCi5lKyun506JE+FVDuQsEWuF5CZPqE2um\n' +
  'hA04Qffi+8AfwLpG2KPBaAYTteU4fx30y8Wm0kLutalk32FgrbQX0VQ7EaCOmkMU\n' +
  '2dnQMmFmaFiVcOTaRzgqDOYKuzSAptCo6hqtk9kgjbda5HnsNiVC7dNMRp1Jlzwr\n' +
  'k/42mqZ3fFIy3wYLaxRlq368BX3u94J9Cx754V2V/XEApiRI/FsiSRzRX+jfUBa4\n' +
  '+wwu3WhWxisQj6z3bBkQD4RTg3S+ic8hhP44wt/1MmSLG946Dc9uVYJKUVZqTco9\n' +
  'QDoDwYfBJBzcXjManSkPsGCb7RfTAr5HqcEtIHsK+w==\n' +
  '-----END X509 CRL-----\n';
// 证书吊销列表二进制数据，需业务自行赋值。
let crlEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function crlToString() {
  let x509Crl: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509Crl = await cert.createX509CRL(crlEncodingBlob);
    console.info('createX509CRL result: success.');
    console.info('crlToString success: ' + x509Crl.toString(cert.EncodingType.ENCODING_UTF8));
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### hashCode12+

hashCode(): Uint8Array

获取DER格式数据的哈希值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | DER格式数据的哈希值。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let crlEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function crlHashCode() {
  let x509Crl: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509Crl = await cert.createX509CRL(crlEncodingBlob);
    console.info('createX509CRL result: success.');
    console.info('crlHashCode success: ' + x509Crl.hashCode());
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getExtensionsObject12+

getExtensionsObject(): CertExtension

获取对应实体的扩展域DER格式数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| CertExtension | 证书扩展域段类对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
    'MIIB6DCB0QIBATANBgkqhkiG9w0BAQsFADCBjjELMAkGA1UEBhMCUlUxFTATBgNV\n' +
    'BAgMDNCc0L7RgdC60LLQsDELMAkGA1UECgwC0K8xCzAJBgNVBAsMAtCvMSowKAYD\n' +
    'VQQDDCHQlNC80LjRgtGA0LjQuSDQkdC10LvRj9Cy0YHQutC40LkxIjAgBgkqhkiG\n' +
    '9w0BCQEWE2JlbGRtaXRAZXhhbXBsZS5jb20XDTE3MDQyNDEzMjUzMVoXDTE3MDUy\n' +
    'NDEzMjUzMVqgDjAMMAoGA1UdFAQDAgEBMA0GCSqGSIb3DQEBCwUAA4IBAQCF5eX+\n' +
    '1BM/BxoHU2/3pQHJgPSKevN0/K/daiFHiJl7Kb9GCwKY14B1RvbN2rUP/58Mt+aq\n' +
    'jvauf1yBzlaJQeJKZcsCmG9p6Tr1y0BJXhrq5kC0SLyNDsfGUTfuxnwmo+clHXRU\n' +
    '+gKuk+h0WkJL022ZYbJ38w588k4NT3CWVHeE23EDC264p942mlDE7en6MyL152Pe\n' +
    'Ld9YrWiq5iOIOrIbQLErq0EjwxvHG9sMiYFUa6VrwmRf26nyZ7u9RKJDP+o2dltw\n' +
    'diBaSXC3Qt3pZ8BIfv/l81lwp8Dr63SwCII2pIRplyICdQqmX/a+1q8kThXIP2Kx\n' +
    '+X48g7VE2o2X4cfy\n' +
    '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let crlEncodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function crlHashCode() {
  let x509Crl: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509Crl = await cert.createX509CRL(crlEncodingBlob);
    console.info('createX509CRL result: success.');
    let object = x509Crl.getExtensionsObject();
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cert.createCertChainValidator

createCertChainValidator(algorithm :string) : CertChainValidator

表示创建证书链校验器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algorithm | string | 是 | 表示证书链校验器算法。当前仅支持输入“PKIX”。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| CertChainValidator | 表示证书链校验器对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let validator = cert.createCertChainValidator('PKIX');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`createCertChainValidator failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### CertChainValidator

证书链校验器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algorithm | string | 是 | 否 | X509证书链校验器算法名称。 |

#### validate

validate(certChain : CertChainData, callback : AsyncCallback<void>) : void

表示校验X509证书链。使用callback异步回调。

由于端侧系统时间不可信，证书链校验不包含对证书有效时间的校验。如果需要检查证书的时间有效性，可使用X509证书的[checkValidityWithDate](#ZH-CN_TOPIC_0000002522081410__checkvaliditywithdate)方法进行检查。详见[证书规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/certificate-framework-overview#证书规格)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certChain | CertChainData | 是 | 表示X509证书链序列化数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数，使用AsyncCallback的第一个error参数判断是否校验成功，error为null表示成功，error不为null表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书链二进制数据。
let certPem = '-----BEGIN CERTIFICATE-----\n' +
  'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
  'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
  'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
  'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
  'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
  'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
  'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
  '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
  '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
  'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
  'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
  'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
  'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
  '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
  'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
  'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
  'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
  'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
  '-----END CERTIFICATE-----';

let caPem = '-----BEGIN CERTIFICATE-----\n' +
'MIIC/zCCAeegAwIBAgIBATANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
'IENBMB4XDTI0MDMxOTAyMDIyNFoXDTM0MDMxNzAyMDIyNFowEjEQMA4GA1UEAwwH\n' +
'Um9vdCBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALxI5SDvRfKU\n' +
'6XaTeyh2LHlUK0rVSeYfXkYf5Mc3Pgucg+ewzQjxkACMx5NYaW1zfGDNPG1i5IZl\n' +
'cPeWNz1Tm2g6wTd+LyNoNOOmwfLV8pLXSfAukgNrBREf3BzVrbu7hvPd2MmLH23H\n' +
'OBM9uDPTIqu3n2CDN2EzwULjaSk2g+jvhVKsDLInu5uKPmZBFhs1FWKgcnVnlbi1\n' +
'AyAx4efheits6EO70oV6UufCEtS1VsBXQHZRAG4ogshWldRBVNxkU6yHAfg0mM/5\n' +
'EhrZsfh51fWqlrhNWrInjgNV3xIt5ebTIgKZWUlSVHEA/UqDoGfY+CsAJdteZWOW\n' +
'KjsrC/DK2O0CAwEAAaNgMF4wHQYDVR0OBBYEFHRb+SgJu8O0UYdRBkszePocqxbY\n' +
'MB8GA1UdIwQYMBaAFHRb+SgJu8O0UYdRBkszePocqxbYMA8GA1UdEwEB/wQFMAMB\n' +
'Af8wCwYDVR0PBAQDAgEGMA0GCSqGSIb3DQEBCwUAA4IBAQAKOT1ObfQNMN2wdfHq\n' +
'PQgFDDp6rBMbZe70LswPirSXljo4S/vfbG+gBoWCdu/SfsV+lyP75kg1wX0IQvzW\n' +
'xYNh864dgqPmGd0v8TIfM0UT0PpnowUyBHQ+E7LNYIOh/kjHbl3oERdEFA2PUyE9\n' +
'j3GLdg8oe/LqhEQCSAlH+v2RQgBZ9eVN+mSdUxwywm9U3acb0uqVkGiWK/ywumpg\n' +
'AmIZLMJtMVvg8uDkfy16Z4lChTEdNaJVUqPczUNk2kHXIF4we4be9HoOuTVz/SD/\n' +
'IsOhXn/BjS3jnhyS9fxo+opJf9zVTWI02Hlh1WVVtH/m3nIZblyAJhcjCHA2wZSz\n' +
'sSus\n' +
'-----END CERTIFICATE-----';

let certPemData = stringToUint8Array(certPem);
let caPemData = stringToUint8Array(caPem);

let certPemDataLenData = new Uint8Array(new Uint16Array([certPemData.length]).buffer)
let caPemDataLenData = new Uint8Array(new Uint16Array([caPemData.length]).buffer)

let certChainBuff =
  new Uint8Array(certPemDataLenData.length + certPemData.length + caPemDataLenData.length + caPemData.length)
certChainBuff.set(certPemDataLenData)
certChainBuff.set(certPemData, certPemDataLenData.length)
certChainBuff.set(caPemDataLenData, certPemDataLenData.length + certPemData.length)
certChainBuff.set(caPemData, certPemDataLenData.length + certPemData.length + caPemDataLenData.length)

let certChainData: cert.CertChainData = {
  data: certChainBuff,
  // 证书链包含的证书个数，需业务自行赋值。
  count: 2,
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

try {
  let validator = cert.createCertChainValidator('PKIX');
  validator.validate(certChainData, (error, data) => {
    if (error) {
      console.error(`validate failed, errCode: ${error.code}, errMsg: ${error.message}`);
    } else {
      console.info('validate result: success.');
    }
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`validate failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### validate

validate(certChain : CertChainData) : Promise<void>

表示校验X509证书链。使用Promise异步回调。

由于端侧系统时间不可信，证书链校验不包含对证书有效时间的校验。如果需要检查证书的时间有效性，可使用X509证书的[checkValidityWithDate](#ZH-CN_TOPIC_0000002522081410__checkvaliditywithdate)方法进行检查。详见[证书规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/certificate-framework-overview#证书规格)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certChain | CertChainData | 是 | 表示X509证书链序列化数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书链数据。
let certPem = '-----BEGIN CERTIFICATE-----\n' +
  'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
  'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
  'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
  'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
  'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
  'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
  'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
  '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
  '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
  'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
  'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
  'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
  'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
  '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
  'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
  'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
  'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
  'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
  '-----END CERTIFICATE-----';

let caPem = '-----BEGIN CERTIFICATE-----\n' +
'MIIC/zCCAeegAwIBAgIBATANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
'IENBMB4XDTI0MDMxOTAyMDIyNFoXDTM0MDMxNzAyMDIyNFowEjEQMA4GA1UEAwwH\n' +
'Um9vdCBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALxI5SDvRfKU\n' +
'6XaTeyh2LHlUK0rVSeYfXkYf5Mc3Pgucg+ewzQjxkACMx5NYaW1zfGDNPG1i5IZl\n' +
'cPeWNz1Tm2g6wTd+LyNoNOOmwfLV8pLXSfAukgNrBREf3BzVrbu7hvPd2MmLH23H\n' +
'OBM9uDPTIqu3n2CDN2EzwULjaSk2g+jvhVKsDLInu5uKPmZBFhs1FWKgcnVnlbi1\n' +
'AyAx4efheits6EO70oV6UufCEtS1VsBXQHZRAG4ogshWldRBVNxkU6yHAfg0mM/5\n' +
'EhrZsfh51fWqlrhNWrInjgNV3xIt5ebTIgKZWUlSVHEA/UqDoGfY+CsAJdteZWOW\n' +
'KjsrC/DK2O0CAwEAAaNgMF4wHQYDVR0OBBYEFHRb+SgJu8O0UYdRBkszePocqxbY\n' +
'MB8GA1UdIwQYMBaAFHRb+SgJu8O0UYdRBkszePocqxbYMA8GA1UdEwEB/wQFMAMB\n' +
'Af8wCwYDVR0PBAQDAgEGMA0GCSqGSIb3DQEBCwUAA4IBAQAKOT1ObfQNMN2wdfHq\n' +
'PQgFDDp6rBMbZe70LswPirSXljo4S/vfbG+gBoWCdu/SfsV+lyP75kg1wX0IQvzW\n' +
'xYNh864dgqPmGd0v8TIfM0UT0PpnowUyBHQ+E7LNYIOh/kjHbl3oERdEFA2PUyE9\n' +
'j3GLdg8oe/LqhEQCSAlH+v2RQgBZ9eVN+mSdUxwywm9U3acb0uqVkGiWK/ywumpg\n' +
'AmIZLMJtMVvg8uDkfy16Z4lChTEdNaJVUqPczUNk2kHXIF4we4be9HoOuTVz/SD/\n' +
'IsOhXn/BjS3jnhyS9fxo+opJf9zVTWI02Hlh1WVVtH/m3nIZblyAJhcjCHA2wZSz\n' +
'sSus\n' +
'-----END CERTIFICATE-----';

let certPemData = stringToUint8Array(certPem);
let caPemData = stringToUint8Array(caPem);

let certPemDataLenData = new Uint8Array(new Uint16Array([certPemData.length]).buffer)
let caPemDataLenData = new Uint8Array(new Uint16Array([caPemData.length]).buffer)

let certChainBuff =
  new Uint8Array(certPemDataLenData.length + certPemData.length + caPemDataLenData.length + caPemData.length)
certChainBuff.set(certPemDataLenData)
certChainBuff.set(certPemData, certPemDataLenData.length)
certChainBuff.set(caPemDataLenData, certPemDataLenData.length + certPemData.length)
certChainBuff.set(caPemData, certPemDataLenData.length + certPemData.length + caPemDataLenData.length)

let certChainData: cert.CertChainData = {
  data: certChainBuff,
  // 证书链包含的证书个数，需业务自行赋值。
  count: 2,
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

try {
  let validator = cert.createCertChainValidator('PKIX');
  validator.validate(certChainData).then(result => {
    console.info('validate result: success.');
  }).catch((error: BusinessError) => {
    console.error(`validate failed, errCode: ${error.code}, errMsg: ${error.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`validate failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### X509CrlEntry(deprecated)

被吊销证书对象。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CrlEntry](#ZH-CN_TOPIC_0000002522081410__x509crlentry11)替代。

#### getEncoded(deprecated)

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取被吊销证书的序列化数据。使用callback异步回调。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getEncoded](#ZH-CN_TOPIC_0000002522081410__getencoded11-2)替代。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<EncodingBlob> | 是 | 回调函数，表示被吊销证书的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (err, x509Crl) => {
  if (err) {
    console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 crl result: success.');

    try {
      let serialNumber = 1000;
      let crlEntry = x509Crl.getRevokedCert(serialNumber);
      crlEntry.getEncoded((error, data) => {
        if (error) {
          console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
        } else {
          console.info('getEncoded result: success.');
        }
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getEncoded(deprecated)

getEncoded() : Promise<EncodingBlob>

表示获取被吊销证书的序列化数据。使用Promise异步回调。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getEncoded](#ZH-CN_TOPIC_0000002522081410__getencoded11-3)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<EncodingBlob> | 表示被吊销证书的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (err, x509Crl) => {
  if (err) {
    console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 crl result: success.');

    try {
      let serialNumber = 1000;
      let crlEntry = x509Crl.getRevokedCert(serialNumber);
      crlEntry.getEncoded().then(result => {
        console.info('getEncoded result: success.');
      }).catch((error: BusinessError) => {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getSerialNumber(deprecated)

getSerialNumber() : number

表示获取被吊销证书的序列号。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getSerialNumber](#ZH-CN_TOPIC_0000002522081410__getserialnumber11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 表示被吊销证书的序列号。 |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (err, x509Crl) => {
  if (err) {
    console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 crl result: success.');

    try {
      let serialNumber = 1000;
      let crlEntry = x509Crl.getRevokedCert(serialNumber);
      serialNumber = crlEntry.getSerialNumber();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert or getSerialNumber failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getCertIssuer(deprecated)

getCertIssuer() : DataBlob

表示获取被吊销证书的颁发者信息。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getCertIssuer](#ZH-CN_TOPIC_0000002522081410__getcertissuer11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示被吊销证书的颁发者信息。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (err, x509Crl) => {
  if (err) {
    console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 crl result: success.');

    try {
      let serialNumber = 1000;
      let crlEntry = x509Crl.getRevokedCert(serialNumber);
      let issuer = crlEntry.getCertIssuer();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert or getCertIssuer failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getRevocationDate(deprecated)

getRevocationDate() : string

表示获取证书被吊销的日期，日期为ASN.1时间格式。


从API version 9开始支持，从API version 11开始废弃，建议使用[X509CRLEntry.getRevocationDate](#ZH-CN_TOPIC_0000002522081410__getrevocationdate11)替代。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示证书被吊销的日期，日期为ASN.1时间格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (err, x509Crl) => {
  if (err) {
    console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 crl result: success.');

    try {
      let serialNumber = 1000;
      let crlEntry = x509Crl.getRevokedCert(serialNumber);
      let date = crlEntry.getRevocationDate();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert or getRevocationDate failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### X509CRLEntry11+

被吊销证书对象。

#### getEncoded11+

getEncoded(callback : AsyncCallback<EncodingBlob>) : void

表示获取被吊销证书的序列化数据。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<EncodingBlob> | 是 | 回调函数，表示被吊销证书的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 CRL result: success.');

    try {
      let serialNumber = BigInt(1000);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      crlEntry.getEncoded((error, data) => {
        if (error) {
          console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
        } else {
          console.info('getEncoded result: success.');
        }
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getEncoded11+

getEncoded() : Promise<EncodingBlob>

表示获取被吊销证书的序列化数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<EncodingBlob> | 表示被吊销证书的序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 CRL result: success.');

    try {
      let serialNumber = BigInt(1000);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      crlEntry.getEncoded().then(result => {
        console.info('getEncoded result: success.');
      }).catch((error: BusinessError) => {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getSerialNumber11+

getSerialNumber() : bigint

表示获取被吊销证书的序列号。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| bigint | 表示被吊销证书的序列号。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('createX509CRL result: success.');

    try {
      let serialNumber = BigInt(1000);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      serialNumber = crlEntry.getSerialNumber();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert or getSerialNumber failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getCertIssuer11+

getCertIssuer() : DataBlob

表示获取被吊销证书的颁发者信息。

获取到的被吊销证书的颁发者信息数据带字符串结束符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示被吊销证书的颁发者信息。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('createX509CRL result: success.');

    try {
      let serialNumber = BigInt(1000);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      let issuer = crlEntry.getCertIssuer();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert or getCertIssuer failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getCertIssuer20+

getCertIssuer(encodingType: EncodingType): string

根据编码类型获取被吊销证书的颁发者信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | EncodingType | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示被吊销证书的颁发者信息，使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The value of encodingType is not in the EncodingType enumeration range. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

 let crlData = '-----BEGIN X509 CRL-----\n' +
    'MIIBTDCBtgIBATANBgkqhkiG9w0BAQsFADBZMQswCQYDVQQGEwJDTjEPMA0GA1UE\n' +
    'CAwG6ZmV6KW/MQ8wDQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEXMBUG\n' +
    'A1UEAwwO5Lit5paH5rWL6K+VIyMXDTI1MDMyNDA5MTExNVoXDTI1MDQyMzA5MTEx\n' +
    'NVowGTAXAgYBcqcmOsAXDTI1MDIyMDA2MTMwM1qgDjAMMAoGA1UdFAQDAgECMA0G\n' +
    'CSqGSIb3DQEBCwUAA4GBACedFnn4unfYLiRCl1ZAFXx6LFdX6U+IZ/buW44xKAWi\n' +
    'fyvcSxKIeGtMVjmQSs4HeNfNujIjaDN1+/J2nLSmHPiQ/c0LAc47zefVt2VnFuR4\n' +
    'TMUJEDUlnekYfDMxQqtihAO/Bpw33twK6otDvaAPm9vJoCu8JmGXxt6g+8vbYuNT\n' +
    '-----END X509 CRL-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('createX509CRL result: success.');

    try {
      let serialNumber = BigInt(1591942200000);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      let issuer = crlEntry.getCertIssuer(cert.EncodingType.ENCODING_UTF8);
      console.info('issuer output = ' + issuer);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert or getCertIssuer failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getRevocationDate11+

getRevocationDate() : string

表示获取证书被吊销的日期。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示证书被吊销的日期。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('createX509CRL result: success.');

    try {
      let serialNumber = BigInt(1000);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      let date = crlEntry.getRevocationDate();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert or getRevocationDate failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getExtensions11+

getExtensions(): DataBlob

表示获取CRL的扩展。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示X509CRLEntry扩展用途。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIIBjjB4AgEBMA0GCSqGSIb3DQEBCwUAMBIxEDAOBgNVBAMMB1Jvb3QgQ0EXDTI0\n' +
  'MDMxOTAyMDQwN1oXDTI0MDQxODAyMDQwN1owIjAgAgEEFw0yNDAzMTkwMjA0MDZa\n' +
  'MAwwCgYDVR0VBAMKAQGgDjAMMAoGA1UdFAQDAgEAMA0GCSqGSIb3DQEBCwUAA4IB\n' +
  'AQCbjvmHxC8dW6WCS/ga73kx2b7f8I/2eVuDYyReuBiGWeJ9vDmGqimJ9VwOk+ph\n' +
  'LvG/2Zvh9I8qXxnOWeseA2C0bEshJGvXpquIjm00OUyLlK6jdfRbhXT8OyvDjqZs\n' +
  'e1IsMV7Zo11SUc8nR2d0QQ7EVDCN/XFKPsmoK7PhJnRh5gc8W3FKQ6b8H9kdjgTa\n' +
  'KQUap1OIDReVsjPBmRAbwMMLtbrAMllF7E6x7uHgHTGaK1ZPJDtsnCJ45ur3mk/o\n' +
  'HAJFwHNjNDltiEfvMSs76/X0cwitpeW4dFk6c3QtqhxJrHDD4gl8di+xHOyHXpzX\n' +
  '+i2osvdPWRia0dJCL1PCA14k\n' +
  '-----END X509 CRL-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('createX509CRL result: success.');

    try {
      let serialNumber = BigInt(4);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      let extensions = crlEntry.getExtensions();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert or getExtensions failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### hasExtensions11+

hasExtensions(): boolean

表示判断CRL Entry是否有扩展。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true则表示CRL Entry有扩展，返回false则表示无扩展。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('createX509CRL result: success.');

    try {
      let serialNumber = BigInt(1000);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      let hasExtensions = crlEntry.hasExtensions();
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert or hasExtensions failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
})
```

#### getCertIssuerX500DistinguishedName12+

getCertIssuerX500DistinguishedName(): X500DistinguishedName

获取证书颁发者的X509可分辨名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| X500DistinguishedName | X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function certGetCertIssuerX500DistinguishedName() {
  let x509Crl: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509Crl = await cert.createX509CRL(encodingBlob);
    console.info('createX509CRL result: success.');
    let name = x509Crl.getRevokedCert(BigInt(1000)).getCertIssuerX500DistinguishedName();
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### toString12+

toString(): string

获取对象的字符串类型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function certToString() {
  let x509Crl: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509Crl = await cert.createX509CRL(encodingBlob);
    console.info('createX509CRL result: success.');
    console.info('toString success: ' + x509Crl.getRevokedCert(BigInt(1000)).toString());
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### hashCode12+

hashCode(): Uint8Array

获取DER格式数据的哈希值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | DER格式数据的哈希值。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n'

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function certHashCode() {
  let x509Crl: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509Crl = await cert.createX509CRL(encodingBlob);
    console.info('createX509CRL result: success.');
    console.info('hashCode success: ' + x509Crl.getRevokedCert(BigInt(1000)).hashCode());
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getExtensionsObject12+

getExtensionsObject(): CertExtension

获取对应实体的扩展域DER格式数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| CertExtension | 证书扩展域段类对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIINlTCCDH0CAQEwDQYJKoZIhvcNAQELBQAwTDELMAkGA1UEBhMCVVMxFTATBgNV\n' +
  'BAoTDERpZ2lDZXJ0IEluYzEmMCQGA1UEAxMdRGlnaUNlcnQgU2VjdXJlIFNpdGUg\n' +
  'Q04gQ0EgRzMXDTI0MDMxMjE4NDQ0NVoXDTI0MDMxOTE4NDQ0NVowggvJMCECEAbk\n' +
  'wC/+N2YXfpw7vgDJ2xAXDTIzMDIwNzA1NTg1OFowIQIQDonqcHww7uhlmWH+OfIe\n' +
  'PhcNMjMwMzA5MDcwMzI1WjAvAhAM4CTrULrJUEinWgT9AFPvFw0yMzAzMjAxOTE4\n' +
  'NTRaMAwwCgYDVR0VBAMKAQQwIQIQBQP4xflKkcRehoJ2NaA/jhcNMjMwMzIyMDk0\n' +
  'NTI5WjAvAhAOmgzoiIqznAaFec53PVPUFw0yMzAzMjcyMDI4MDNaMAwwCgYDVR0V\n' +
  'BAMKAQQwLwIQBaC2Z3D4dcQ/O7HnzFU9KBcNMjMwMzI5MTc1OTQ1WjAMMAoGA1Ud\n' +
  'FQQDCgEFMCECEAlz9Rg1b+9La4oFqsHUc4AXDTIzMDMzMTAyMzk0MVowIQIQD9yW\n' +
  '92pX6BinUKVBVSSTmBcNMjMwNDExMDExNjI5WjAvAhAIIarHUWWee4V9W/Yzm86k\n' +
  'Fw0yMzA0MTQyMDE5MTJaMAwwCgYDVR0VBAMKAQQwIQIQC2OiM3VIJX2dEe8/pf8f\n' +
  'hRcNMjMwNDIxMDMzMDIyWjAhAhAP0ueyg5n/7b2Hotml7f42Fw0yMzA0MjYwMjU3\n' +
  'NDJaMCECEAqMu61nkOEmTOdMbUZTMrkXDTIzMDUxNzAxMzI0NVowLwIQDYv1rt0K\n' +
  'olvP+nQoi5LeLRcNMjMwNTIzMTc0MDE4WjAMMAoGA1UdFQQDCgEEMC8CEA8WMKlw\n' +
  'iCK36PruJvup5bUXDTIzMDUyMzE3NDA1M1owDDAKBgNVHRUEAwoBBDAvAhAJ5uwT\n' +
  'aqwgLzNVpxh4u9EPFw0yMzA1MjUxNzEwNTBaMAwwCgYDVR0VBAMKAQQwIQIQCg0k\n' +
  '5UadwDH5xm14yxcgLRcNMjMwNjA3MDcyNDAwWjAhAhAEByUhbBR6/pZRFUH2PTxE\n' +
  'Fw0yMzA2MDgwMjIwMzBaMCECEATquAQcy3W1kUOkb4VoOvEXDTIzMDYyNjA5MDIw\n' +
  'NlowIQIQBrF5sueIjk1snKdO0ISOXhcNMjMwNjMwMDI0MDA0WjAhAhAJEG72WQtV\n' +
  'lTOYiA0xjVk5Fw0yMzA3MDUwMjEyMzdaMCECEAmXIuCMJv9gllYuKfCHm5EXDTIz\n' +
  'MDcwNTAyMTIzN1owIQIQAotQots0ngzRwACzrS9mCBcNMjMwNzA2MDU0NDU3WjAh\n' +
  'AhAG2hyGc9SfXrLc0Uk2J1BeFw0yMzA3MjQwMTUwNDBaMCECEAJhm5FSlVyTG9UK\n' +
  'zS+ecUgXDTIzMDcyNjA2NDQzM1owIQIQC4mlxBQuFxWC4pF7/P8BDxcNMjMwNzMx\n' +
  'MTAzMjU0WjAhAhADCEp333/avF3m6HZtBImOFw0yMzA3MzExMDMzNTBaMCECEAKd\n' +
  'P7fydlXUcS4v/YnZMMwXDTIzMDczMTEwMzQzOFowIQIQC+m5EUcRd1E0lEIPj17Z\n' +
  'rRcNMjMwODAxMDYwNDE4WjAvAhAF4QcgQQlWpAi4FVflzbKxFw0yMzA4MDMxNjIz\n' +
  'MTdaMAwwCgYDVR0VBAMKAQQwIQIQAn01GEZ50Y5ugIcEuGfF9BcNMjMwODA4MDE1\n' +
  'NzM1WjAhAhAFHj3FDKeP9q9CM924d8RIFw0yMzA4MDgwMTU5NDhaMC8CEAnkNPSD\n' +
  'U5yiMsV3fU06a6oXDTIzMDgwODE5MjIwMlowDDAKBgNVHRUEAwoBBDAvAhAETU4z\n' +
  '13iMKiwQujsxJDRhFw0yMzA4MTAyMDU4NDdaMAwwCgYDVR0VBAMKAQQwIQIQB1oD\n' +
  'M2mOYuse7e/nTqx+8xcNMjMwOTA0MDUwOTU3WjAhAhALf3Bp63so6O+R5QbWPWu6\n' +
  'Fw0yMzEwMDkwNjE5NTVaMCECEAKFHdXcy/zBXRtMj3BVhO0XDTIzMTAwOTA2MTk1\n' +
  'N1owIQIQDNNmVHN4tMu1xth6IAe4ZhcNMjMxMDEyMDc0MjQ1WjAhAhACNNJA2oMM\n' +
  'pr+giIgczvHOFw0yMzEwMTYwNTEyMzdaMCECEAoQun7uSHhvy6GBoxG7XOkXDTIz\n' +
  'MTExNjA3MDAzN1owLwIQA1NsI22PLvohCvKwdtAJwBcNMjMxMjA2MTgyNzUzWjAM\n' +
  'MAoGA1UdFQQDCgEEMCECEAWagozDt4jfBzi+aDGFr88XDTIzMTIxMTA3MjM1OFow\n' +
  'IQIQD1g7NdEk7t05zg6yweYc5hcNMjMxMjExMDcyNTM3WjAhAhAMJnRjUQAzFQFH\n' +
  'kwIguRz2Fw0yMzEyMTEwNzI2NDJaMCECEAT0bVxyPKkeTV8JQuPxfcwXDTIzMTIx\n' +
  'MTA3MjcyNlowIQIQA/5BlE0Ushtw24Ol9L2sexcNMjMxMjExMDcyODA2WjAhAhAL\n' +
  'Ij6FAKVJDnKAwwt19+/RFw0yMzEyMTEwNzI5MDJaMCECEAmPyfX3FuOHgryS2i8c\n' +
  'SrUXDTIzMTIxMTA3Mjk0M1owIQIQC+uGa6tmPRPCB0jW+6WWUhcNMjMxMjExMDcz\n' +
  'MDIzWjAhAhAJCq59mFZj6SWLH/m18Fq2Fw0yMzEyMTEwNzMwNTJaMCECEAp0Po24\n' +
  'WHmdEMTVyp9AMssXDTIzMTIxMTA3MzEyNlowIQIQAcf+793qPEHipkAhjf7MghcN\n' +
  'MjMxMjExMDczMTQ5WjAhAhAElLuCARMBoDIH0Y2D1DpSFw0yMzEyMTEwNzMyMTla\n' +
  'MCECEAWlgWhTXqKOB61zA7Ao8vQXDTIzMTIxMTA3MzI0OFowIQIQAeZqfkFYc/6t\n' +
  'zO7j/FVYwBcNMjMxMjExMDczMzM1WjAhAhAHzftyRhskxV6opTfHb59OFw0yMzEy\n' +
  'MTEwNzM0MDNaMCECEASXrBHdRYUm9VIZ1wN4qAsXDTIzMTIxMTA3MzQyN1owIQIQ\n' +
  'BDFb/OY65CZ1sTdMPAc+IhcNMjMxMjExMDczNTEzWjAhAhAFg7mRyWvWXc+KT014\n' +
  'Ro5AFw0yMzEyMTEwNzM1NDhaMCECEA+wAstqfBUEkSvinYlWeOwXDTIzMTIxMTA3\n' +
  'MzYyNVowIQIQB3Z75ksHGnvGmuHbvwbheRcNMjMxMjExMDczNjU5WjAhAhALfrIn\n' +
  'OGRVeePivKkJ+d1xFw0yMzEyMTEwNzM4MDFaMCECEAnm5NfU36m+FXNlJiUsXpMX\n' +
  'DTIzMTIxMTA3MzgzNVowIQIQCrBoHo4X2md3Amteqh7h3RcNMjMxMjExMDczOTA3\n' +
  'WjAhAhAGxHlqrHu66ifOwTTMhHHFFw0yMzEyMTEwNzM5NDNaMCECEA2BDG1SI7Se\n' +
  '2GAt+b9UnF8XDTIzMTIxMTA3NDAyNFowLwIQDZvl5jkmAwjTweDCtrXbLRcNMjMx\n' +
  'MjExMjA0NDQ3WjAMMAoGA1UdFQQDCgEEMCECEAzgcwGVpyXXZSmLLF4MExQXDTIz\n' +
  'MTIxOTE3MjczMlowIQIQARB9nVoMuE5GSFeb3U553hcNMjMxMjE5MTcyODA1WjAh\n' +
  'AhAD+JIH7lFcX9UNqTogrMcPFw0yMzEyMTkxNzI5MDZaMCECEAux1kd8ugXs4mI+\n' +
  'xMfXgpsXDTIzMTIxOTE3MjkyOFowIQIQCUO5VqAmbxA8Jdly97msLhcNMjMxMjE5\n' +
  'MTcyOTU0WjAhAhAFyzrU1JtsiPNPeWrfdvGvFw0yMzEyMTkxNzMwNDlaMCECEAwT\n' +
  'tMq5EsBTUhQwm6nWhnAXDTIzMTIyMDE3NDc1NlowIQIQBx3qL8rMclE9gxamaa14\n' +
  'xBcNMjMxMjIwMTc0ODM2WjAhAhAOnKUlrCaxs+lRqLrBmk2PFw0yNDAxMzAxOTMw\n' +
  'MTVaMCECEAtYs/5ZRsrMAxQVDA44eWYXDTI0MDIwNjA2MjYwMFowIQIQDjrMV1d3\n' +
  '0NhxngX5rqqxjBcNMjQwMjIxMDc0ODEwWjAhAhAPGohz3+JyS6H4JzHCjLrXFw0y\n' +
  'NDAyMjgyMDQxMjZaMC8CEAqZ2QktAMprzZmtolbOXlgXDTI0MDIyOTE4MDYzMVow\n' +
  'DDAKBgNVHRUEAwoBBDAhAhAMAHgNfiburtKDp8OJuzRCFw0yNDAzMDQwNjA3MzJa\n' +
  'MCECEA/HgrXcSBqkb2JdfrFDAfgXDTI0MDMwNDA2MDczMlqgMDAuMB8GA1UdIwQY\n' +
  'MBaAFETZyEozjtNSjaeSlGEfmsilt+zLMAsGA1UdFAQEAgIFrDANBgkqhkiG9w0B\n' +
  'AQsFAAOCAQEAJ5rSr0Av5sH59J2LXW5hZ8SJTzDbR8ADdi/CCLolbUUnE0oaAZ+2\n' +
  '9z0niAD5m8HQikNz8K+FKAsQatN/CAj4bzRMeF37hQCiZpqNtxP69JDGeWpGPiH2\n' +
  'K/YfpzL9iSbBOxFmosxUX8J/iX36mCUl+3OUHh+qSYeElboxeAmTCnY5Pl5Bq9is\n' +
  'gp0MmzNYCo7GEFrtS03p2msK25uRqQl6Qn0NZS0yGjdUG7RTZe4xua5drjEkB1o/\n' +
  '15f+mtYj6DtWM1twi1q3VYVxhRSsk6XmmS0BViTEl+MT0BRAPwBSdlyt++1Pnnrd\n' +
  'BsQoO8O2EVpJ54fxKMCSDOkJf1hNCxi3eQ==\n' +
  '-----END X509 CRL-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function certGetExtensionsObject() {
  let x509Crl: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509Crl = await cert.createX509CRL(encodingBlob);
    console.info('createX509CRL result: success.');
    let object = x509Crl.getRevokedCert(BigInt('14091103387070223745671018446433705560')).getExtensionsObject();
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cert.createCertCRLCollection11+

createCertCRLCollection(certs: Array<X509Cert>, crls?: Array<X509CRL>): CertCRLCollection

表示创建证书和证书吊销列表集合对象，并返回相应的结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certs | Array<X509Cert> | 是 | X509Cert数组。 |
| crls | Array<X509CRL> | 否 | X509CRL数组。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| CertCRLCollection | 表示证书和证书吊销列表集合对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
19020001memory malloc failed.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509CRL(): Promise<cert.X509CRL> {
  let crlData = '-----BEGIN X509 CRL-----\n' +
    'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
    'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
    'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
    'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
    '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
    'eavsH0Q3\n' +
    '-----END X509 CRL-----\n';

  // 证书吊销列表二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(crlData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509CRL: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509CRL = await cert.createX509CRL(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509CRL;
}

async function createX509Cert(): Promise<cert.X509Cert> {
  let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
    'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
    'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
    'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
    'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
    'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
    'Qw==\n' +
    '-----END CERTIFICATE-----\n';

  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509Cert;
}

async function createCollection() {
  const x509Cert = await createX509Cert();
  const x509CRL = await createX509CRL();
  try {
    const collection: cert.CertCRLCollection = cert.createCertCRLCollection([x509Cert], [x509CRL]);
    console.info('createCertCRLCollection result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createCertCRLCollection failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### CertCRLCollection11+

证书和证书吊销列表集合对象。

#### selectCerts11+

selectCerts(param: X509CertMatchParameters): Promise<Array<X509Cert>>

查找证书和证书吊销列表集合中所有与参数匹配的证书对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | X509CertMatchParameters | 是 | 表示证书需匹配的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<X509Cert>> | Promise对象。表示匹配到的证书对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509Cert(): Promise<cert.X509Cert> {
  let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
    'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
    'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
    'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
    'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
    'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
    'Qw==\n' +
    '-----END CERTIFICATE-----\n';

  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509Cert;
}

async function selectCerts() {
  const x509Cert = await createX509Cert();
  const collection = cert.createCertCRLCollection([x509Cert]);

  try {
    const param: cert.X509CertMatchParameters = {
      x509Cert,
      validDate: '20231121074700Z',
      issuer: new Uint8Array([0x30, 0x1a, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0C, 0x0F, 0x45, 0x78, 0x61, 0x6D, 0x70, 0x6C, 0x65, 0x20, 0x52, 0x6F, 0x6F, 0x74, 0x20, 0x43, 0x41]),
      subject: new Uint8Array([0x30, 0x1a, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0C, 0x0F, 0x45, 0x78, 0x61, 0x6D, 0x70, 0x6C, 0x65, 0x20, 0x52, 0x6F, 0x6F, 0x74, 0x20, 0x43, 0x41]),
      publicKeyAlgID: '1.2.840.10045.2.1'
    };
    const certs = await collection.selectCerts(param);
    console.info('call selectCerts result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`call selectCerts failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### selectCerts11+

selectCerts(param: X509CertMatchParameters, callback: AsyncCallback<Array<X509Cert>>): void

查找证书和证书吊销列表集合中所有与参数匹配的证书对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | X509CertMatchParameters | 是 | 表示证书需匹配的参数。 |
| callback | AsyncCallback<Array<X509Cert>> | 是 | 回调函数，表示匹配到的证书对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509Cert(): Promise<cert.X509Cert> {
  let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
    'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
    'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
    'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
    'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
    'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
    'Qw==\n' +
    '-----END CERTIFICATE-----\n';

  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509Cert;
}

async function selectCerts() {
  const x509Cert = await createX509Cert();
  const collection = cert.createCertCRLCollection([x509Cert]);
  // 需业务自行赋值。
  const param: cert.X509CertMatchParameters = {
    x509Cert,
    validDate: '20231121074700Z',
    issuer: new Uint8Array([0x30, 0x1a, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0C, 0x0F, 0x45, 0x78, 0x61, 0x6D, 0x70, 0x6C, 0x65, 0x20, 0x52, 0x6F, 0x6F, 0x74, 0x20, 0x43, 0x41]),
    subject: new Uint8Array([0x30, 0x1a, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0C, 0x0F, 0x45, 0x78, 0x61, 0x6D, 0x70, 0x6C, 0x65, 0x20, 0x52, 0x6F, 0x6F, 0x74, 0x20, 0x43, 0x41]),
    publicKeyAlgID: '1.2.840.10045.2.1'
  };
  collection.selectCerts(param, (err, certs) => {
    if (err) {
      console.error(`selectCerts failed, errCode: ${err.code}, errMsg: ${err.message}`);
    } else {
      console.info('selectCerts result: success.');
    }
  });
}
```

#### selectCRLs11+

selectCRLs(param: X509CRLMatchParameters): Promise<Array<X509CRL>>

查找证书和证书吊销列表集合中所有与参数匹配的证书吊销列表对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | X509CRLMatchParameters | 是 | 表示证书吊销列表需匹配的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<X509CRL>> | Promise对象，表示匹配到的证书吊销列表对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509CRL(): Promise<cert.X509CRL> {
  let crlData = '-----BEGIN X509 CRL-----\n' +
    'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
    'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
    'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
    'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
    '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
    'eavsH0Q3\n' +
    '-----END X509 CRL-----\n';

  // 证书吊销列表二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(crlData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509CRL: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509CRL = await cert.createX509CRL(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509CRL;
}

async function createX509Cert(): Promise<cert.X509Cert> {
  const certData = '-----BEGIN CERTIFICATE-----\r\n' +
    'MIIC8TCCAdmgAwIBAgIIFB75m06RTHwwDQYJKoZIhvcNAQELBQAwWDELMAkGA1UE\r\n' +
    'BhMCQ04xEDAOBgNVBAgTB0ppYW5nc3UxEDAOBgNVBAcTB05hbmppbmcxCzAJBgNV\r\n' +
    'BAoTAnRzMQswCQYDVQQLEwJ0czELMAkGA1UEAxMCdHMwHhcNMjMxMTIzMDMzMjAw\r\n' +
    'WhcNMjQxMTIzMDMzMjAwWjBhMQswCQYDVQQGEwJDTjEQMA4GA1UECBMHSmlhbmdz\r\n' +
    'dTEQMA4GA1UEBxMHTmFuamluZzEMMAoGA1UEChMDdHMxMQwwCgYDVQQLEwN0czEx\r\n' +
    'EjAQBgNVBAMTCTEyNy4wLjAuMTAqMAUGAytlcAMhALsWnY9cMNC6jzduM69vI3Ej\r\n' +
    'pUlgHtEHS8kRfmYBupJSo4GvMIGsMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNSg\r\n' +
    'poQvfxR8A1Y4St8NjOHkRpm4MAsGA1UdDwQEAwID+DAnBgNVHSUEIDAeBggrBgEF\r\n' +
    'BQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEyNy4wLjAuMTAR\r\n' +
    'BglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0\r\n' +
    'ZTANBgkqhkiG9w0BAQsFAAOCAQEAfnLmPF6BtAUCZ9pjt1ITdXc5M4LJfMw5IPcv\r\n' +
    'fUAvhdaUXtqBQcjGCWtDdhyb1n5Xp+N7oKz/Cnn0NGFTwVArtFiQ5NEP2CmrckLh\r\n' +
    'Da4VnsDFU+zx2Bbfwo5Ms7iArxyx0fArbMZzN9D1lZcVjiIxp1+3k1/0sdCemcY/\r\n' +
    'y7mw5NwkcczLWLBZl1/Ho8b4dlo1wTA7TZk9uu8UwYBwXDrQe6S9rMcvMcRKiJ9e\r\n' +
    'V4SYZIO7ihr8+n4LQDQP+spvX4cf925a3kyZrftfvGCJ2ZNwvsPhyumYhaBqAgSy\r\n' +
    'Up2BImymAqPi157q9EeYcQz170TtDZHGmjYzdQxhOAHRb6/IdQ==\r\n' +
    '-----END CERTIFICATE-----\r\n';
  const certEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    encodingFormat: cert.EncodingFormat.FORMAT_PEM,
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(certEncodingBlob);
    console.info('createX509Cert result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509Cert;
}

async function selectCRLs() {
  const x509CRL = await createX509CRL();
  const x509Cert = await createX509Cert();
  const collection = cert.createCertCRLCollection([], [x509CRL]);

  const param: cert.X509CRLMatchParameters = {
    issuer: [new Uint8Array([0x30, 0x58, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x43, 0x4E,
      0x31, 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x4A, 0x69, 0x61, 0x6E, 0x67, 0x73, 0x75, 0x31,
      0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x07, 0x4E, 0x61, 0x6E, 0x6A, 0x69, 0x6E, 0x67, 0x31, 0x0B,
      0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x0A, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04,
      0x0B, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x03, 0x13, 0x02, 0x74, 0x73])],
    x509Cert: x509Cert
  }
  try {
    const crls = await collection.selectCRLs(param);
    console.info('selectCRLs result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`selectCRLs failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### selectCRLs11+

selectCRLs(param: X509CRLMatchParameters, callback: AsyncCallback<Array<X509CRL>>): void

查找证书和证书吊销列表集合中所有与参数匹配的证书吊销列表对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | X509CRLMatchParameters | 是 | 表示证书吊销列表需匹配的参数对象。 |
| callback | AsyncCallback<Array<X509CRL>> | 是 | 回调函数，表示匹配到的证书吊销列表对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509CRL(): Promise<cert.X509CRL> {
  let crlData = '-----BEGIN X509 CRL-----\n' +
    'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
    'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
    'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
    'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
    '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
    'eavsH0Q3\n' +
    '-----END X509 CRL-----\n';

  // 证书吊销列表二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(crlData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509CRL: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509CRL = await cert.createX509CRL(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509CRL;
}

async function createX509Cert(): Promise<cert.X509Cert> {
  const certData = '-----BEGIN CERTIFICATE-----\r\n' +
    'MIIC8TCCAdmgAwIBAgIIFB75m06RTHwwDQYJKoZIhvcNAQELBQAwWDELMAkGA1UE\r\n' +
    'BhMCQ04xEDAOBgNVBAgTB0ppYW5nc3UxEDAOBgNVBAcTB05hbmppbmcxCzAJBgNV\r\n' +
    'BAoTAnRzMQswCQYDVQQLEwJ0czELMAkGA1UEAxMCdHMwHhcNMjMxMTIzMDMzMjAw\r\n' +
    'WhcNMjQxMTIzMDMzMjAwWjBhMQswCQYDVQQGEwJDTjEQMA4GA1UECBMHSmlhbmdz\r\n' +
    'dTEQMA4GA1UEBxMHTmFuamluZzEMMAoGA1UEChMDdHMxMQwwCgYDVQQLEwN0czEx\r\n' +
    'EjAQBgNVBAMTCTEyNy4wLjAuMTAqMAUGAytlcAMhALsWnY9cMNC6jzduM69vI3Ej\r\n' +
    'pUlgHtEHS8kRfmYBupJSo4GvMIGsMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNSg\r\n' +
    'poQvfxR8A1Y4St8NjOHkRpm4MAsGA1UdDwQEAwID+DAnBgNVHSUEIDAeBggrBgEF\r\n' +
    'BQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEyNy4wLjAuMTAR\r\n' +
    'BglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0\r\n' +
    'ZTANBgkqhkiG9w0BAQsFAAOCAQEAfnLmPF6BtAUCZ9pjt1ITdXc5M4LJfMw5IPcv\r\n' +
    'fUAvhdaUXtqBQcjGCWtDdhyb1n5Xp+N7oKz/Cnn0NGFTwVArtFiQ5NEP2CmrckLh\r\n' +
    'Da4VnsDFU+zx2Bbfwo5Ms7iArxyx0fArbMZzN9D1lZcVjiIxp1+3k1/0sdCemcY/\r\n' +
    'y7mw5NwkcczLWLBZl1/Ho8b4dlo1wTA7TZk9uu8UwYBwXDrQe6S9rMcvMcRKiJ9e\r\n' +
    'V4SYZIO7ihr8+n4LQDQP+spvX4cf925a3kyZrftfvGCJ2ZNwvsPhyumYhaBqAgSy\r\n' +
    'Up2BImymAqPi157q9EeYcQz170TtDZHGmjYzdQxhOAHRb6/IdQ==\r\n' +
    '-----END CERTIFICATE-----\r\n';
  const certEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    encodingFormat: cert.EncodingFormat.FORMAT_PEM,
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(certEncodingBlob);
    console.info('createX509Cert result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509Cert;
}

async function selectCRLs() {
  const x509CRL = await createX509CRL();
  const x509Cert = await createX509Cert();
  const collection = cert.createCertCRLCollection([], [x509CRL]);

  const param: cert.X509CRLMatchParameters = {
    issuer: [new Uint8Array([0x30, 0x58, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x43, 0x4E,
      0x31, 0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x4A, 0x69, 0x61, 0x6E, 0x67, 0x73, 0x75, 0x31,
      0x10, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x07, 0x4E, 0x61, 0x6E, 0x6A, 0x69, 0x6E, 0x67, 0x31, 0x0B,
      0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x0A, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04,
      0x0B, 0x13, 0x02, 0x74, 0x73, 0x31, 0x0B, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x03, 0x13, 0x02, 0x74, 0x73])],
    x509Cert: x509Cert
  }
  collection.selectCRLs(param, (err, crls) => {
    if (err) {
      console.error(`selectCRLs failed, errCode: ${err.code}, errMsg: ${err.message}`);
    } else {
      console.info('selectCRLs result: success.');
    }
  });
}
```

#### cert.createX509CertChain11+

createX509CertChain(inStream: EncodingBlob): Promise<X509CertChain>

表示创建X509证书链对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | X509证书序列化数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<X509CertChain> | 表示X509证书链对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509CertChain(): Promise<cert.X509CertChain> {
  let certChainData = '-----BEGIN CERTIFICATE-----\n' +
    'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
    'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
    'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
    'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
    'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
    'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
    'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
    'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
    'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
    'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
    'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
    '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
    'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
    'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
    'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
    'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
    'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
    'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
    'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
    'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
    'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
    '-----END CERTIFICATE-----\n' +
    '-----BEGIN CERTIFICATE-----\n' +
    'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
    'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
    'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
    'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
    'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
    'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
    'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
    'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
    'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
    'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
    'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
    'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
    'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
    'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
    'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
    'uKPWR9dKBA==\n' +
    '-----END CERTIFICATE-----\n' +
    '-----BEGIN CERTIFICATE-----\n' +
    'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
    'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
    'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
    'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
    'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
    'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
    'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
    'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
    'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
    'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
    'xjoE\n' +
    '-----END CERTIFICATE-----\n';

  // 证书链二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certChainData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
  try {
    x509CertChain = await cert.createX509CertChain(encodingBlob);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509CertChain;
}

createX509CertChain();
```

#### cert.createX509CertChain11+

createX509CertChain(inStream: EncodingBlob, callback: AsyncCallback<X509CertChain>): void

表示创建X509证书链对象。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inStream | EncodingBlob | 是 | X509证书序列化数据。 |
| callback | AsyncCallback<X509CertChain> | 是 | 回调函数，表示X509证书链对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certChainData = '-----BEGIN CERTIFICATE-----\n' +
  'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
  'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
  'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
  'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
  'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
  'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
  'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
  'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
  'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
  'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
  'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
  '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
  'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
  'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
  'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
  'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
  'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
  'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
  'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
  'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
  'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
  '-----END CERTIFICATE-----\n' +
  '-----BEGIN CERTIFICATE-----\n' +
  'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
  'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
  'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
  'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
  'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
  'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
  'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
  'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
  'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
  'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
  'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
  'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
  'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
  'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
  'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
  'uKPWR9dKBA==\n' +
  '-----END CERTIFICATE-----\n' +
  '-----BEGIN CERTIFICATE-----\n' +
  'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
  'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
  'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
  'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
  'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
  'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
  'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
  'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
  'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
  'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
  'xjoE\n' +
  '-----END CERTIFICATE-----\n';

// 证书链二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certChainData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CertChain(encodingBlob, (err, certChain) => {
  if (err) {
    console.error(`createX509CertChain failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('createX509CertChain result: success.');
  }
});
```

#### cert.createX509CertChain11+

createX509CertChain(certs: Array<X509Cert>): X509CertChain

表示使用X509Cert数组方式创建X509证书链对象，并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certs | Array<X509Cert> | 是 | X509证书对象数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| X509CertChain | 表示X509证书链对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509Cert(): Promise<cert.X509Cert> {
  let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
    'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
    'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
    'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
    'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
    'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
    'Qw==\n' +
    '-----END CERTIFICATE-----\n';

  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509Cert;
}

async function createX509CertChain(): Promise<cert.X509CertChain> {
  const x509Cert = await createX509Cert();
  let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
  try {
    x509CertChain = cert.createX509CertChain([x509Cert]);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509CertChain;
}

createX509CertChain();
```

#### cert.buildX509CertChain12+

buildX509CertChain(param: [CertChainBuildParameters](#ZH-CN_TOPIC_0000002522081410__certchainbuildparameters12)): Promise<CertChainBuildResult>

表示使用CertChainBuildParameters对象方式创建X509证书链对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | CertChainBuildParameters | 是 | 构建证书链的参数对象。 CertChainBuildParameters中的maxLength要小于证书集合中证书数量。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<CertChainBuildResult> | 表示X509证书链对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书链数据。
let certPem = '-----BEGIN CERTIFICATE-----\n' +
  'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
  'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
  'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
  'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
  'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
  'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
  'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
  '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
  '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
  'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
  'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
  'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
  'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
  '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
  'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
  'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
  'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
  'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
  '-----END CERTIFICATE-----';

let caPem = '-----BEGIN CERTIFICATE-----\n' +
'MIIC/zCCAeegAwIBAgIBATANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
'IENBMB4XDTI0MDMxOTAyMDIyNFoXDTM0MDMxNzAyMDIyNFowEjEQMA4GA1UEAwwH\n' +
'Um9vdCBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALxI5SDvRfKU\n' +
'6XaTeyh2LHlUK0rVSeYfXkYf5Mc3Pgucg+ewzQjxkACMx5NYaW1zfGDNPG1i5IZl\n' +
'cPeWNz1Tm2g6wTd+LyNoNOOmwfLV8pLXSfAukgNrBREf3BzVrbu7hvPd2MmLH23H\n' +
'OBM9uDPTIqu3n2CDN2EzwULjaSk2g+jvhVKsDLInu5uKPmZBFhs1FWKgcnVnlbi1\n' +
'AyAx4efheits6EO70oV6UufCEtS1VsBXQHZRAG4ogshWldRBVNxkU6yHAfg0mM/5\n' +
'EhrZsfh51fWqlrhNWrInjgNV3xIt5ebTIgKZWUlSVHEA/UqDoGfY+CsAJdteZWOW\n' +
'KjsrC/DK2O0CAwEAAaNgMF4wHQYDVR0OBBYEFHRb+SgJu8O0UYdRBkszePocqxbY\n' +
'MB8GA1UdIwQYMBaAFHRb+SgJu8O0UYdRBkszePocqxbYMA8GA1UdEwEB/wQFMAMB\n' +
'Af8wCwYDVR0PBAQDAgEGMA0GCSqGSIb3DQEBCwUAA4IBAQAKOT1ObfQNMN2wdfHq\n' +
'PQgFDDp6rBMbZe70LswPirSXljo4S/vfbG+gBoWCdu/SfsV+lyP75kg1wX0IQvzW\n' +
'xYNh864dgqPmGd0v8TIfM0UT0PpnowUyBHQ+E7LNYIOh/kjHbl3oERdEFA2PUyE9\n' +
'j3GLdg8oe/LqhEQCSAlH+v2RQgBZ9eVN+mSdUxwywm9U3acb0uqVkGiWK/ywumpg\n' +
'AmIZLMJtMVvg8uDkfy16Z4lChTEdNaJVUqPczUNk2kHXIF4we4be9HoOuTVz/SD/\n' +
'IsOhXn/BjS3jnhyS9fxo+opJf9zVTWI02Hlh1WVVtH/m3nIZblyAJhcjCHA2wZSz\n' +
'sSus\n' +
'-----END CERTIFICATE-----';

async function createX509Cert(certData: string): Promise<cert.X509Cert> {
  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509Cert;
}

async function buildX509CertChain() {
  try {
    const caCert = await createX509Cert(caPem);
    const x509Cert = await createX509Cert(certPem);
    let certCrlCollection = cert.createCertCRLCollection([x509Cert]);
    let param: cert.CertChainBuildParameters = {
      certMatchParameters: {validDate:'20240812080000Z'},
      maxLength: 3,
      validationParameters: {
        date: '20240812080000Z',
        certCRLs: [certCrlCollection],
        trustAnchors: [{CACert:caCert}, {CACert:caCert}],
      }
    let certChainBuildResult = await cert.buildX509CertChain(param);
    console.info("cert issuer name: " + certChainBuildResult.validationResult.entityCert.getIssuerName().data)
    console.info("ca subject name: " + certChainBuildResult.validationResult.trustAnchor.CACert?.getSubjectName().data)
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
}

buildX509CertChain();
```

#### cert.parsePkcs1218+

parsePkcs12(data: Uint8Array, config: Pkcs12ParsingConfig): Pkcs12Data

表示从P12文件中解析证书、私钥及其他证书合集，并返回结果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | P12文件，DER格式。 |
| config | Pkcs12ParsingConfig | 是 | P12文件的解析配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Pkcs12Data | 表示P12文件解析后的证书、私钥及其他证书合集。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030008 | maybe wrong password. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

function doTestParsePkcs12() {
  try {
    let p12_cert =
      new Uint8Array([0x30, 0x82, 0x09, 0x51, 0x02, 0x01, 0x03, 0x30, 0x82, 0x09, 0x17, 0x06, 0x09, 0x2a, 0x86, 0x48,
      0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x09, 0x08, 0x04, 0x82, 0x09, 0x04, 0x30, 0x82,
      0x09, 0x00, 0x30, 0x82, 0x03, 0xb7, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07,
      0x06, 0xa0, 0x82, 0x03, 0xa8, 0x30, 0x82, 0x03, 0xa4, 0x02, 0x01, 0x00, 0x30, 0x82, 0x03, 0x9d,
      0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0x30, 0x1c, 0x06, 0x0a, 0x2a,
      0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x01, 0x06, 0x30, 0x0e, 0x04, 0x08, 0x7c, 0xd8, 0x60,
      0x3a, 0x07, 0xfb, 0x87, 0x8b, 0x02, 0x02, 0x08, 0x00, 0x80, 0x82, 0x03, 0x70, 0x4d, 0x64, 0xbe,
      0x82, 0xc2, 0x59, 0x58, 0x65, 0xf0, 0x37, 0x46, 0x4f, 0x6b, 0xfa, 0x43, 0x2e, 0x9d, 0xd9, 0x4f,
      0xd3, 0x54, 0x71, 0x69, 0x6e, 0x03, 0xf8, 0xb8, 0xf9, 0x05, 0xa2, 0x70, 0xa8, 0x70, 0xfb, 0xe6,
      0xda, 0x73, 0xdb, 0x4e, 0xdf, 0x72, 0xcd, 0xb6, 0x88, 0x81, 0xec, 0x3f, 0x8d, 0x7b, 0xdc, 0xa6,
      0x62, 0xd3, 0xd1, 0xdc, 0xef, 0xb9, 0x76, 0xb5, 0xd3, 0xb3, 0xfb, 0x61, 0x50, 0xeb, 0x22, 0x9b,
      0x72, 0x20, 0xb4, 0xe9, 0x7c, 0x5e, 0xaf, 0xa9, 0xb6, 0x40, 0x69, 0x70, 0xea, 0x79, 0x02, 0x1d,
      0x66, 0x71, 0x62, 0x39, 0x31, 0xd3, 0x31, 0xb1, 0x6f, 0x2a, 0x2d, 0x13, 0x59, 0xe9, 0xb7, 0x98,
      0xbe, 0x67, 0xfa, 0x5d, 0x6f, 0x8f, 0x7a, 0x43, 0x10, 0x5a, 0x3f, 0x13, 0xda, 0xb0, 0x94, 0x08,
      0x82, 0xf4, 0x39, 0x1d, 0x42, 0x26, 0x4a, 0xbe, 0x13, 0xe9, 0x89, 0x55, 0x52, 0xa4, 0x16, 0x3d,
      0x50, 0x83, 0x5c, 0xb9, 0x00, 0x5e, 0x03, 0x35, 0x65, 0x13, 0x1f, 0xd8, 0xf8, 0xeb, 0x28, 0xe5,
      0x00, 0x09, 0x9a, 0x62, 0x65, 0xab, 0x28, 0x21, 0x2e, 0x55, 0x11, 0x77, 0x7e, 0x64, 0xae, 0x12,
      0xc1, 0x5e, 0x85, 0xf2, 0xe7, 0xf7, 0x2b, 0x51, 0x46, 0xa6, 0xf8, 0x55, 0x2c, 0xc4, 0x0a, 0x80,
      0x6a, 0xc2, 0xa8, 0xba, 0x94, 0xf8, 0xee, 0x18, 0xf7, 0x32, 0x50, 0x53, 0xcc, 0x1e, 0x53, 0x85,
      0xeb, 0x0d, 0x1e, 0xec, 0xe2, 0xbb, 0xc2, 0xf3, 0xf7, 0x80, 0xfd, 0x81, 0x63, 0x8f, 0x87, 0x98,
      0x09, 0x47, 0x72, 0xee, 0x2d, 0x5a, 0x18, 0x89, 0x6b, 0x95, 0xef, 0x52, 0xde, 0x4d, 0xf5, 0x48,
      0x2a, 0x38, 0x6f, 0x4b, 0x98, 0x3c, 0x6d, 0x41, 0xdd, 0x1b, 0xfd, 0x65, 0x1b, 0x87, 0x8a, 0xcf,
      0xec, 0x47, 0xe3, 0x7a, 0xa0, 0x56, 0xd9, 0x36, 0x36, 0xcb, 0x17, 0xaa, 0x1b, 0x24, 0x79, 0x96,
      0xc6, 0x60, 0xd4, 0xe4, 0xa8, 0x59, 0x35, 0x5e, 0x4e, 0x00, 0xbf, 0x9a, 0xf5, 0x5c, 0x2a, 0xd7,
      0xd7, 0x92, 0x98, 0x79, 0xad, 0x13, 0xda, 0xea, 0xde, 0xcd, 0x65, 0x81, 0x26, 0xbd, 0x55, 0x0f,
      0xa4, 0x73, 0x54, 0x7b, 0x2f, 0x55, 0x2a, 0x2f, 0xb9, 0x2d, 0x6e, 0x04, 0xc8, 0x37, 0x5e, 0x93,
      0x09, 0xa7, 0x7f, 0xb1, 0x6b, 0x4a, 0x9f, 0xea, 0x59, 0x19, 0x57, 0xd0, 0xc1, 0xa1, 0x6b, 0xaf,
      0x27, 0x2b, 0xac, 0x81, 0xec, 0xcd, 0x2e, 0xa2, 0xa6, 0x08, 0x01, 0xfc, 0xa1, 0xbc, 0xc9, 0xdc,
      0x97, 0xb9, 0x48, 0xa8, 0x65, 0x5d, 0x63, 0xdb, 0x5c, 0x7e, 0x55, 0xe7, 0x47, 0xf2, 0x74, 0x17,
      0x67, 0xfe, 0x56, 0x20, 0x54, 0x65, 0x11, 0xdf, 0xec, 0x75, 0x70, 0x49, 0x59, 0xd1, 0xea, 0x6b,
      0x8f, 0x39, 0xec, 0x5d, 0x81, 0x82, 0x9a, 0xec, 0xce, 0x6c, 0x0c, 0x32, 0x14, 0xbd, 0xef, 0xac,
      0xae, 0x04, 0xd0, 0x75, 0x62, 0xf5, 0x82, 0x16, 0xd1, 0xa8, 0xfb, 0x22, 0x2a, 0xc2, 0xe7, 0x7a,
      0x75, 0x08, 0x59, 0x99, 0x34, 0x3d, 0xd9, 0xd7, 0x66, 0xb8, 0xcd, 0xaa, 0xf4, 0x48, 0xcc, 0x21,
      0x25, 0x83, 0xae, 0xad, 0x55, 0x0e, 0xff, 0x44, 0xf3, 0xcc, 0xd1, 0x89, 0x72, 0x0f, 0x9f, 0xe3,
      0xe5, 0xc7, 0xd4, 0x53, 0x94, 0xd6, 0xfb, 0x35, 0xd5, 0xd8, 0x2f, 0xa7, 0x4b, 0xf9, 0x50, 0x15,
      0x1e, 0x35, 0xfc, 0x3d, 0xca, 0xad, 0xb6, 0x49, 0x16, 0xee, 0xff, 0xd7, 0x8a, 0xcc, 0xf0, 0x96,
      0x11, 0x97, 0x22, 0xf3, 0xf7, 0x7c, 0x7a, 0x50, 0x49, 0x12, 0x68, 0x6e, 0x0e, 0x62, 0x32, 0xc7,
      0xe9, 0xc3, 0xa0, 0x1b, 0xfe, 0x29, 0x8c, 0x46, 0xc2, 0x7e, 0xe1, 0xea, 0xc3, 0xcb, 0x30, 0xaf,
      0xe4, 0x60, 0xe5, 0xa5, 0xa5, 0xb8, 0xf4, 0x16, 0xfa, 0x19, 0xd0, 0x1c, 0x14, 0xce, 0xf9, 0xa8,
      0x0b, 0x3f, 0x87, 0x89, 0xd3, 0xed, 0x9e, 0x16, 0x14, 0xbb, 0xd3, 0x64, 0xeb, 0x00, 0xe7, 0x48,
      0x1f, 0xd4, 0x47, 0xbc, 0xa9, 0x6f, 0x03, 0xe0, 0x0e, 0xaf, 0xb9, 0xad, 0x05, 0xa0, 0x1d, 0xee,
      0x0a, 0xcd, 0x0f, 0xd0, 0xb8, 0xf1, 0x35, 0x80, 0xa7, 0x72, 0xcd, 0x36, 0x8e, 0xce, 0x72, 0xf9,
      0x9f, 0xd5, 0x29, 0xae, 0x02, 0xb7, 0xbe, 0x65, 0xff, 0x38, 0x45, 0xf8, 0x8d, 0x87, 0x2f, 0xf8,
      0xdd, 0xc1, 0x72, 0x17, 0x2b, 0xdd, 0x3e, 0xfe, 0x01, 0xa0, 0x59, 0xb3, 0x19, 0x92, 0xf0, 0x59,
      0xf5, 0x06, 0x77, 0x8b, 0x1a, 0x41, 0x1d, 0x8b, 0x80, 0x74, 0x95, 0x8b, 0x30, 0x03, 0x18, 0xdd,
      0x1e, 0x1b, 0x21, 0x36, 0xdf, 0xde, 0xc3, 0xa2, 0x68, 0xe0, 0x3d, 0x94, 0x37, 0x6b, 0x48, 0xb2,
      0xb9, 0x41, 0x53, 0xd6, 0x65, 0xef, 0x7a, 0x3d, 0xdc, 0x09, 0x17, 0x66, 0xb4, 0x05, 0x58, 0x8a,
      0x5d, 0x2f, 0x40, 0x4a, 0x91, 0x8a, 0xa5, 0xb7, 0x29, 0xfb, 0x37, 0x81, 0x71, 0x77, 0x50, 0x8d,
      0x34, 0x80, 0x7e, 0xab, 0xb9, 0xc8, 0xdc, 0xb7, 0x2c, 0x7e, 0xbc, 0xad, 0x7c, 0x14, 0x5c, 0xf6,
      0x90, 0x88, 0x0e, 0x0d, 0x50, 0x7a, 0x4e, 0xa6, 0x85, 0xe4, 0x2a, 0xe7, 0x67, 0x21, 0x53, 0xbb,
      0x73, 0xd5, 0x30, 0x78, 0xbd, 0x08, 0x2b, 0x42, 0x44, 0x3e, 0x5d, 0x2b, 0x2f, 0x09, 0x8e, 0x82,
      0xc3, 0x5b, 0x9e, 0xd8, 0x20, 0xc6, 0xb7, 0x42, 0xe5, 0xb3, 0x60, 0x0b, 0x9b, 0x01, 0x76, 0x26,
      0xf7, 0xc1, 0xf7, 0xe1, 0xd1, 0x46, 0xf7, 0x9c, 0x21, 0xfd, 0x66, 0xb7, 0x14, 0x1d, 0x89, 0xb5,
      0xd3, 0xa1, 0x4e, 0x57, 0x97, 0xe7, 0xe4, 0x63, 0x96, 0xe2, 0x6f, 0x10, 0x6a, 0xb7, 0x8e, 0x83,
      0x64, 0x22, 0x10, 0x02, 0x27, 0x87, 0x6d, 0xb6, 0x11, 0x51, 0xe9, 0xe6, 0x68, 0x1a, 0xc8, 0xd3,
      0x6b, 0x23, 0x33, 0x68, 0x66, 0xab, 0x4d, 0xf9, 0x92, 0x11, 0x67, 0x9d, 0x24, 0xee, 0x18, 0xa8,
      0x3c, 0x5a, 0xfe, 0x79, 0x76, 0x99, 0xeb, 0x9f, 0x19, 0x9d, 0x74, 0xee, 0x13, 0xd9, 0xb1, 0x7b,
      0x4e, 0xcf, 0x30, 0x05, 0xdb, 0x5a, 0x3e, 0x00, 0x7e, 0x0a, 0xed, 0x6f, 0xaf, 0x0d, 0x1b, 0xf3,
      0x61, 0x24, 0x06, 0xe7, 0xf2, 0x57, 0x72, 0xf8, 0x61, 0x4d, 0x5f, 0x00, 0x78, 0x1f, 0x4d, 0xc7,
      0x28, 0x5e, 0xc4, 0x9b, 0xed, 0xac, 0x4f, 0x16, 0xaf, 0x81, 0x85, 0x33, 0x16, 0xbd, 0x6a, 0xb9,
      0xb2, 0x8e, 0x25, 0xbc, 0xaf, 0xfd, 0xea, 0xb7, 0x20, 0x32, 0x15, 0x62, 0x77, 0x52, 0xa1, 0xf2,
      0xd0, 0x9d, 0x12, 0x4c, 0x85, 0x71, 0x08, 0x03, 0xa7, 0x94, 0x34, 0xb4, 0x96, 0x30, 0x82, 0x05,
      0x41, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x05, 0x32,
      0x04, 0x82, 0x05, 0x2e, 0x30, 0x82, 0x05, 0x2a, 0x30, 0x82, 0x05, 0x26, 0x06, 0x0b, 0x2a, 0x86,
      0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x0a, 0x01, 0x02, 0xa0, 0x82, 0x04, 0xee, 0x30, 0x82, 0x04,
      0xea, 0x30, 0x1c, 0x06, 0x0a, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x01, 0x03, 0x30,
      0x0e, 0x04, 0x08, 0x30, 0xee, 0xbd, 0x7c, 0xcb, 0xb5, 0xa5, 0x1b, 0x02, 0x02, 0x08, 0x00, 0x04,
      0x82, 0x04, 0xc8, 0x1e, 0xd0, 0x7f, 0x7e, 0x86, 0x1c, 0x6f, 0x0e, 0xac, 0x6c, 0xe3, 0x35, 0xcb,
      0xff, 0xe4, 0x84, 0x88, 0x97, 0x45, 0xf3, 0x48, 0xa9, 0x98, 0xeb, 0x74, 0x91, 0x53, 0x07, 0x7a,
      0xe4, 0x78, 0x89, 0x13, 0xe7, 0xce, 0xa3, 0xc5, 0xab, 0x2c, 0x16, 0xe5, 0x02, 0x64, 0xc6, 0xb5,
      0x11, 0x36, 0x69, 0x0b, 0x5f, 0x7e, 0x95, 0x27, 0x59, 0x9a, 0xac, 0x98, 0x12, 0x76, 0x39, 0x31,
      0xaa, 0x4f, 0x22, 0x55, 0x21, 0x71, 0x20, 0xeb, 0x4e, 0x5e, 0x2d, 0xd8, 0xab, 0xd9, 0x64, 0x38,
      0x13, 0x9a, 0x14, 0x48, 0x7f, 0x48, 0x05, 0xec, 0x49, 0x55, 0x80, 0x49, 0xaf, 0x4e, 0x29, 0xdf,
      0x4a, 0xfb, 0xa1, 0x20, 0x2f, 0x98, 0x35, 0xf7, 0x8f, 0xb9, 0x41, 0x8b, 0x00, 0x14, 0x23, 0x9a,
      0x43, 0xfe, 0x55, 0xfc, 0xe5, 0x57, 0x19, 0xa9, 0x74, 0x44, 0x1f, 0xdd, 0xc3, 0xc8, 0x9f, 0xfa,
      0x9f, 0x67, 0x93, 0xed, 0x79, 0x11, 0xe1, 0x4e, 0xed, 0xd6, 0x20, 0x82, 0xc8, 0x85, 0xdf, 0x4e,
      0xa0, 0xcd, 0xd8, 0x36, 0x37, 0x4f, 0x67, 0x9d, 0x84, 0x44, 0x14, 0xce, 0xc0, 0xc9, 0xa6, 0xbd,
      0x73, 0x06, 0x27, 0xb7, 0x16, 0x97, 0x8c, 0x61, 0xd9, 0x63, 0xb2, 0x56, 0x8d, 0x28, 0x9e, 0x2e,
      0xcf, 0xa3, 0xfe, 0x8d, 0xaa, 0xef, 0x69, 0x32, 0x7b, 0x32, 0xbe, 0xd5, 0x62, 0x2c, 0x2e, 0x7f,
      0x72, 0xdb, 0x3c, 0x4b, 0xe4, 0x76, 0xa3, 0xa9, 0xa1, 0x67, 0x84, 0x86, 0xea, 0x14, 0x15, 0x6c,
      0x74, 0xd2, 0xac, 0x0e, 0xe2, 0x54, 0x54, 0xd4, 0x31, 0xa3, 0x88, 0x66, 0x89, 0x31, 0x7b, 0xf7,
      0x3c, 0x92, 0xce, 0x3e, 0x86, 0xfb, 0x57, 0xc8, 0x65, 0xae, 0x85, 0x6d, 0x48, 0xf6, 0xe6, 0x37,
      0xeb, 0x77, 0xcf, 0x06, 0xd6, 0x9e, 0x54, 0xb4, 0xd8, 0x9a, 0x5f, 0xdd, 0xc5, 0xa5, 0x05, 0xa0,
      0x4b, 0xd1, 0x54, 0xab, 0x4f, 0xd0, 0x3e, 0x6b, 0x8f, 0x03, 0x66, 0xd4, 0xe2, 0x90, 0xea, 0x2d,
      0x9b, 0x6a, 0x2b, 0xc4, 0x7b, 0x9d, 0xf1, 0xb5, 0x22, 0xdf, 0x86, 0xc2, 0xfd, 0x13, 0x0a, 0x69,
      0x29, 0x59, 0xe9, 0x45, 0xcd, 0xdf, 0xcd, 0xa5, 0x71, 0x7e, 0x70, 0xc3, 0x60, 0x9e, 0x47, 0x5d,
      0xd4, 0x6c, 0xcc, 0x15, 0x51, 0x23, 0x5b, 0x4e, 0xee, 0x72, 0x80, 0x49, 0xd6, 0xac, 0x89, 0x16,
      0x65, 0xf4, 0x95, 0x57, 0x19, 0x13, 0xab, 0x9c, 0x08, 0xe8, 0xdf, 0x0a, 0xe2, 0x39, 0xfc, 0xff,
      0x42, 0x02, 0xac, 0xaf, 0xf1, 0xb6, 0x56, 0xef, 0x75, 0x60, 0x2f, 0xc2, 0x5d, 0xef, 0xf5, 0x79,
      0xb5, 0x46, 0xa0, 0xb5, 0x03, 0x67, 0xef, 0x78, 0x3d, 0x49, 0xd0, 0xc5, 0x0e, 0xff, 0x42, 0x72,
      0x02, 0x86, 0x99, 0x93, 0xaa, 0xa3, 0x9e, 0x2c, 0xc7, 0xec, 0xa2, 0xdf, 0x25, 0x4e, 0x28, 0x81,
      0x82, 0x3e, 0x29, 0xd3, 0x37, 0xfd, 0x32, 0xf4, 0x85, 0x46, 0x42, 0xb9, 0x94, 0x44, 0x8a, 0xbf,
      0xd9, 0x14, 0xcb, 0xb6, 0xd3, 0xc5, 0xe7, 0x6b, 0x28, 0x70, 0xc3, 0x9c, 0xc2, 0x93, 0x9d, 0x2f,
      0xab, 0xd6, 0xb2, 0x19, 0x28, 0x9a, 0xda, 0x0d, 0x90, 0x5b, 0xba, 0x64, 0x6f, 0xcc, 0x11, 0xef,
      0x6c, 0x88, 0x18, 0x4f, 0x86, 0x6e, 0xed, 0xcf, 0xde, 0x0d, 0xec, 0xe2, 0x12, 0xc3, 0x89, 0x0a,
      0x3f, 0xbb, 0x3d, 0x8c, 0x8f, 0xa9, 0x40, 0xe6, 0xf8, 0xd1, 0x1a, 0x9a, 0x7e, 0x8a, 0xd7, 0x7b,
      0x56, 0xf4, 0x5d, 0x80, 0x64, 0xd5, 0x88, 0x86, 0x85, 0x18, 0x30, 0x5d, 0x64, 0x04, 0xb3, 0xc2,
      0xc7, 0x80, 0xda, 0x3e, 0xc4, 0xd6, 0xf6, 0xc4, 0x95, 0x56, 0xd5, 0xad, 0x82, 0x86, 0xcc, 0x1a,
      0x05, 0x69, 0x06, 0x08, 0x5b, 0x19, 0xea, 0x10, 0xc5, 0xcd, 0x67, 0x93, 0xab, 0x0f, 0xe3, 0xba,
      0xb0, 0x0d, 0xac, 0x99, 0x0d, 0x35, 0x6f, 0xe5, 0x41, 0xb2, 0x7c, 0x87, 0x91, 0x6c, 0xe2, 0x75,
      0x9b, 0x64, 0x62, 0x06, 0x2a, 0x8b, 0xd9, 0x4d, 0x23, 0xcd, 0x2b, 0xef, 0xf5, 0x61, 0x82, 0x8e,
      0x3f, 0xf6, 0x2b, 0xe1, 0x6f, 0xcf, 0xbd, 0xaa, 0x07, 0x97, 0x49, 0x4e, 0x02, 0x9d, 0xa5, 0x9e,
      0xc5, 0xd7, 0x8b, 0xd3, 0xe1, 0xd9, 0x35, 0x96, 0x9d, 0x1f, 0xa2, 0xf6, 0x91, 0xee, 0xd1, 0x3b,
      0xa8, 0xfe, 0x4d, 0xeb, 0xf9, 0xfc, 0xe4, 0xab, 0x60, 0xb7, 0x86, 0x9d, 0x2a, 0x35, 0xb0, 0x00,
      0xd4, 0x3c, 0x2a, 0x7e, 0x6d, 0x65, 0x5f, 0xf3, 0x7c, 0x23, 0x57, 0x52, 0x2a, 0x8c, 0x5b, 0x36,
      0x74, 0xb7, 0x61, 0x49, 0xf0, 0xdf, 0xcf, 0x8a, 0x28, 0xc5, 0x8d, 0xbc, 0x20, 0xcc, 0xac, 0x86,
      0x20, 0xd8, 0x2d, 0x86, 0x99, 0xf5, 0xf0, 0xdb, 0xed, 0x8d, 0xf9, 0xd7, 0x4e, 0xa8, 0xde, 0x84,
      0x35, 0x50, 0xc1, 0x7c, 0xbd, 0xdf, 0xc2, 0x24, 0x1a, 0x49, 0x24, 0x9a, 0x37, 0x93, 0xca, 0x2d,
      0x73, 0x47, 0x8f, 0x83, 0xed, 0x4d, 0xca, 0xf8, 0xf0, 0xd3, 0x9b, 0xe0, 0x4b, 0x3b, 0xf1, 0x86,
      0xeb, 0x78, 0x7b, 0x42, 0xa1, 0xb9, 0x36, 0x15, 0xde, 0x63, 0xab, 0x8b, 0x8b, 0x5d, 0xa2, 0x92,
      0x10, 0x95, 0xdf, 0xda, 0xd7, 0xba, 0xa0, 0x26, 0xb9, 0xdc, 0x83, 0xeb, 0xdc, 0xd2, 0x1f, 0xf1,
      0xb1, 0x8d, 0x21, 0x51, 0x71, 0x59, 0x0e, 0xe8, 0x7e, 0xf1, 0x53, 0x08, 0x98, 0x79, 0x05, 0x3b,
      0x22, 0xf1, 0xda, 0x07, 0x0d, 0xf7, 0x89, 0x5e, 0xc4, 0x62, 0x8c, 0xf9, 0x19, 0xc8, 0xbc, 0xa4,
      0x0c, 0x6f, 0x41, 0x34, 0x56, 0x22, 0x6b, 0xe6, 0xee, 0x7c, 0x4a, 0xd9, 0x26, 0x8c, 0x56, 0x12,
      0xf3, 0x03, 0x12, 0x1c, 0x5b, 0x8d, 0x64, 0x5c, 0x1c, 0xb6, 0x0f, 0x93, 0xaf, 0xb1, 0x67, 0x6f,
      0x13, 0xdd, 0xe3, 0xcf, 0x0e, 0xe6, 0x06, 0xf3, 0xb2, 0xbc, 0x99, 0xf5, 0xb0, 0xd7, 0xe9, 0x7e,
      0xb0, 0x6a, 0xb9, 0xb5, 0xda, 0xcf, 0x88, 0xf1, 0xc5, 0x58, 0x54, 0x05, 0x5c, 0x9d, 0x79, 0xc2,
      0xcd, 0xbb, 0xc6, 0xf2, 0x69, 0xa9, 0xe3, 0x4e, 0x05, 0x0d, 0x02, 0xb6, 0x4d, 0x8e, 0x7d, 0x60,
      0x8e, 0xda, 0x4d, 0x28, 0xd2, 0xec, 0x8a, 0x11, 0xe3, 0xe7, 0x17, 0x20, 0x07, 0x7b, 0xfc, 0x9b,
      0x4e, 0xf7, 0x79, 0xf5, 0x0a, 0x6e, 0xd1, 0x1e, 0x7b, 0x83, 0x66, 0x5e, 0x1b, 0x9d, 0x36, 0x32,
      0x89, 0xf6, 0x72, 0xa5, 0x58, 0x54, 0x42, 0xba, 0x90, 0xf3, 0xbb, 0x05, 0x46, 0xa4, 0x91, 0x1c,
      0xdb, 0xab, 0xf3, 0x68, 0x56, 0x7a, 0xd3, 0xff, 0x3f, 0x9f, 0xc5, 0x4a, 0x47, 0xbd, 0x89, 0x46,
      0xf6, 0x94, 0x3a, 0x94, 0xd4, 0x30, 0xd3, 0xae, 0x0d, 0x99, 0x95, 0xf7, 0x75, 0xfe, 0x14, 0x10,
      0x9e, 0xed, 0x21, 0x0f, 0x0d, 0x54, 0x7d, 0x54, 0xc5, 0x80, 0x21, 0x4d, 0xf2, 0xaf, 0x67, 0xaf,
      0x8a, 0x76, 0x9e, 0x34, 0x32, 0x74, 0x89, 0x2a, 0x32, 0xf9, 0x48, 0x20, 0x90, 0xe6, 0x4a, 0xa3,
      0x7f, 0xf2, 0x2a, 0x51, 0x22, 0x93, 0xe5, 0xdd, 0x59, 0xb3, 0x83, 0xa8, 0x47, 0xf5, 0x6b, 0x38,
      0x24, 0xc2, 0xac, 0x2d, 0x03, 0xda, 0xb1, 0x17, 0x19, 0xe0, 0x38, 0x2c, 0xb3, 0xa6, 0x4c, 0x8e,
      0xae, 0x63, 0xa7, 0xae, 0x96, 0xb1, 0x07, 0x8c, 0x8f, 0x6a, 0x08, 0x32, 0x15, 0x1f, 0x33, 0x97,
      0x21, 0x3b, 0x51, 0x70, 0xc5, 0x1f, 0xa6, 0xa3, 0x8a, 0xd0, 0x8f, 0x0b, 0xda, 0x64, 0xab, 0xbe,
      0xee, 0x4b, 0x14, 0xfd, 0x32, 0x87, 0x9e, 0xa7, 0x19, 0x75, 0xc9, 0xaa, 0xd3, 0xed, 0xa7, 0xa0,
      0x01, 0xe7, 0xa0, 0xe5, 0x28, 0xdd, 0x3b, 0x7c, 0x49, 0xe4, 0x24, 0x7d, 0x92, 0x86, 0x25, 0x03,
      0xb3, 0x66, 0x04, 0xf3, 0xa1, 0x40, 0x11, 0x35, 0x3a, 0x1d, 0xbf, 0x1c, 0x02, 0x83, 0x3d, 0x37,
      0x51, 0x88, 0xa3, 0x2b, 0x10, 0x8c, 0x8e, 0x10, 0xdd, 0xdc, 0xef, 0xa4, 0xe9, 0x14, 0x77, 0xb6,
      0x8e, 0x75, 0xb6, 0x8e, 0xea, 0xaa, 0x57, 0x16, 0x1f, 0xb0, 0x0c, 0xbc, 0x44, 0xed, 0x92, 0x94,
      0x9a, 0xb4, 0xf3, 0x31, 0x64, 0x02, 0x5c, 0xa1, 0x51, 0x63, 0x39, 0x42, 0x74, 0x7a, 0x1d, 0xf2,
      0xf5, 0x92, 0x50, 0xf1, 0x5a, 0x8a, 0xde, 0xb3, 0x4e, 0xf1, 0x6e, 0x67, 0xd9, 0x5b, 0x00, 0xa7,
      0xd1, 0x90, 0x58, 0x36, 0xc4, 0x15, 0x80, 0xbb, 0xa5, 0xbb, 0x98, 0xc0, 0x8a, 0x9b, 0x17, 0x35,
      0x36, 0x3b, 0x62, 0x0f, 0x29, 0xcd, 0xe9, 0x04, 0x0e, 0x9d, 0xca, 0x43, 0x04, 0xdf, 0x17, 0x49,
      0xbf, 0xb6, 0x7a, 0x7a, 0x3c, 0xdb, 0x0d, 0x6d, 0xd5, 0x89, 0xb9, 0x69, 0x94, 0xd8, 0xb2, 0xd6,
      0x38, 0x8a, 0xcc, 0x78, 0x44, 0x40, 0x63, 0x9f, 0x1e, 0x0e, 0x40, 0x33, 0x51, 0xd3, 0x65, 0xf8,
      0xf1, 0x42, 0x06, 0x75, 0x84, 0xe7, 0xb1, 0xe9, 0xd6, 0xa4, 0x5e, 0x7f, 0xb0, 0x48, 0x6f, 0x80,
      0x92, 0xf8, 0xfc, 0x2a, 0xdb, 0x18, 0x97, 0xe5, 0xe7, 0xc7, 0x46, 0xb6, 0x59, 0x8c, 0x3a, 0x09,
      0x91, 0xc1, 0x49, 0x55, 0xf9, 0xf3, 0x87, 0x19, 0xdc, 0x72, 0x56, 0xd3, 0x20, 0x5e, 0xc5, 0x3d,
      0xfb, 0x19, 0xea, 0x6a, 0xdf, 0x09, 0xb2, 0x8f, 0xb6, 0xdd, 0x26, 0x31, 0x25, 0x30, 0x23, 0x06,
      0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x15, 0x31, 0x16, 0x04, 0x14, 0x3b, 0xd2,
      0xb3, 0x51, 0x4c, 0x57, 0xd0, 0xca, 0x34, 0xa4, 0xf0, 0x06, 0xdd, 0xe9, 0x76, 0x08, 0xdb, 0x7b,
      0x3a, 0xb0, 0x30, 0x31, 0x30, 0x21, 0x30, 0x09, 0x06, 0x05, 0x2b, 0x0e, 0x03, 0x02, 0x1a, 0x05,
      0x00, 0x04, 0x14, 0x8e, 0x7f, 0x87, 0x67, 0x78, 0x64, 0x93, 0x36, 0x35, 0xe5, 0x93, 0x9d, 0xac,
      0x61, 0x09, 0x4f, 0xdc, 0x95, 0xd7, 0x4f, 0x04, 0x08, 0x23, 0xc2, 0xc0, 0xc6, 0x8d, 0x5f, 0x70,
      0x7e, 0x02, 0x02, 0x08, 0x00]);

    let conf: cert.Pkcs12ParsingConfig = {
      password: '123456',
      needsCert: false,
      needsPrivateKey: true,
      privateKeyFormat: cert.EncodingBaseFormat.DER,
      needsOtherCerts: false,
    };
    let p12: cert.Pkcs12Data = cert.parsePkcs12(p12_cert, conf);
    console.info('parsePKCS12 result: success.');
    if (p12.privateKey) {
      console.info('privateKey:' + p12.privateKey.toString())
    }
  } catch (error) {
    console.error(`parsePKCS12 failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### cert.parsePkcs1221+

parsePkcs12(data: Uint8Array, password: string): Promise<Pkcs12Data>

表示从Pkcs12文件中解析证书、私钥及其他证书合集。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | Pkcs12文件，DER格式。 |
| password | string | 是 | Pkcs12的密码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Pkcs12Data> | Promise对象，返回Pkcs12文件解析后的证书、私钥及其他证书合集。返回的Pkcs12Data中的私钥采用PEM格式编码。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The length of the data is zero or too large; 2. The length of the password is zero or too large. |
| 19030001 | crypto operation error. |
| 19030008 | maybe wrong password. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

async function doTestParsePkcs12() {
  try {
    let p12_cert =
      new Uint8Array([0x30, 0x82, 0x09, 0x51, 0x02, 0x01, 0x03, 0x30, 0x82, 0x09, 0x17, 0x06, 0x09, 0x2a, 0x86, 0x48,
      0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x09, 0x08, 0x04, 0x82, 0x09, 0x04, 0x30, 0x82,
      0x09, 0x00, 0x30, 0x82, 0x03, 0xb7, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07,
      0x06, 0xa0, 0x82, 0x03, 0xa8, 0x30, 0x82, 0x03, 0xa4, 0x02, 0x01, 0x00, 0x30, 0x82, 0x03, 0x9d,
      0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0x30, 0x1c, 0x06, 0x0a, 0x2a,
      0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x01, 0x06, 0x30, 0x0e, 0x04, 0x08, 0x7c, 0xd8, 0x60,
      0x3a, 0x07, 0xfb, 0x87, 0x8b, 0x02, 0x02, 0x08, 0x00, 0x80, 0x82, 0x03, 0x70, 0x4d, 0x64, 0xbe,
      0x82, 0xc2, 0x59, 0x58, 0x65, 0xf0, 0x37, 0x46, 0x4f, 0x6b, 0xfa, 0x43, 0x2e, 0x9d, 0xd9, 0x4f,
      0xd3, 0x54, 0x71, 0x69, 0x6e, 0x03, 0xf8, 0xb8, 0xf9, 0x05, 0xa2, 0x70, 0xa8, 0x70, 0xfb, 0xe6,
      0xda, 0x73, 0xdb, 0x4e, 0xdf, 0x72, 0xcd, 0xb6, 0x88, 0x81, 0xec, 0x3f, 0x8d, 0x7b, 0xdc, 0xa6,
      0x62, 0xd3, 0xd1, 0xdc, 0xef, 0xb9, 0x76, 0xb5, 0xd3, 0xb3, 0xfb, 0x61, 0x50, 0xeb, 0x22, 0x9b,
      0x72, 0x20, 0xb4, 0xe9, 0x7c, 0x5e, 0xaf, 0xa9, 0xb6, 0x40, 0x69, 0x70, 0xea, 0x79, 0x02, 0x1d,
      0x66, 0x71, 0x62, 0x39, 0x31, 0xd3, 0x31, 0xb1, 0x6f, 0x2a, 0x2d, 0x13, 0x59, 0xe9, 0xb7, 0x98,
      0xbe, 0x67, 0xfa, 0x5d, 0x6f, 0x8f, 0x7a, 0x43, 0x10, 0x5a, 0x3f, 0x13, 0xda, 0xb0, 0x94, 0x08,
      0x82, 0xf4, 0x39, 0x1d, 0x42, 0x26, 0x4a, 0xbe, 0x13, 0xe9, 0x89, 0x55, 0x52, 0xa4, 0x16, 0x3d,
      0x50, 0x83, 0x5c, 0xb9, 0x00, 0x5e, 0x03, 0x35, 0x65, 0x13, 0x1f, 0xd8, 0xf8, 0xeb, 0x28, 0xe5,
      0x00, 0x09, 0x9a, 0x62, 0x65, 0xab, 0x28, 0x21, 0x2e, 0x55, 0x11, 0x77, 0x7e, 0x64, 0xae, 0x12,
      0xc1, 0x5e, 0x85, 0xf2, 0xe7, 0xf7, 0x2b, 0x51, 0x46, 0xa6, 0xf8, 0x55, 0x2c, 0xc4, 0x0a, 0x80,
      0x6a, 0xc2, 0xa8, 0xba, 0x94, 0xf8, 0xee, 0x18, 0xf7, 0x32, 0x50, 0x53, 0xcc, 0x1e, 0x53, 0x85,
      0xeb, 0x0d, 0x1e, 0xec, 0xe2, 0xbb, 0xc2, 0xf3, 0xf7, 0x80, 0xfd, 0x81, 0x63, 0x8f, 0x87, 0x98,
      0x09, 0x47, 0x72, 0xee, 0x2d, 0x5a, 0x18, 0x89, 0x6b, 0x95, 0xef, 0x52, 0xde, 0x4d, 0xf5, 0x48,
      0x2a, 0x38, 0x6f, 0x4b, 0x98, 0x3c, 0x6d, 0x41, 0xdd, 0x1b, 0xfd, 0x65, 0x1b, 0x87, 0x8a, 0xcf,
      0xec, 0x47, 0xe3, 0x7a, 0xa0, 0x56, 0xd9, 0x36, 0x36, 0xcb, 0x17, 0xaa, 0x1b, 0x24, 0x79, 0x96,
      0xc6, 0x60, 0xd4, 0xe4, 0xa8, 0x59, 0x35, 0x5e, 0x4e, 0x00, 0xbf, 0x9a, 0xf5, 0x5c, 0x2a, 0xd7,
      0xd7, 0x92, 0x98, 0x79, 0xad, 0x13, 0xda, 0xea, 0xde, 0xcd, 0x65, 0x81, 0x26, 0xbd, 0x55, 0x0f,
      0xa4, 0x73, 0x54, 0x7b, 0x2f, 0x55, 0x2a, 0x2f, 0xb9, 0x2d, 0x6e, 0x04, 0xc8, 0x37, 0x5e, 0x93,
      0x09, 0xa7, 0x7f, 0xb1, 0x6b, 0x4a, 0x9f, 0xea, 0x59, 0x19, 0x57, 0xd0, 0xc1, 0xa1, 0x6b, 0xaf,
      0x27, 0x2b, 0xac, 0x81, 0xec, 0xcd, 0x2e, 0xa2, 0xa6, 0x08, 0x01, 0xfc, 0xa1, 0xbc, 0xc9, 0xdc,
      0x97, 0xb9, 0x48, 0xa8, 0x65, 0x5d, 0x63, 0xdb, 0x5c, 0x7e, 0x55, 0xe7, 0x47, 0xf2, 0x74, 0x17,
      0x67, 0xfe, 0x56, 0x20, 0x54, 0x65, 0x11, 0xdf, 0xec, 0x75, 0x70, 0x49, 0x59, 0xd1, 0xea, 0x6b,
      0x8f, 0x39, 0xec, 0x5d, 0x81, 0x82, 0x9a, 0xec, 0xce, 0x6c, 0x0c, 0x32, 0x14, 0xbd, 0xef, 0xac,
      0xae, 0x04, 0xd0, 0x75, 0x62, 0xf5, 0x82, 0x16, 0xd1, 0xa8, 0xfb, 0x22, 0x2a, 0xc2, 0xe7, 0x7a,
      0x75, 0x08, 0x59, 0x99, 0x34, 0x3d, 0xd9, 0xd7, 0x66, 0xb8, 0xcd, 0xaa, 0xf4, 0x48, 0xcc, 0x21,
      0x25, 0x83, 0xae, 0xad, 0x55, 0x0e, 0xff, 0x44, 0xf3, 0xcc, 0xd1, 0x89, 0x72, 0x0f, 0x9f, 0xe3,
      0xe5, 0xc7, 0xd4, 0x53, 0x94, 0xd6, 0xfb, 0x35, 0xd5, 0xd8, 0x2f, 0xa7, 0x4b, 0xf9, 0x50, 0x15,
      0x1e, 0x35, 0xfc, 0x3d, 0xca, 0xad, 0xb6, 0x49, 0x16, 0xee, 0xff, 0xd7, 0x8a, 0xcc, 0xf0, 0x96,
      0x11, 0x97, 0x22, 0xf3, 0xf7, 0x7c, 0x7a, 0x50, 0x49, 0x12, 0x68, 0x6e, 0x0e, 0x62, 0x32, 0xc7,
      0xe9, 0xc3, 0xa0, 0x1b, 0xfe, 0x29, 0x8c, 0x46, 0xc2, 0x7e, 0xe1, 0xea, 0xc3, 0xcb, 0x30, 0xaf,
      0xe4, 0x60, 0xe5, 0xa5, 0xa5, 0xb8, 0xf4, 0x16, 0xfa, 0x19, 0xd0, 0x1c, 0x14, 0xce, 0xf9, 0xa8,
      0x0b, 0x3f, 0x87, 0x89, 0xd3, 0xed, 0x9e, 0x16, 0x14, 0xbb, 0xd3, 0x64, 0xeb, 0x00, 0xe7, 0x48,
      0x1f, 0xd4, 0x47, 0xbc, 0xa9, 0x6f, 0x03, 0xe0, 0x0e, 0xaf, 0xb9, 0xad, 0x05, 0xa0, 0x1d, 0xee,
      0x0a, 0xcd, 0x0f, 0xd0, 0xb8, 0xf1, 0x35, 0x80, 0xa7, 0x72, 0xcd, 0x36, 0x8e, 0xce, 0x72, 0xf9,
      0x9f, 0xd5, 0x29, 0xae, 0x02, 0xb7, 0xbe, 0x65, 0xff, 0x38, 0x45, 0xf8, 0x8d, 0x87, 0x2f, 0xf8,
      0xdd, 0xc1, 0x72, 0x17, 0x2b, 0xdd, 0x3e, 0xfe, 0x01, 0xa0, 0x59, 0xb3, 0x19, 0x92, 0xf0, 0x59,
      0xf5, 0x06, 0x77, 0x8b, 0x1a, 0x41, 0x1d, 0x8b, 0x80, 0x74, 0x95, 0x8b, 0x30, 0x03, 0x18, 0xdd,
      0x1e, 0x1b, 0x21, 0x36, 0xdf, 0xde, 0xc3, 0xa2, 0x68, 0xe0, 0x3d, 0x94, 0x37, 0x6b, 0x48, 0xb2,
      0xb9, 0x41, 0x53, 0xd6, 0x65, 0xef, 0x7a, 0x3d, 0xdc, 0x09, 0x17, 0x66, 0xb4, 0x05, 0x58, 0x8a,
      0x5d, 0x2f, 0x40, 0x4a, 0x91, 0x8a, 0xa5, 0xb7, 0x29, 0xfb, 0x37, 0x81, 0x71, 0x77, 0x50, 0x8d,
      0x34, 0x80, 0x7e, 0xab, 0xb9, 0xc8, 0xdc, 0xb7, 0x2c, 0x7e, 0xbc, 0xad, 0x7c, 0x14, 0x5c, 0xf6,
      0x90, 0x88, 0x0e, 0x0d, 0x50, 0x7a, 0x4e, 0xa6, 0x85, 0xe4, 0x2a, 0xe7, 0x67, 0x21, 0x53, 0xbb,
      0x73, 0xd5, 0x30, 0x78, 0xbd, 0x08, 0x2b, 0x42, 0x44, 0x3e, 0x5d, 0x2b, 0x2f, 0x09, 0x8e, 0x82,
      0xc3, 0x5b, 0x9e, 0xd8, 0x20, 0xc6, 0xb7, 0x42, 0xe5, 0xb3, 0x60, 0x0b, 0x9b, 0x01, 0x76, 0x26,
      0xf7, 0xc1, 0xf7, 0xe1, 0xd1, 0x46, 0xf7, 0x9c, 0x21, 0xfd, 0x66, 0xb7, 0x14, 0x1d, 0x89, 0xb5,
      0xd3, 0xa1, 0x4e, 0x57, 0x97, 0xe7, 0xe4, 0x63, 0x96, 0xe2, 0x6f, 0x10, 0x6a, 0xb7, 0x8e, 0x83,
      0x64, 0x22, 0x10, 0x02, 0x27, 0x87, 0x6d, 0xb6, 0x11, 0x51, 0xe9, 0xe6, 0x68, 0x1a, 0xc8, 0xd3,
      0x6b, 0x23, 0x33, 0x68, 0x66, 0xab, 0x4d, 0xf9, 0x92, 0x11, 0x67, 0x9d, 0x24, 0xee, 0x18, 0xa8,
      0x3c, 0x5a, 0xfe, 0x79, 0x76, 0x99, 0xeb, 0x9f, 0x19, 0x9d, 0x74, 0xee, 0x13, 0xd9, 0xb1, 0x7b,
      0x4e, 0xcf, 0x30, 0x05, 0xdb, 0x5a, 0x3e, 0x00, 0x7e, 0x0a, 0xed, 0x6f, 0xaf, 0x0d, 0x1b, 0xf3,
      0x61, 0x24, 0x06, 0xe7, 0xf2, 0x57, 0x72, 0xf8, 0x61, 0x4d, 0x5f, 0x00, 0x78, 0x1f, 0x4d, 0xc7,
      0x28, 0x5e, 0xc4, 0x9b, 0xed, 0xac, 0x4f, 0x16, 0xaf, 0x81, 0x85, 0x33, 0x16, 0xbd, 0x6a, 0xb9,
      0xb2, 0x8e, 0x25, 0xbc, 0xaf, 0xfd, 0xea, 0xb7, 0x20, 0x32, 0x15, 0x62, 0x77, 0x52, 0xa1, 0xf2,
      0xd0, 0x9d, 0x12, 0x4c, 0x85, 0x71, 0x08, 0x03, 0xa7, 0x94, 0x34, 0xb4, 0x96, 0x30, 0x82, 0x05,
      0x41, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x05, 0x32,
      0x04, 0x82, 0x05, 0x2e, 0x30, 0x82, 0x05, 0x2a, 0x30, 0x82, 0x05, 0x26, 0x06, 0x0b, 0x2a, 0x86,
      0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x0a, 0x01, 0x02, 0xa0, 0x82, 0x04, 0xee, 0x30, 0x82, 0x04,
      0xea, 0x30, 0x1c, 0x06, 0x0a, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x0c, 0x01, 0x03, 0x30,
      0x0e, 0x04, 0x08, 0x30, 0xee, 0xbd, 0x7c, 0xcb, 0xb5, 0xa5, 0x1b, 0x02, 0x02, 0x08, 0x00, 0x04,
      0x82, 0x04, 0xc8, 0x1e, 0xd0, 0x7f, 0x7e, 0x86, 0x1c, 0x6f, 0x0e, 0xac, 0x6c, 0xe3, 0x35, 0xcb,
      0xff, 0xe4, 0x84, 0x88, 0x97, 0x45, 0xf3, 0x48, 0xa9, 0x98, 0xeb, 0x74, 0x91, 0x53, 0x07, 0x7a,
      0xe4, 0x78, 0x89, 0x13, 0xe7, 0xce, 0xa3, 0xc5, 0xab, 0x2c, 0x16, 0xe5, 0x02, 0x64, 0xc6, 0xb5,
      0x11, 0x36, 0x69, 0x0b, 0x5f, 0x7e, 0x95, 0x27, 0x59, 0x9a, 0xac, 0x98, 0x12, 0x76, 0x39, 0x31,
      0xaa, 0x4f, 0x22, 0x55, 0x21, 0x71, 0x20, 0xeb, 0x4e, 0x5e, 0x2d, 0xd8, 0xab, 0xd9, 0x64, 0x38,
      0x13, 0x9a, 0x14, 0x48, 0x7f, 0x48, 0x05, 0xec, 0x49, 0x55, 0x80, 0x49, 0xaf, 0x4e, 0x29, 0xdf,
      0x4a, 0xfb, 0xa1, 0x20, 0x2f, 0x98, 0x35, 0xf7, 0x8f, 0xb9, 0x41, 0x8b, 0x00, 0x14, 0x23, 0x9a,
      0x43, 0xfe, 0x55, 0xfc, 0xe5, 0x57, 0x19, 0xa9, 0x74, 0x44, 0x1f, 0xdd, 0xc3, 0xc8, 0x9f, 0xfa,
      0x9f, 0x67, 0x93, 0xed, 0x79, 0x11, 0xe1, 0x4e, 0xed, 0xd6, 0x20, 0x82, 0xc8, 0x85, 0xdf, 0x4e,
      0xa0, 0xcd, 0xd8, 0x36, 0x37, 0x4f, 0x67, 0x9d, 0x84, 0x44, 0x14, 0xce, 0xc0, 0xc9, 0xa6, 0xbd,
      0x73, 0x06, 0x27, 0xb7, 0x16, 0x97, 0x8c, 0x61, 0xd9, 0x63, 0xb2, 0x56, 0x8d, 0x28, 0x9e, 0x2e,
      0xcf, 0xa3, 0xfe, 0x8d, 0xaa, 0xef, 0x69, 0x32, 0x7b, 0x32, 0xbe, 0xd5, 0x62, 0x2c, 0x2e, 0x7f,
      0x72, 0xdb, 0x3c, 0x4b, 0xe4, 0x76, 0xa3, 0xa9, 0xa1, 0x67, 0x84, 0x86, 0xea, 0x14, 0x15, 0x6c,
      0x74, 0xd2, 0xac, 0x0e, 0xe2, 0x54, 0x54, 0xd4, 0x31, 0xa3, 0x88, 0x66, 0x89, 0x31, 0x7b, 0xf7,
      0x3c, 0x92, 0xce, 0x3e, 0x86, 0xfb, 0x57, 0xc8, 0x65, 0xae, 0x85, 0x6d, 0x48, 0xf6, 0xe6, 0x37,
      0xeb, 0x77, 0xcf, 0x06, 0xd6, 0x9e, 0x54, 0xb4, 0xd8, 0x9a, 0x5f, 0xdd, 0xc5, 0xa5, 0x05, 0xa0,
      0x4b, 0xd1, 0x54, 0xab, 0x4f, 0xd0, 0x3e, 0x6b, 0x8f, 0x03, 0x66, 0xd4, 0xe2, 0x90, 0xea, 0x2d,
      0x9b, 0x6a, 0x2b, 0xc4, 0x7b, 0x9d, 0xf1, 0xb5, 0x22, 0xdf, 0x86, 0xc2, 0xfd, 0x13, 0x0a, 0x69,
      0x29, 0x59, 0xe9, 0x45, 0xcd, 0xdf, 0xcd, 0xa5, 0x71, 0x7e, 0x70, 0xc3, 0x60, 0x9e, 0x47, 0x5d,
      0xd4, 0x6c, 0xcc, 0x15, 0x51, 0x23, 0x5b, 0x4e, 0xee, 0x72, 0x80, 0x49, 0xd6, 0xac, 0x89, 0x16,
      0x65, 0xf4, 0x95, 0x57, 0x19, 0x13, 0xab, 0x9c, 0x08, 0xe8, 0xdf, 0x0a, 0xe2, 0x39, 0xfc, 0xff,
      0x42, 0x02, 0xac, 0xaf, 0xf1, 0xb6, 0x56, 0xef, 0x75, 0x60, 0x2f, 0xc2, 0x5d, 0xef, 0xf5, 0x79,
      0xb5, 0x46, 0xa0, 0xb5, 0x03, 0x67, 0xef, 0x78, 0x3d, 0x49, 0xd0, 0xc5, 0x0e, 0xff, 0x42, 0x72,
      0x02, 0x86, 0x99, 0x93, 0xaa, 0xa3, 0x9e, 0x2c, 0xc7, 0xec, 0xa2, 0xdf, 0x25, 0x4e, 0x28, 0x81,
      0x82, 0x3e, 0x29, 0xd3, 0x37, 0xfd, 0x32, 0xf4, 0x85, 0x46, 0x42, 0xb9, 0x94, 0x44, 0x8a, 0xbf,
      0xd9, 0x14, 0xcb, 0xb6, 0xd3, 0xc5, 0xe7, 0x6b, 0x28, 0x70, 0xc3, 0x9c, 0xc2, 0x93, 0x9d, 0x2f,
      0xab, 0xd6, 0xb2, 0x19, 0x28, 0x9a, 0xda, 0x0d, 0x90, 0x5b, 0xba, 0x64, 0x6f, 0xcc, 0x11, 0xef,
      0x6c, 0x88, 0x18, 0x4f, 0x86, 0x6e, 0xed, 0xcf, 0xde, 0x0d, 0xec, 0xe2, 0x12, 0xc3, 0x89, 0x0a,
      0x3f, 0xbb, 0x3d, 0x8c, 0x8f, 0xa9, 0x40, 0xe6, 0xf8, 0xd1, 0x1a, 0x9a, 0x7e, 0x8a, 0xd7, 0x7b,
      0x56, 0xf4, 0x5d, 0x80, 0x64, 0xd5, 0x88, 0x86, 0x85, 0x18, 0x30, 0x5d, 0x64, 0x04, 0xb3, 0xc2,
      0xc7, 0x80, 0xda, 0x3e, 0xc4, 0xd6, 0xf6, 0xc4, 0x95, 0x56, 0xd5, 0xad, 0x82, 0x86, 0xcc, 0x1a,
      0x05, 0x69, 0x06, 0x08, 0x5b, 0x19, 0xea, 0x10, 0xc5, 0xcd, 0x67, 0x93, 0xab, 0x0f, 0xe3, 0xba,
      0xb0, 0x0d, 0xac, 0x99, 0x0d, 0x35, 0x6f, 0xe5, 0x41, 0xb2, 0x7c, 0x87, 0x91, 0x6c, 0xe2, 0x75,
      0x9b, 0x64, 0x62, 0x06, 0x2a, 0x8b, 0xd9, 0x4d, 0x23, 0xcd, 0x2b, 0xef, 0xf5, 0x61, 0x82, 0x8e,
      0x3f, 0xf6, 0x2b, 0xe1, 0x6f, 0xcf, 0xbd, 0xaa, 0x07, 0x97, 0x49, 0x4e, 0x02, 0x9d, 0xa5, 0x9e,
      0xc5, 0xd7, 0x8b, 0xd3, 0xe1, 0xd9, 0x35, 0x96, 0x9d, 0x1f, 0xa2, 0xf6, 0x91, 0xee, 0xd1, 0x3b,
      0xa8, 0xfe, 0x4d, 0xeb, 0xf9, 0xfc, 0xe4, 0xab, 0x60, 0xb7, 0x86, 0x9d, 0x2a, 0x35, 0xb0, 0x00,
      0xd4, 0x3c, 0x2a, 0x7e, 0x6d, 0x65, 0x5f, 0xf3, 0x7c, 0x23, 0x57, 0x52, 0x2a, 0x8c, 0x5b, 0x36,
      0x74, 0xb7, 0x61, 0x49, 0xf0, 0xdf, 0xcf, 0x8a, 0x28, 0xc5, 0x8d, 0xbc, 0x20, 0xcc, 0xac, 0x86,
      0x20, 0xd8, 0x2d, 0x86, 0x99, 0xf5, 0xf0, 0xdb, 0xed, 0x8d, 0xf9, 0xd7, 0x4e, 0xa8, 0xde, 0x84,
      0x35, 0x50, 0xc1, 0x7c, 0xbd, 0xdf, 0xc2, 0x24, 0x1a, 0x49, 0x24, 0x9a, 0x37, 0x93, 0xca, 0x2d,
      0x73, 0x47, 0x8f, 0x83, 0xed, 0x4d, 0xca, 0xf8, 0xf0, 0xd3, 0x9b, 0xe0, 0x4b, 0x3b, 0xf1, 0x86,
      0xeb, 0x78, 0x7b, 0x42, 0xa1, 0xb9, 0x36, 0x15, 0xde, 0x63, 0xab, 0x8b, 0x8b, 0x5d, 0xa2, 0x92,
      0x10, 0x95, 0xdf, 0xda, 0xd7, 0xba, 0xa0, 0x26, 0xb9, 0xdc, 0x83, 0xeb, 0xdc, 0xd2, 0x1f, 0xf1,
      0xb1, 0x8d, 0x21, 0x51, 0x71, 0x59, 0x0e, 0xe8, 0x7e, 0xf1, 0x53, 0x08, 0x98, 0x79, 0x05, 0x3b,
      0x22, 0xf1, 0xda, 0x07, 0x0d, 0xf7, 0x89, 0x5e, 0xc4, 0x62, 0x8c, 0xf9, 0x19, 0xc8, 0xbc, 0xa4,
      0x0c, 0x6f, 0x41, 0x34, 0x56, 0x22, 0x6b, 0xe6, 0xee, 0x7c, 0x4a, 0xd9, 0x26, 0x8c, 0x56, 0x12,
      0xf3, 0x03, 0x12, 0x1c, 0x5b, 0x8d, 0x64, 0x5c, 0x1c, 0xb6, 0x0f, 0x93, 0xaf, 0xb1, 0x67, 0x6f,
      0x13, 0xdd, 0xe3, 0xcf, 0x0e, 0xe6, 0x06, 0xf3, 0xb2, 0xbc, 0x99, 0xf5, 0xb0, 0xd7, 0xe9, 0x7e,
      0xb0, 0x6a, 0xb9, 0xb5, 0xda, 0xcf, 0x88, 0xf1, 0xc5, 0x58, 0x54, 0x05, 0x5c, 0x9d, 0x79, 0xc2,
      0xcd, 0xbb, 0xc6, 0xf2, 0x69, 0xa9, 0xe3, 0x4e, 0x05, 0x0d, 0x02, 0xb6, 0x4d, 0x8e, 0x7d, 0x60,
      0x8e, 0xda, 0x4d, 0x28, 0xd2, 0xec, 0x8a, 0x11, 0xe3, 0xe7, 0x17, 0x20, 0x07, 0x7b, 0xfc, 0x9b,
      0x4e, 0xf7, 0x79, 0xf5, 0x0a, 0x6e, 0xd1, 0x1e, 0x7b, 0x83, 0x66, 0x5e, 0x1b, 0x9d, 0x36, 0x32,
      0x89, 0xf6, 0x72, 0xa5, 0x58, 0x54, 0x42, 0xba, 0x90, 0xf3, 0xbb, 0x05, 0x46, 0xa4, 0x91, 0x1c,
      0xdb, 0xab, 0xf3, 0x68, 0x56, 0x7a, 0xd3, 0xff, 0x3f, 0x9f, 0xc5, 0x4a, 0x47, 0xbd, 0x89, 0x46,
      0xf6, 0x94, 0x3a, 0x94, 0xd4, 0x30, 0xd3, 0xae, 0x0d, 0x99, 0x95, 0xf7, 0x75, 0xfe, 0x14, 0x10,
      0x9e, 0xed, 0x21, 0x0f, 0x0d, 0x54, 0x7d, 0x54, 0xc5, 0x80, 0x21, 0x4d, 0xf2, 0xaf, 0x67, 0xaf,
      0x8a, 0x76, 0x9e, 0x34, 0x32, 0x74, 0x89, 0x2a, 0x32, 0xf9, 0x48, 0x20, 0x90, 0xe6, 0x4a, 0xa3,
      0x7f, 0xf2, 0x2a, 0x51, 0x22, 0x93, 0xe5, 0xdd, 0x59, 0xb3, 0x83, 0xa8, 0x47, 0xf5, 0x6b, 0x38,
      0x24, 0xc2, 0xac, 0x2d, 0x03, 0xda, 0xb1, 0x17, 0x19, 0xe0, 0x38, 0x2c, 0xb3, 0xa6, 0x4c, 0x8e,
      0xae, 0x63, 0xa7, 0xae, 0x96, 0xb1, 0x07, 0x8c, 0x8f, 0x6a, 0x08, 0x32, 0x15, 0x1f, 0x33, 0x97,
      0x21, 0x3b, 0x51, 0x70, 0xc5, 0x1f, 0xa6, 0xa3, 0x8a, 0xd0, 0x8f, 0x0b, 0xda, 0x64, 0xab, 0xbe,
      0xee, 0x4b, 0x14, 0xfd, 0x32, 0x87, 0x9e, 0xa7, 0x19, 0x75, 0xc9, 0xaa, 0xd3, 0xed, 0xa7, 0xa0,
      0x01, 0xe7, 0xa0, 0xe5, 0x28, 0xdd, 0x3b, 0x7c, 0x49, 0xe4, 0x24, 0x7d, 0x92, 0x86, 0x25, 0x03,
      0xb3, 0x66, 0x04, 0xf3, 0xa1, 0x40, 0x11, 0x35, 0x3a, 0x1d, 0xbf, 0x1c, 0x02, 0x83, 0x3d, 0x37,
      0x51, 0x88, 0xa3, 0x2b, 0x10, 0x8c, 0x8e, 0x10, 0xdd, 0xdc, 0xef, 0xa4, 0xe9, 0x14, 0x77, 0xb6,
      0x8e, 0x75, 0xb6, 0x8e, 0xea, 0xaa, 0x57, 0x16, 0x1f, 0xb0, 0x0c, 0xbc, 0x44, 0xed, 0x92, 0x94,
      0x9a, 0xb4, 0xf3, 0x31, 0x64, 0x02, 0x5c, 0xa1, 0x51, 0x63, 0x39, 0x42, 0x74, 0x7a, 0x1d, 0xf2,
      0xf5, 0x92, 0x50, 0xf1, 0x5a, 0x8a, 0xde, 0xb3, 0x4e, 0xf1, 0x6e, 0x67, 0xd9, 0x5b, 0x00, 0xa7,
      0xd1, 0x90, 0x58, 0x36, 0xc4, 0x15, 0x80, 0xbb, 0xa5, 0xbb, 0x98, 0xc0, 0x8a, 0x9b, 0x17, 0x35,
      0x36, 0x3b, 0x62, 0x0f, 0x29, 0xcd, 0xe9, 0x04, 0x0e, 0x9d, 0xca, 0x43, 0x04, 0xdf, 0x17, 0x49,
      0xbf, 0xb6, 0x7a, 0x7a, 0x3c, 0xdb, 0x0d, 0x6d, 0xd5, 0x89, 0xb9, 0x69, 0x94, 0xd8, 0xb2, 0xd6,
      0x38, 0x8a, 0xcc, 0x78, 0x44, 0x40, 0x63, 0x9f, 0x1e, 0x0e, 0x40, 0x33, 0x51, 0xd3, 0x65, 0xf8,
      0xf1, 0x42, 0x06, 0x75, 0x84, 0xe7, 0xb1, 0xe9, 0xd6, 0xa4, 0x5e, 0x7f, 0xb0, 0x48, 0x6f, 0x80,
      0x92, 0xf8, 0xfc, 0x2a, 0xdb, 0x18, 0x97, 0xe5, 0xe7, 0xc7, 0x46, 0xb6, 0x59, 0x8c, 0x3a, 0x09,
      0x91, 0xc1, 0x49, 0x55, 0xf9, 0xf3, 0x87, 0x19, 0xdc, 0x72, 0x56, 0xd3, 0x20, 0x5e, 0xc5, 0x3d,
      0xfb, 0x19, 0xea, 0x6a, 0xdf, 0x09, 0xb2, 0x8f, 0xb6, 0xdd, 0x26, 0x31, 0x25, 0x30, 0x23, 0x06,
      0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x15, 0x31, 0x16, 0x04, 0x14, 0x3b, 0xd2,
      0xb3, 0x51, 0x4c, 0x57, 0xd0, 0xca, 0x34, 0xa4, 0xf0, 0x06, 0xdd, 0xe9, 0x76, 0x08, 0xdb, 0x7b,
      0x3a, 0xb0, 0x30, 0x31, 0x30, 0x21, 0x30, 0x09, 0x06, 0x05, 0x2b, 0x0e, 0x03, 0x02, 0x1a, 0x05,
      0x00, 0x04, 0x14, 0x8e, 0x7f, 0x87, 0x67, 0x78, 0x64, 0x93, 0x36, 0x35, 0xe5, 0x93, 0x9d, 0xac,
      0x61, 0x09, 0x4f, 0xdc, 0x95, 0xd7, 0x4f, 0x04, 0x08, 0x23, 0xc2, 0xc0, 0xc6, 0x8d, 0x5f, 0x70,
      0x7e, 0x02, 0x02, 0x08, 0x00]);

    let p12: cert.Pkcs12Data = await cert.parsePkcs12(p12_cert, '123456');
    console.info('parsePKCS12 result: success.');
    if (p12.privateKey) {
      console.info('privateKey:' + p12.privateKey.toString());
    }
    if (p12.cert) {
      console.info('cert:' + p12.cert.toString());
    }
    if (p12.otherCerts && Array.isArray(p12.otherCerts)) {
      console.info('otherCerts counts:', p12.otherCerts.length);
      p12.otherCerts.forEach((cert, idx) => {
        console.info(`otherCerts[${idx}]:\n${cert.toString()}`);
      });
    } else {
      console.info('otherCerts is empty or not an array.');
    }
  } catch (err) {
    console.error(`parsePKCS12 failed: errCode: ${err.code}, errMsg: ${err.message}`);
}
```

#### cert.createPkcs1221+

createPkcs12(data: Pkcs12Data, config: Pkcs12CreationConfig): Promise<Uint8Array>

表示创建Pkcs12数据。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Pkcs12Data | 是 | 要打包的Pkcs12数据对象。 |
| config | Pkcs12CreationConfig | 是 | Pkcs12文件的创建配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象。表示创建的Pkcs12文件，DER格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The password is too short or too long; 2. The private key does not match the certificate; 3. Invalid encryption algorithm parameters. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let priKey = '-----BEGIN PRIVATE KEY-----\n' +
  'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9kBV6Cqd3vSi5\n' +
  'RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnxObpDLyQw0Uu08tbn\n' +
  'EQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd0LS9k8Q57FRqOrQm\n' +
  '7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfkDbuSKRD7UvVV/JZi\n' +
  'BklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLRnRPCVePV6xtoCmbN\n' +
  'A3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNxkDQtugv14qeDsFPS\n' +
  'IU8CtkCbAgMBAAECggEBAKbMmMlJhLCM5r+ZDJE/j55ujRLe6XwC1xP2keEeTdK9\n' +
  '18aKLGR41BPsSH8JfAxh0m75lSvLjoVLRSQPUOZIfjXqUF/2hzzug5F2W8xKVovH\n' +
  'o1uqHlp71nVZPrJK7Q9H7TH/SyP4uxK6UvkKzt0j34WLHgeqV3t8qCMhB34zIAWG\n' +
  'BcAuKJNRZGvMvjK99OSOh0SyvGQ5Yb5vyj1/znx3gM4z4deYXxDSyCO0m5I16jmM\n' +
  'gBEUG0UDUp8Xr2xs/EkhhWYRT1bkDlYZ9IuCbH/vB1YJJFdaO2tDivDUF6IObvNt\n' +
  'GaVuLlA/rSOJmJFBetrm7n+O2vNJxvoQmBYDKm3+qYkCgYEA9p5C1ZY5XfwwOcqi\n' +
  'KQ+Asd2NWLG2blhsII5wB8uPhFapjV0S9xTabScUD35AfxHgctafpZeQk4x5niRP\n' +
  'BHq7hpitaDdYs6A/jhZ7fdVYKb1KRTDt1LXmcg0qVmi/ANNvjhqjvyZM+pEj8yxM\n' +
  'aOl4isbBfUbzSsEbda3LcHi6+w8CgYEAxMYtkl3gbXJcgbAEdW+nMMQGoFDLkgyu\n' +
  'n0ZYuRRrWLnnUzZUyqNBwQUaZpwxHaAqi0OAEGSRSZBKRHz9IA2iP9YzcaJ0WtpB\n' +
  'CPqwBZjrCaVEpHldo2pIdujysXgiXRUiE+VR9ViDmftoVbdL6kttGS08jBBDVIV/\n' +
  'uQgC/q29UbUCgYAJHirMaMRwNB24VUSPjhItAUrzh4Z+J+i/f2Sm9SC2PNoB7vn/\n' +
  'hpbYyEQWmo1Z5VhOBp9aaPMgcWYhsaf2O29pd4WZv8oYwgj3gN9J9LRQvr3bNwbk\n' +
  'AWGmv9Pb4/2D001hjJyXOZxI+0q/99hPXKpnPxfyQMhH8EHKpQVLgDsxgwKBgEiH\n' +
  '+DJUci5Fkj2ngO08u7bo+rxLK85o6FEDYB7QnQT2eYMdqsGKzej1FZcvCZeu+x+c\n' +
  'QO9J8pfYHNgD7lXLULwRG6NOS29VtdU2en2FsVU72wJ5Tf+3ZICYOyUZcCk5afdF\n' +
  'dyFlgBTZK8s0pkH1jYBTQVcrg3X7Q2oTvu7bYcZlAoGAUwQI11mMR8oqfgWMoI/1\n' +
  'smOoq9qSMlutuWBjoPkbtJEGHEXAvjW1kgdBlPjUCwn6j+oIDLYu8DbfQRdiFQeP\n' +
  'rVCbbgOgayVpr+8Tv2DqB370GwBpOpuq0yiiN+c39Y0u03Yfve3icyl8+lN1t4h6\n' +
  'a20rj9HG4sb8tUIHPBv0dgY=\n' +
  '-----END PRIVATE KEY-----\n';

let othercert = '-----BEGIN CERTIFICATE-----\n' +
  'MIIDZTCCAk0CFAoqA7Irtoo7/3+sfOHy0s91pKkiMA0GCSqGSIb3DQEBCwUAMG8x\n' +
  'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
  'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
  'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NDM0WhcNMjYwODE0MTE1NDM0WjBv\n' +
  'MQswCQYDVQQGEwJFTjENMAsGA1UECAwEVEVTVDENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
  'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR4aWFuMQ0wCwYDVQQDDAR4aWFuMRMwEQYJ\n' +
  'KoZIhvcNAQkBFgR4aWFuMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n' +
  'wk4aByV5nOw+zIh/1agaN7rQyk+NFuXlYSwINrONRZt8zePSxhxz6gMq0XAb8ld0\n' +
  'DFC5onGQEI4ED8iP3v7C7yHqIAybTmIy22RWWk8c6h9S40Azp/YHujTTRs2XMe9G\n' +
  'A/iKed9DwLclbv6+m+WPmIvgFFAJlebtFI6X0E/zBxs/TknR8tJ2uk2G/CGCBlo5\n' +
  'bbSz5RIPfEmz93rR7prMxQLOsvfdNewNlhe82jxMKfzGEPXYXUj+Xwp8ep+aaUTr\n' +
  'Kb6Thvx7+uOBxgMM1crREepTKJM/4bsOpb2yIXXcOqclUPAZBvtzIjgs/DdKtCZo\n' +
  '0Jzr3gUbDJeE2xd+DcADxQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA5RyDOMYJV\n' +
  'AsdBUihPvnnakKfAY9CYN9I1tR0b9DaboeL+bONeIKzXyFdDrAj6eZLKZLUblFlH\n' +
  'BZnbP4lNwfYjmNgp4j7cqSIFVwd2Y+6T29pK6T6XYRsFGOaSp7wFzXplfbP8Ou1b\n' +
  'o2zTZWWWHbiExuXot4RfQkgH3Zhk5zjJGWvaOksvEhJUaufkWAXbRY2KHmH64dDB\n' +
  'Bgp50CPObTuc2a+5PAi7W5nj1se2OqKvepoeYLl8pfF/GFRqrvcII9kCm0oyMqBx\n' +
  '25R7aCNtSnENZnvRBspdYcX8zu6fR1qf0JmpLqLw5pPxJ2Puvq7g+33GWJ3Gq45f\n' +
  'ZcLXS+9LpW3a\n' +
  '-----END CERTIFICATE-----\n';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIDZzCCAk8CFCwQ5cxuFI+fsf/2fkG4gy8UT1gmMA0GCSqGSIb3DQEBCwUAMG8x\n' +
  'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
  'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
  'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NTQ1WhcNMjYwODE0MTE1NTQ1WjBx\n' +
  'MQswCQYDVQQGEwJHVDEPMA0GA1UECAwGaHVhd2VpMQ0wCwYDVQQHDAR4aWFuMQ8w\n' +
  'DQYDVQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzAR\n' +
  'BgkqhkiG9w0BCQEWBHhpYW4wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB\n' +
  'AQC9kBV6Cqd3vSi5RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnx\n' +
  'ObpDLyQw0Uu08tbnEQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd\n' +
  '0LS9k8Q57FRqOrQm7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfk\n' +
  'DbuSKRD7UvVV/JZiBklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLR\n' +
  'nRPCVePV6xtoCmbNA3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNx\n' +
  'kDQtugv14qeDsFPSIU8CtkCbAgMBAAEwDQYJKoZIhvcNAQELBQADggEBALuqlvql\n' +
  'q/5SVghmtdzVNlsif9JofSgJhmww3r8HblZ7zD7ALfR6JcxxbBJYdBIn6mf2eNx/\n' +
  'kTzwYs94D12PhyAP63AcDxS/4Sh7QhmnNIx2SGi/rbFdPm8cmkaFfwr5gQP+ouNB\n' +
  '1e7vVyNpSjr4F8YcfjOHPofoCdWaOaBPrM760h711y/BTVMjuYkdzn0D1bHZIBc+\n' +
  'tljIMWXKsTwR6wCIpnFRJbEATTBwV843Q071d62jYueLgdS2wT39Syqb3ao3aHAS\n' +
  'ZI8k9GgNNKD4qBAZUbQVCs6diTBbeUMaqJ2N+tcQfmGfnNZK+/olEF6Ue/H0LZzY\n' +
  'nZSOvPxc0c2O34k=\n' +
  '-----END CERTIFICATE-----\n';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509Cert(certData: string): Promise<cert.X509Cert> {
  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (err) {
    console.error(`createX509Cert failed: errCode: ${err.code}, errMsg: ${err.message}`);
  }
  return x509Cert;
}

async function doTestCreatePkcs12() {
  const caCert = await createX509Cert(othercert);
  const x509Cert = await createX509Cert(certData);

  let data : cert.Pkcs12Data = {
    privateKey : priKey,
    cert : x509Cert,
    otherCerts : [caCert]
  }

  let keyParam : cert.PbesParams = {
    saltLen : 16,
    iterations : 2048,
    encryptionAlgorithm : cert.PbesEncryptionAlgorithm.AES_192_CBC
  }

  let certParam : cert.PbesParams = {
    saltLen : 16,
    iterations : 2048,
    encryptionAlgorithm : cert.PbesEncryptionAlgorithm.AES_256_CBC
  }

  let config : cert.Pkcs12CreationConfig = {
    password: '123456',
    keyEncParams : keyParam,
    encryptCert : true,
    certEncParams : certParam,
    macSaltLen : 16,
    macIterations : 2048,
    macDigestAlgorithm : cert.Pkcs12MacDigestAlgorithm.SHA384
  }
  try {
    let p12 = await cert.createPkcs12(data, config);
    console.info('createPkcs12 result: success, p12 = ' + p12);
  } catch (err) {
    console.error(`createPkcs12 failed: errCode: ${err.code}, errMsg: ${err.message}`);
}
```

#### cert.createPkcs1221+

createPkcs12Sync(data: Pkcs12Data, config: Pkcs12CreationConfig): Uint8Array

表示创建Pkcs12数据，同步返回结果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Pkcs12Data | 是 | 要打包的P12数据对象。 |
| config | Pkcs12CreationConfig | 是 | P12文件的创建配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 表示创建的P12文件，DER格式。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The password is too short or too long; 2. The private key does not match the certificate; 3. Invalid encryption algorithm parameters. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let priKey = '-----BEGIN PRIVATE KEY-----\n' +
  'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9kBV6Cqd3vSi5\n' +
  'RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnxObpDLyQw0Uu08tbn\n' +
  'EQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd0LS9k8Q57FRqOrQm\n' +
  '7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfkDbuSKRD7UvVV/JZi\n' +
  'BklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLRnRPCVePV6xtoCmbN\n' +
  'A3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNxkDQtugv14qeDsFPS\n' +
  'IU8CtkCbAgMBAAECggEBAKbMmMlJhLCM5r+ZDJE/j55ujRLe6XwC1xP2keEeTdK9\n' +
  '18aKLGR41BPsSH8JfAxh0m75lSvLjoVLRSQPUOZIfjXqUF/2hzzug5F2W8xKVovH\n' +
  'o1uqHlp71nVZPrJK7Q9H7TH/SyP4uxK6UvkKzt0j34WLHgeqV3t8qCMhB34zIAWG\n' +
  'BcAuKJNRZGvMvjK99OSOh0SyvGQ5Yb5vyj1/znx3gM4z4deYXxDSyCO0m5I16jmM\n' +
  'gBEUG0UDUp8Xr2xs/EkhhWYRT1bkDlYZ9IuCbH/vB1YJJFdaO2tDivDUF6IObvNt\n' +
  'GaVuLlA/rSOJmJFBetrm7n+O2vNJxvoQmBYDKm3+qYkCgYEA9p5C1ZY5XfwwOcqi\n' +
  'KQ+Asd2NWLG2blhsII5wB8uPhFapjV0S9xTabScUD35AfxHgctafpZeQk4x5niRP\n' +
  'BHq7hpitaDdYs6A/jhZ7fdVYKb1KRTDt1LXmcg0qVmi/ANNvjhqjvyZM+pEj8yxM\n' +
  'aOl4isbBfUbzSsEbda3LcHi6+w8CgYEAxMYtkl3gbXJcgbAEdW+nMMQGoFDLkgyu\n' +
  'n0ZYuRRrWLnnUzZUyqNBwQUaZpwxHaAqi0OAEGSRSZBKRHz9IA2iP9YzcaJ0WtpB\n' +
  'CPqwBZjrCaVEpHldo2pIdujysXgiXRUiE+VR9ViDmftoVbdL6kttGS08jBBDVIV/\n' +
  'uQgC/q29UbUCgYAJHirMaMRwNB24VUSPjhItAUrzh4Z+J+i/f2Sm9SC2PNoB7vn/\n' +
  'hpbYyEQWmo1Z5VhOBp9aaPMgcWYhsaf2O29pd4WZv8oYwgj3gN9J9LRQvr3bNwbk\n' +
  'AWGmv9Pb4/2D001hjJyXOZxI+0q/99hPXKpnPxfyQMhH8EHKpQVLgDsxgwKBgEiH\n' +
  '+DJUci5Fkj2ngO08u7bo+rxLK85o6FEDYB7QnQT2eYMdqsGKzej1FZcvCZeu+x+c\n' +
  'QO9J8pfYHNgD7lXLULwRG6NOS29VtdU2en2FsVU72wJ5Tf+3ZICYOyUZcCk5afdF\n' +
  'dyFlgBTZK8s0pkH1jYBTQVcrg3X7Q2oTvu7bYcZlAoGAUwQI11mMR8oqfgWMoI/1\n' +
  'smOoq9qSMlutuWBjoPkbtJEGHEXAvjW1kgdBlPjUCwn6j+oIDLYu8DbfQRdiFQeP\n' +
  'rVCbbgOgayVpr+8Tv2DqB370GwBpOpuq0yiiN+c39Y0u03Yfve3icyl8+lN1t4h6\n' +
  'a20rj9HG4sb8tUIHPBv0dgY=\n' +
  '-----END PRIVATE KEY-----\n';

let othercert = '-----BEGIN CERTIFICATE-----\n' +
  'MIIDZTCCAk0CFAoqA7Irtoo7/3+sfOHy0s91pKkiMA0GCSqGSIb3DQEBCwUAMG8x\n' +
  'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
  'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
  'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NDM0WhcNMjYwODE0MTE1NDM0WjBv\n' +
  'MQswCQYDVQQGEwJFTjENMAsGA1UECAwEVEVTVDENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
  'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR4aWFuMQ0wCwYDVQQDDAR4aWFuMRMwEQYJ\n' +
  'KoZIhvcNAQkBFgR4aWFuMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n' +
  'wk4aByV5nOw+zIh/1agaN7rQyk+NFuXlYSwINrONRZt8zePSxhxz6gMq0XAb8ld0\n' +
  'DFC5onGQEI4ED8iP3v7C7yHqIAybTmIy22RWWk8c6h9S40Azp/YHujTTRs2XMe9G\n' +
  'A/iKed9DwLclbv6+m+WPmIvgFFAJlebtFI6X0E/zBxs/TknR8tJ2uk2G/CGCBlo5\n' +
  'bbSz5RIPfEmz93rR7prMxQLOsvfdNewNlhe82jxMKfzGEPXYXUj+Xwp8ep+aaUTr\n' +
  'Kb6Thvx7+uOBxgMM1crREepTKJM/4bsOpb2yIXXcOqclUPAZBvtzIjgs/DdKtCZo\n' +
  '0Jzr3gUbDJeE2xd+DcADxQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA5RyDOMYJV\n' +
  'AsdBUihPvnnakKfAY9CYN9I1tR0b9DaboeL+bONeIKzXyFdDrAj6eZLKZLUblFlH\n' +
  'BZnbP4lNwfYjmNgp4j7cqSIFVwd2Y+6T29pK6T6XYRsFGOaSp7wFzXplfbP8Ou1b\n' +
  'o2zTZWWWHbiExuXot4RfQkgH3Zhk5zjJGWvaOksvEhJUaufkWAXbRY2KHmH64dDB\n' +
  'Bgp50CPObTuc2a+5PAi7W5nj1se2OqKvepoeYLl8pfF/GFRqrvcII9kCm0oyMqBx\n' +
  '25R7aCNtSnENZnvRBspdYcX8zu6fR1qf0JmpLqLw5pPxJ2Puvq7g+33GWJ3Gq45f\n' +
  'ZcLXS+9LpW3a\n' +
  '-----END CERTIFICATE-----\n';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIDZzCCAk8CFCwQ5cxuFI+fsf/2fkG4gy8UT1gmMA0GCSqGSIb3DQEBCwUAMG8x\n' +
  'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
  'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
  'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NTQ1WhcNMjYwODE0MTE1NTQ1WjBx\n' +
  'MQswCQYDVQQGEwJHVDEPMA0GA1UECAwGaHVhd2VpMQ0wCwYDVQQHDAR4aWFuMQ8w\n' +
  'DQYDVQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzAR\n' +
  'BgkqhkiG9w0BCQEWBHhpYW4wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB\n' +
  'AQC9kBV6Cqd3vSi5RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnx\n' +
  'ObpDLyQw0Uu08tbnEQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd\n' +
  '0LS9k8Q57FRqOrQm7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfk\n' +
  'DbuSKRD7UvVV/JZiBklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLR\n' +
  'nRPCVePV6xtoCmbNA3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNx\n' +
  'kDQtugv14qeDsFPSIU8CtkCbAgMBAAEwDQYJKoZIhvcNAQELBQADggEBALuqlvql\n' +
  'q/5SVghmtdzVNlsif9JofSgJhmww3r8HblZ7zD7ALfR6JcxxbBJYdBIn6mf2eNx/\n' +
  'kTzwYs94D12PhyAP63AcDxS/4Sh7QhmnNIx2SGi/rbFdPm8cmkaFfwr5gQP+ouNB\n' +
  '1e7vVyNpSjr4F8YcfjOHPofoCdWaOaBPrM760h711y/BTVMjuYkdzn0D1bHZIBc+\n' +
  'tljIMWXKsTwR6wCIpnFRJbEATTBwV843Q071d62jYueLgdS2wT39Syqb3ao3aHAS\n' +
  'ZI8k9GgNNKD4qBAZUbQVCs6diTBbeUMaqJ2N+tcQfmGfnNZK+/olEF6Ue/H0LZzY\n' +
  'nZSOvPxc0c2O34k=\n' +
  '-----END CERTIFICATE-----\n';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509Cert(certData: string): Promise<cert.X509Cert> {
  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (err) {
    console.error(`createX509Cert failed: errCode: ${err.code}, errMsg: ${err.message}`);
  }
  return x509Cert;
}

async function doTestCreatePkcs12Sync() {
  const caCert = await createX509Cert(othercert);
  const x509Cert = await createX509Cert(certData);

  let data : cert.Pkcs12Data = {
    privateKey : priKey,
    cert : x509Cert,
    otherCerts : [caCert]
  }

  let keyParam : cert.PbesParams = {
    saltLen : 16,
    iterations : 2048,
    encryptionAlgorithm : cert.PbesEncryptionAlgorithm.AES_192_CBC
  }

  let certParam : cert.PbesParams = {
    saltLen : 16,
    iterations : 2048,
    encryptionAlgorithm : cert.PbesEncryptionAlgorithm.AES_256_CBC
  }

  let config : cert.Pkcs12CreationConfig = {
    password: '123456',
    keyEncParams : keyParam,
    encryptCert : true,
    certEncParams : certParam,
    macSaltLen : 16,
    macIterations : 2048,
    macDigestAlgorithm : cert.Pkcs12MacDigestAlgorithm.SHA384
  }
  try {
    let p12 = cert.createPkcs12Sync(data, config);
    console.info('createPkcs12Sync result: success, p12 = ' + p12);
  } catch (err) {
    console.error(`createPkcs12Sync failed: errCode: ${err.code}, errMsg: ${err.message}`);
}
```

#### cert.createTrustAnchorsWithKeyStore12+

createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<[X509TrustAnchor](#ZH-CN_TOPIC_0000002522081410__x509trustanchor11)>>

表示从P12文件中读取ca证书来构造[TrustAnchor](#ZH-CN_TOPIC_0000002522081410__x509trustanchor11)对象数组。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keystore | Uint8Array | 是 | P12文件，DER格式。 |
| pwd | string | 是 | P12文件的密码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<X509TrustAnchor>> | 表示X509TrustAnchor对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  cert.createTrustAnchorsWithKeyStore(
    new Uint8Array([0x30, 0x82, 0x07, 0x5C, 0x02, 0x01, 0x03, 0x30, 0x82, 0x07, 0x12, 0x06, 0x09, 0x2A, 0x86, 0x48,
      0x86, 0xF7, 0x0D, 0x01, 0x07, 0x01, 0xA0, 0x82, 0x07, 0x03, 0x04, 0x82, 0x06, 0xFF, 0x30, 0x82, 0x06, 0xFB, 0x30,
      0x82, 0x05, 0xB2, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x07, 0x06, 0xA0, 0x82, 0x05, 0xA3, 0x30,
      0x82, 0x05, 0x9F, 0x02, 0x01, 0x00, 0x30, 0x82, 0x05, 0x98, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01,
      0x07, 0x01, 0x30, 0x57, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x05, 0x0D, 0x30, 0x4A, 0x30, 0x29,
      0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x05, 0x0C, 0x30, 0x1C, 0x04, 0x08, 0xA9, 0x1C, 0x1B, 0x19,
      0x36, 0xDE, 0xD4, 0x20, 0x02, 0x02, 0x08, 0x00, 0x30, 0x0C, 0x06, 0x08, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x02,
      0x09, 0x05, 0x00, 0x30, 0x1D, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x01, 0x2A, 0x04, 0x10, 0x7D,
      0xE5, 0x23, 0x96, 0x18, 0x8B, 0xF4, 0xBC, 0x9F, 0x4E, 0xE8, 0xE9, 0xAA, 0x52, 0x18, 0x39, 0x80, 0x82, 0x05, 0x30,
      0x02, 0x2D, 0x59, 0xA9, 0x96, 0x5A, 0xFE, 0x20, 0x18, 0xB2, 0x25, 0xEA, 0xFC, 0x86, 0x0F, 0xA8, 0x3C, 0x2B, 0x26,
      0x2F, 0x44, 0x6E, 0xF3, 0x15, 0xB7, 0x94, 0xE4, 0x43, 0xEE, 0xE6, 0xC3, 0xBB, 0x3C, 0x9E, 0x60, 0x08, 0xF8, 0x15,
      0x61, 0x44, 0xD0, 0xEA, 0xD5, 0x6D, 0x1A, 0x3B, 0x9F, 0x4E, 0x2A, 0x1E, 0xBB, 0xB9, 0x4E, 0x15, 0x43, 0xB8, 0x68,
      0xDB, 0x1A, 0x4E, 0x41, 0xBA, 0x29, 0x8E, 0x75, 0xEB, 0x12, 0xC1, 0xF0, 0x4B, 0x0D, 0x13, 0xB2, 0xC2, 0x48, 0x6F,
      0xC4, 0xC4, 0x82, 0xF2, 0x26, 0xD4, 0x3D, 0x1F, 0x42, 0x7D, 0x67, 0xB0, 0x37, 0x55, 0x9E, 0xD9, 0x46, 0x99, 0x98,
      0xB4, 0xE7, 0x4B, 0x07, 0x08, 0x3F, 0xD3, 0x96, 0x9A, 0xC5, 0xDA, 0x37, 0x74, 0x08, 0x5D, 0x3B, 0x06, 0x8A, 0x16,
      0x6D, 0x81, 0x63, 0x01, 0x83, 0x94, 0xDA, 0x1B, 0x0E, 0x04, 0xCE, 0x18, 0xF0, 0x51, 0x22, 0xD8, 0x2D, 0xF1, 0x69,
      0x0C, 0xCB, 0xC9, 0x51, 0x17, 0x07, 0x1F, 0x2B, 0xCF, 0x74, 0x26, 0xD7, 0x73, 0xB3, 0x2D, 0xF2, 0x82, 0xF0, 0x38,
      0x5B, 0x8A, 0x8F, 0xCD, 0x84, 0x69, 0x40, 0x59, 0xCE, 0xB3, 0x39, 0xFE, 0xF6, 0xB7, 0x24, 0x89, 0x34, 0xFF, 0xF4,
      0x40, 0x50, 0x06, 0x4D, 0xC6, 0x13, 0x82, 0xAF, 0x7F, 0x84, 0xB1, 0x67, 0x3C, 0x89, 0xBB, 0x5D, 0x32, 0xC3, 0xA6,
      0xF1, 0x7D, 0xF5, 0x72, 0x68, 0x75, 0xCE, 0x69, 0xAB, 0x6C, 0x32, 0xDA, 0x16, 0x3B, 0xC4, 0xCA, 0x47, 0x45, 0xE9,
      0x59, 0x1E, 0xB1, 0x70, 0xDA, 0x8A, 0x00, 0x69, 0x80, 0x40, 0xCA, 0x60, 0xE6, 0x07, 0x16, 0xF0, 0xA2, 0xF9, 0x12,
      0x7D, 0x09, 0x43, 0x66, 0x46, 0x78, 0x35, 0xA6, 0x94, 0x35, 0x60, 0x82, 0xFC, 0xB8, 0x5E, 0x39, 0xE7, 0xA1, 0x22,
      0xAD, 0xCC, 0x6F, 0x5E, 0xCE, 0x01, 0x6B, 0xA1, 0xDD, 0xE5, 0xDD, 0x79, 0x9B, 0xA1, 0x28, 0xC4, 0x03, 0x84, 0x8D,
      0x6C, 0x07, 0xD4, 0xFE, 0x57, 0xFB, 0x89, 0x3F, 0x43, 0x44, 0x69, 0xF1, 0x9E, 0x53, 0x6C, 0x11, 0x11, 0x96, 0x79,
      0xE4, 0xB8, 0x3B, 0x49, 0x2E, 0xF6, 0x3B, 0xC5, 0x6C, 0x76, 0x21, 0x22, 0x15, 0x85, 0x77, 0x8A, 0xDD, 0xD2, 0x43,
      0x85, 0x73, 0x39, 0x77, 0x9F, 0xFA, 0x8F, 0xCF, 0xCB, 0xEA, 0x62, 0xBD, 0x5C, 0x66, 0x45, 0xCD, 0xB0, 0xCA, 0x42,
      0xCC, 0xB9, 0xCF, 0xE3, 0x84, 0x63, 0x9F, 0x63, 0xCE, 0x49, 0xE9, 0x74, 0x26, 0xCC, 0x26, 0x78, 0xCE, 0x9F, 0x4E,
      0x38, 0xA2, 0x9C, 0xEB, 0x75, 0xC5, 0x33, 0x6B, 0x00, 0x83, 0x85, 0xA3, 0x0F, 0xE7, 0xE1, 0x11, 0xA6, 0x48, 0xDC,
      0xEF, 0x0C, 0x05, 0xB3, 0xDE, 0x94, 0xB9, 0x69, 0xCB, 0x27, 0x09, 0xAB, 0x27, 0xD8, 0x06, 0xED, 0x25, 0xBC, 0xA6,
      0x2E, 0xB7, 0xF9, 0x2E, 0xAD, 0x84, 0x1D, 0xDD, 0x73, 0xD8, 0xC0, 0x46, 0x8A, 0xFE, 0x9A, 0xDF, 0x07, 0xE1, 0x33,
      0xE2, 0x1C, 0x37, 0x6A, 0x8E, 0xA2, 0x91, 0x0B, 0xD7, 0x76, 0xEF, 0x3C, 0x87, 0x4A, 0x53, 0x84, 0xFA, 0xFA, 0xC5,
      0x71, 0x76, 0xC0, 0x75, 0x70, 0x67, 0x67, 0x71, 0x9D, 0x8B, 0x81, 0x6F, 0x68, 0xC5, 0xB1, 0xFC, 0xA3, 0x59, 0xB5,
      0xD0, 0x03, 0x56, 0xE7, 0x89, 0x03, 0xD7, 0x99, 0xDE, 0x66, 0x33, 0xFA, 0x53, 0x50, 0x5F, 0xB4, 0x9D, 0xB3, 0x90,
      0x8F, 0x57, 0x20, 0xF0, 0x8B, 0xDB, 0x73, 0xCA, 0xA4, 0x71, 0x61, 0x67, 0x6A, 0x6D, 0xA5, 0xCA, 0x88, 0xD4, 0xCC,
      0x82, 0x34, 0xC9, 0x3E, 0x10, 0x10, 0x57, 0xD1, 0x08, 0x96, 0x80, 0x09, 0xA8, 0xBB, 0x6F, 0x53, 0x8F, 0xFD, 0x87,
      0xCF, 0x73, 0xFC, 0xE1, 0x3A, 0x92, 0x2E, 0x78, 0x66, 0xFB, 0x86, 0x5D, 0x62, 0xE0, 0xC4, 0x58, 0x55, 0x3F, 0xA4,
      0xEA, 0xA1, 0xBE, 0x5B, 0x5E, 0x8E, 0x46, 0x50, 0x5E, 0x7C, 0x01, 0xD6, 0x63, 0xAA, 0x6F, 0xD5, 0xFD, 0xAF, 0xC5,
      0x1D, 0xB3, 0x90, 0x9C, 0xD8, 0x5F, 0x8D, 0xF2, 0x81, 0xEB, 0xBF, 0xA1, 0xDE, 0xB7, 0x9D, 0xCD, 0x24, 0x82, 0x06,
      0x0B, 0x63, 0xE6, 0xBF, 0x57, 0x51, 0xF0, 0xB6, 0xE9, 0x7F, 0xAA, 0x7B, 0x10, 0xBD, 0xCD, 0x85, 0x41, 0xE0, 0xD7,
      0xF1, 0x53, 0xB7, 0xF8, 0x46, 0x91, 0x9E, 0x8D, 0x4B, 0xCB, 0x28, 0x35, 0x40, 0x37, 0x1E, 0x83, 0x64, 0x6A, 0x70,
      0x01, 0x9D, 0xBF, 0xF1, 0x0E, 0xB6, 0x2E, 0x7A, 0xB7, 0x8F, 0x0F, 0x8C, 0x69, 0xD6, 0xF2, 0xD1, 0xF6, 0x1E, 0xCD,
      0x08, 0xA8, 0xD4, 0x1B, 0xCB, 0x38, 0xEA, 0x26, 0x37, 0x5C, 0x60, 0x3A, 0x38, 0x5B, 0x12, 0x1D, 0x00, 0x7B, 0xEC,
      0xCE, 0xFB, 0x89, 0x23, 0x8A, 0x11, 0xE1, 0x1B, 0xDE, 0x54, 0x91, 0x6A, 0x26, 0x22, 0xD0, 0x1C, 0x2E, 0xBA, 0xD0,
      0x92, 0x87, 0xDA, 0xF0, 0x93, 0xBB, 0x3A, 0x2C, 0x52, 0xFB, 0xB2, 0xA9, 0xA8, 0x92, 0x19, 0xE3, 0x19, 0xDC, 0xB0,
      0x0E, 0xC5, 0xE7, 0x9D, 0xFB, 0xF9, 0xA3, 0x23, 0x32, 0xD0, 0x4E, 0x2C, 0x05, 0x2D, 0x76, 0xDB, 0x93, 0x53, 0x5B,
      0x0E, 0x2A, 0xA3, 0xDD, 0x5F, 0xD3, 0x1A, 0x3B, 0x1E, 0x1F, 0x26, 0x88, 0x43, 0xAD, 0x10, 0x1F, 0xA9, 0xC4, 0xF9,
      0x1F, 0xCD, 0xA5, 0xD2, 0xDC, 0x24, 0x95, 0x1D, 0xE7, 0x57, 0xE1, 0x02, 0x0A, 0x20, 0xEA, 0x6A, 0x78, 0x4E, 0x96,
      0xE2, 0xE5, 0x6D, 0x6F, 0xFD, 0x81, 0x7B, 0x61, 0x85, 0xA3, 0x3D, 0xC5, 0x7B, 0xEF, 0xAE, 0x58, 0xA2, 0xDB, 0x91,
      0x73, 0xDB, 0x47, 0x8E, 0xD1, 0x7D, 0xD7, 0x8F, 0x56, 0x06, 0x28, 0x8C, 0x78, 0x73, 0x02, 0x65, 0xB0, 0x16, 0x4B,
      0xE6, 0xA3, 0xD7, 0x06, 0x7C, 0xEA, 0x7D, 0xE2, 0xAE, 0xBB, 0xE5, 0xD2, 0xEB, 0xF0, 0x91, 0x71, 0x7C, 0xBC, 0xA6,
      0x1A, 0xE8, 0x9F, 0xD3, 0xA9, 0x3C, 0x5D, 0x60, 0xCF, 0x59, 0x26, 0x46, 0x45, 0xF2, 0x7F, 0x85, 0x6B, 0xE7, 0xC2,
      0x58, 0x52, 0x90, 0x12, 0x07, 0xBA, 0xE6, 0xB8, 0xE5, 0xD7, 0x24, 0x93, 0xD5, 0x6E, 0xB1, 0x74, 0x6C, 0xAA, 0xA0,
      0x60, 0xBF, 0xF3, 0x32, 0x41, 0x0B, 0xA2, 0x01, 0x84, 0x0D, 0x83, 0xE4, 0x43, 0xD1, 0xBA, 0xC1, 0x92, 0x84, 0x26,
      0xF8, 0xF2, 0x77, 0x20, 0x1B, 0xF2, 0x8F, 0x00, 0x69, 0x18, 0x2F, 0x6C, 0xA8, 0x58, 0xB5, 0x5D, 0xFA, 0x27, 0xD2,
      0x38, 0xD2, 0x49, 0x6E, 0xDF, 0x55, 0x79, 0xAF, 0x1C, 0x44, 0xDA, 0x5A, 0xD7, 0x44, 0x53, 0x50, 0x8B, 0x77, 0x70,
      0x4D, 0x91, 0xEC, 0x07, 0xA5, 0x64, 0x21, 0x3C, 0x31, 0x09, 0x68, 0x65, 0xB4, 0xFA, 0xBE, 0x23, 0xF9, 0xDF, 0x77,
      0x46, 0xA2, 0x9A, 0x5D, 0xE3, 0xBE, 0x1E, 0xE3, 0x84, 0xEF, 0xAE, 0x7D, 0xF8, 0x1C, 0x54, 0xE8, 0x4E, 0xAE, 0xB5,
      0xBB, 0xD6, 0xC3, 0x8D, 0x56, 0x79, 0xE8, 0x7C, 0x43, 0xDC, 0xF3, 0xB3, 0x7A, 0x30, 0x22, 0x09, 0xBC, 0x10, 0xD6,
      0x84, 0xC4, 0x0F, 0x4C, 0x0B, 0xA2, 0xD1, 0xCB, 0xCD, 0x1F, 0x50, 0x3D, 0xF7, 0x23, 0x45, 0x55, 0x18, 0x21, 0x3D,
      0x64, 0x05, 0x2E, 0x52, 0x3A, 0x73, 0xFD, 0xF2, 0xA9, 0xCA, 0x3F, 0xF6, 0x7F, 0x87, 0xE8, 0x56, 0x9B, 0x68, 0x6B,
      0x20, 0xB0, 0x1D, 0x83, 0x04, 0x2F, 0x59, 0xFD, 0x84, 0x57, 0x7D, 0x82, 0x97, 0x96, 0xE8, 0xFB, 0xDF, 0x71, 0x8C,
      0x26, 0x47, 0x85, 0xA5, 0xBE, 0xFB, 0xF5, 0x05, 0x4C, 0xD3, 0x3D, 0x73, 0xF4, 0xA5, 0xF1, 0xA3, 0x99, 0x98, 0x1B,
      0x84, 0x8B, 0xB3, 0x53, 0xCE, 0x4D, 0xEA, 0x5A, 0x48, 0xD2, 0xB9, 0x7E, 0xB6, 0xEB, 0x9B, 0x94, 0x6F, 0xDD, 0x44,
      0x80, 0x89, 0xD2, 0x78, 0x6D, 0xB9, 0xDA, 0x8B, 0x83, 0x49, 0xE0, 0x4D, 0x49, 0xDF, 0x6B, 0xFF, 0xF7, 0x04, 0x00,
      0x32, 0xAA, 0x1D, 0x4F, 0x8D, 0x4B, 0xDE, 0xB8, 0x0D, 0xC6, 0x54, 0x1C, 0xB2, 0xCD, 0x60, 0x29, 0x72, 0x0A, 0x7E,
      0xE7, 0xEB, 0x7A, 0xF6, 0x5B, 0x04, 0x3F, 0x5B, 0x93, 0x12, 0x0D, 0xD5, 0xFF, 0x7A, 0x41, 0x44, 0x0B, 0x37, 0x12,
      0x82, 0x3D, 0xDD, 0x1E, 0x59, 0xB9, 0xBE, 0x0F, 0x9E, 0xD6, 0xD0, 0x68, 0x69, 0x74, 0xF9, 0xB1, 0x21, 0xA3, 0x70,
      0x4F, 0xDA, 0xF8, 0x9F, 0xB9, 0x49, 0x3F, 0xC6, 0xB2, 0x69, 0xC8, 0xD8, 0x60, 0xF1, 0x6A, 0x52, 0x07, 0xFA, 0x42,
      0xFD, 0xA9, 0x06, 0xCF, 0x97, 0x4A, 0x0E, 0xC5, 0xFC, 0x63, 0x27, 0x54, 0xC8, 0xBE, 0x8B, 0x4F, 0xB6, 0x42, 0xBC,
      0xA2, 0xCC, 0x70, 0x4A, 0x6B, 0x24, 0x5B, 0x68, 0x28, 0x47, 0xFA, 0x6B, 0x89, 0x28, 0x07, 0x5D, 0xE0, 0x2C, 0x4A,
      0xD9, 0x22, 0xE3, 0xB3, 0x2F, 0xAA, 0xC2, 0xA0, 0x7C, 0x0F, 0x92, 0xC5, 0xDD, 0xB6, 0x23, 0x8F, 0x73, 0x73, 0x0F,
      0xD7, 0x73, 0x71, 0x2F, 0x0A, 0x78, 0xE8, 0x5B, 0xDB, 0xC2, 0xE0, 0xDB, 0xC9, 0x3E, 0xC3, 0x72, 0x9C, 0x14, 0xD7,
      0xD1, 0x28, 0xFD, 0xF4, 0xEE, 0xBC, 0x0E, 0x13, 0x37, 0xCA, 0x85, 0x9F, 0xB9, 0xA2, 0x0E, 0xF6, 0xE7, 0x49, 0xD1,
      0xD0, 0x11, 0x76, 0x53, 0xA3, 0x73, 0x95, 0x2A, 0x23, 0xC8, 0x0E, 0x97, 0x83, 0x07, 0x64, 0xB2, 0x51, 0xB7, 0xC8,
      0x51, 0x9F, 0xA4, 0x3E, 0x7B, 0xA4, 0x18, 0x6D, 0x99, 0xF0, 0x6E, 0xC3, 0x97, 0xAE, 0xF4, 0xB7, 0x66, 0x37, 0xFA,
      0x65, 0xFC, 0x5E, 0xE2, 0x57, 0xFA, 0x8B, 0x4C, 0x86, 0x10, 0xB4, 0x5C, 0xA4, 0xD2, 0x60, 0x83, 0x69, 0x1E, 0xFF,
      0x36, 0x9B, 0xF9, 0x84, 0xFB, 0xB8, 0x83, 0x64, 0xF1, 0x41, 0xA5, 0x25, 0x56, 0x21, 0xBA, 0x13, 0x98, 0x0C, 0x3B,
      0x04, 0xAA, 0x6C, 0x9A, 0xD4, 0xE3, 0x13, 0x15, 0x54, 0x05, 0x4C, 0x5C, 0xE1, 0x7A, 0x31, 0x5E, 0x90, 0xCF, 0x48,
      0x4E, 0x83, 0xD7, 0x7F, 0xED, 0x93, 0x22, 0xAB, 0x67, 0xE7, 0x76, 0x32, 0x64, 0xBA, 0x5A, 0x21, 0x3E, 0x30, 0x82,
      0x01, 0x41, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x07, 0x01, 0xA0, 0x82, 0x01, 0x32, 0x04, 0x82,
      0x01, 0x2E, 0x30, 0x82, 0x01, 0x2A, 0x30, 0x82, 0x01, 0x26, 0x06, 0x0B, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01,
      0x0C, 0x0A, 0x01, 0x02, 0xA0, 0x81, 0xEF, 0x30, 0x81, 0xEC, 0x30, 0x57, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7,
      0x0D, 0x01, 0x05, 0x0D, 0x30, 0x4A, 0x30, 0x29, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x05, 0x0C,
      0x30, 0x1C, 0x04, 0x08, 0xED, 0x3E, 0xED, 0x07, 0x5C, 0x1F, 0x71, 0xAD, 0x02, 0x02, 0x08, 0x00, 0x30, 0x0C, 0x06,
      0x08, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x02, 0x09, 0x05, 0x00, 0x30, 0x1D, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01,
      0x65, 0x03, 0x04, 0x01, 0x2A, 0x04, 0x10, 0xA7, 0x49, 0xA4, 0x6E, 0x00, 0x19, 0x75, 0x59, 0x75, 0x59, 0xBA, 0x4B,
      0xC7, 0x24, 0x88, 0x34, 0x04, 0x81, 0x90, 0xCA, 0x23, 0x82, 0xAA, 0x16, 0x57, 0x99, 0xFA, 0x94, 0x9F, 0xAE, 0x32,
      0x5C, 0x5B, 0xE7, 0x01, 0xD0, 0xED, 0xA7, 0x58, 0x57, 0x52, 0xBF, 0x57, 0x13, 0xD4, 0x15, 0xB0, 0x06, 0xF5, 0x38,
      0xCC, 0x64, 0x23, 0x09, 0xD5, 0x8C, 0x0D, 0x64, 0x31, 0xFA, 0x74, 0xAA, 0x96, 0x7E, 0x9B, 0x16, 0xCA, 0x21, 0xFD,
      0xC0, 0x54, 0x91, 0x40, 0x7F, 0xB3, 0xF2, 0xA3, 0xEC, 0xA1, 0x4A, 0x07, 0xF0, 0x87, 0x22, 0xDB, 0x8A, 0x49, 0x89,
      0xF7, 0xF2, 0x6A, 0xFC, 0x8D, 0x03, 0x6E, 0x32, 0x4F, 0xD0, 0xD8, 0x93, 0x92, 0xA5, 0xF1, 0x41, 0xBD, 0xEA, 0xE1,
      0x38, 0xA9, 0xD8, 0x9D, 0xAB, 0xB4, 0x8E, 0x4A, 0x40, 0x0E, 0xC7, 0xE3, 0xE9, 0xBF, 0x0E, 0xBA, 0x8D, 0xAA, 0x3E,
      0x93, 0x53, 0x88, 0xEE, 0x0A, 0x2C, 0x71, 0xF1, 0x61, 0x44, 0xA5, 0xAD, 0xED, 0x3E, 0xAB, 0x32, 0x9A, 0x32, 0x85,
      0x08, 0xF5, 0x8B, 0xCC, 0x15, 0x35, 0xEE, 0xFA, 0x17, 0x27, 0x97, 0x8D, 0xD9, 0x1C, 0x5E, 0x74, 0x9D, 0x7B, 0x31,
      0x25, 0x30, 0x23, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x09, 0x15, 0x31, 0x16, 0x04, 0x14, 0x5F,
      0x8E, 0xAB, 0x9C, 0x5F, 0xE2, 0x3B, 0xB1, 0x5C, 0x1A, 0x36, 0x1D, 0x7D, 0xCB, 0x90, 0x45, 0x20, 0x3C, 0x3B, 0xAC,
      0x30, 0x41, 0x30, 0x31, 0x30, 0x0D, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01, 0x05, 0x00,
      0x04, 0x20, 0x93, 0x25, 0xC4, 0x3E, 0x2A, 0x6D, 0x4C, 0x30, 0x87, 0x0F, 0xE3, 0x5A, 0x95, 0xB0, 0xF2, 0x6C, 0xBA,
      0x07, 0x89, 0x7D, 0xFB, 0xCF, 0xCF, 0x1D, 0x54, 0xA3, 0x36, 0x24, 0x7B, 0x30, 0x97, 0xB5, 0x04, 0x08, 0xE7, 0x96,
      0x59, 0xCC, 0x42, 0x9F, 0xEF, 0xFC, 0x02, 0x02, 0x08, 0x00]),
    '123456').then((data) => {
    console.info('createTrustAnchorsWithKeyStore result: success, number of the result = ' + data.length);
  }).catch((err : BusinessError) => {
    console.error(`createTrustAnchorsWithKeyStore failed: errCode: ${err.code}, errMsg: ${err.message}`);
  })
} catch (error) {
  console.error(`createTrustAnchorsWithKeyStore failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### X509CertChain11+

X509证书链对象。

#### getCertList11+

getCertList(): Array<X509Cert>

获取X509证书列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<X509Cert> | X509证书数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19030001 | crypto operation error. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certChainData = '-----BEGIN CERTIFICATE-----\n' +
  'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
  'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
  'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
  'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
  'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
  'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
  'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
  'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
  'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
  'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
  'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
  '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
  'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
  'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
  'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
  'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
  'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
  'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
  'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
  'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
  'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
  '-----END CERTIFICATE-----\n' +
  '-----BEGIN CERTIFICATE-----\n' +
  'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
  'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
  'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
  'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
  'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
  'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
  'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
  'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
  'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
  'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
  'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
  'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
  'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
  'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
  'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
  'uKPWR9dKBA==\n' +
  '-----END CERTIFICATE-----\n' +
  '-----BEGIN CERTIFICATE-----\n' +
  'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
  'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
  'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
  'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
  'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
  'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
  'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
  'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
  'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
  'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
  'xjoE\n' +
  '-----END CERTIFICATE-----\n';

// 证书链二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certChainData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CertChain(encodingBlob, (err, certChain) => {
  if (err) {
    console.error(`createX509CertChain failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('createX509CertChain result: success.');
    try {
      let certList = certChain.getCertList();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`X509CertChain getCertList failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### validate11+

validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>

校验证书链。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | CertChainValidationParameters | 是 | 表示校验X509证书链的参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<CertChainValidationResult> | Promise对象，返回证书链校验结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509CertChain(): Promise<cert.X509CertChain> {
  let certChainData = '-----BEGIN CERTIFICATE-----\n' +
    'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
    'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
    'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
    'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
    'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
    'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
    'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
    'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
    'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
    'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
    'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
    '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
    'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
    'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
    'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
    'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
    'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
    'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
    'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
    'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
    'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
    '-----END CERTIFICATE-----\n' +
    '-----BEGIN CERTIFICATE-----\n' +
    'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
    'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
    'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
    'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
    'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
    'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
    'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
    'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
    'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
    'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
    'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
    'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
    'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
    'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
    'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
    'uKPWR9dKBA==\n' +
    '-----END CERTIFICATE-----\n' +
    '-----BEGIN CERTIFICATE-----\n' +
    'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
    'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
    'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
    'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
    'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
    'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
    'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
    'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
    'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
    'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
    'xjoE\n' +
    '-----END CERTIFICATE-----\n';

  // 证书链二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certChainData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
  try {
    x509CertChain = await cert.createX509CertChain(encodingBlob);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509CertChain;
}

async function validate() {
  const certChain = await createX509CertChain();
  // 证书链校验数据，需业务自行赋值。
  const param: cert.CertChainValidationParameters = {
    date: '20231212080000Z',
    trustAnchors: [{
      CAPubKey: new Uint8Array([0x30, 0x2a, 0x30, 0x05, 0x06, 0x03, 0x2b, 0x65, 0x70, 0x03, 0x21, 0x00, 0xbb, 0x16,
        0x9d, 0x8f, 0x5c, 0x30, 0xd0, 0xba, 0x8f, 0x37, 0x6e, 0x33, 0xaf, 0x6f, 0x23, 0x71, 0x23, 0xa5, 0x49, 0x60,
        0x1e, 0xd1, 0x07, 0x4b, 0xc9, 0x11, 0x7e, 0x66, 0x01, 0xba, 0x92, 0x52]),
      CASubject: new Uint8Array([0x30, 0x5a, 0x31, 0x0b, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x45,
        0x4e, 0x31, 0x10, 0x30, 0x0e, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x45, 0x6e, 0x67, 0x6c, 0x61, 0x6e,
        0x64, 0x31, 0x0f, 0x30, 0x0d, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x06, 0x4c, 0x6f, 0x6e, 0x64, 0x6f, 0x6e,
        0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0a, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a,
        0x06, 0x03, 0x55, 0x04, 0x0b, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04,
        0x03, 0x13, 0x03, 0x74, 0x73, 0x31]),
    }]
  }
  try {
    const validationRes = await certChain.validate(param);
    console.info('X509CertChain validate result: success.');
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`X509CertChain validate failed, errCode: ${e.code}, errMsg: ${e.message}`);
}

validate();
```

#### validate11+

validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void

使用校验参数校验证书链。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | CertChainValidationParameters | 是 | 表示校验X509证书链的参数。 |
| callback | AsyncCallback<CertChainValidationResult> | 是 | 回调函数，返回证书链校验结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certChainData = '-----BEGIN CERTIFICATE-----\n' +
  'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
  'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
  'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
  'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
  'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
  'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
  'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
  'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
  'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
  'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
  'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
  '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
  'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
  'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
  'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
  'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
  'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
  'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
  'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
  'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
  'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
  '-----END CERTIFICATE-----\n' +
  '-----BEGIN CERTIFICATE-----\n' +
  'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
  'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
  'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
  'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
  'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
  'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
  'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
  'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
  'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
  'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
  'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
  'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
  'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
  'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
  'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
  'uKPWR9dKBA==\n' +
  '-----END CERTIFICATE-----\n' +
  '-----BEGIN CERTIFICATE-----\n' +
  'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
  'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
  'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
  'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
  'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
  'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
  'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
  'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
  'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
  'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
  'xjoE\n' +
  '-----END CERTIFICATE-----\n';

// 证书链二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certChainData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

// 证书链校验数据，需业务自行赋值。
let param: cert.CertChainValidationParameters = {
  date: '20231212080000Z',
  trustAnchors: [{
    CAPubKey: new Uint8Array([0x30, 0x2a, 0x30, 0x05, 0x06, 0x03, 0x2b, 0x65, 0x70, 0x03, 0x21, 0x00, 0xbb, 0x16, 0x9d,
      0x8f, 0x5c, 0x30, 0xd0, 0xba, 0x8f, 0x37, 0x6e, 0x33, 0xaf, 0x6f, 0x23, 0x71, 0x23, 0xa5, 0x49, 0x60, 0x1e, 0xd1,
      0x07, 0x4b, 0xc9, 0x11, 0x7e, 0x66, 0x01, 0xba, 0x92, 0x52]),
    CASubject: new Uint8Array([0x30, 0x5a, 0x31, 0x0b, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x45, 0x4e,
      0x31, 0x10, 0x30, 0x0e, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x45, 0x6e, 0x67, 0x6c, 0x61, 0x6e, 0x64, 0x31,
      0x0f, 0x30, 0x0d, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x06, 0x4c, 0x6f, 0x6e, 0x64, 0x6f, 0x6e, 0x31, 0x0c, 0x30,
      0x0a, 0x06, 0x03, 0x55, 0x04, 0x0a, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04,
      0x0b, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x03, 0x13, 0x03, 0x74, 0x73,
      0x31]),
  }]
};

cert.createX509CertChain(encodingBlob, (err, certChain) => {
  if (err) {
    console.error(`createX509CertChain failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('createX509CertChain result: success.');
    certChain.validate(param, (error, validationRes) => {
      if (error) {
        console.error(`X509CertChain validate failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        console.info('X509CertChain validate result: success.');
      }
    });
  }
});
```

#### toString12+

toString(): string

获取对象的字符串类型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 对象的字符串类型数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certChainData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIGVjCCBT6gAwIBAgIQBMO0W3CU9LWVw1bE/jqYojANBgkqhkiG9w0BAQsFADBE\n' +
  'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMR4wHAYDVQQDExVH\n' +
  'ZW9UcnVzdCBSU0EgQ04gQ0EgRzIwHhcNMjMwMzIzMDAwMDAwWhcNMjQwNDIyMjM1\n' +
  'OTU5WjB1MQswCQYDVQQGEwJDTjERMA8GA1UECBMIemhlamlhbmcxETAPBgNVBAcT\n' +
  'CGhhbmd6aG91MSwwKgYDVQQKEyNOZXRFYXNlIChIYW5nemhvdSkgTmV0d29yayBD\n' +
  'by4sIEx0ZDESMBAGA1UEAwwJKi4xNjMuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC\n' +
  'AQ8AMIIBCgKCAQEAwELks0Q1Z81u1OpbGdEFE2Snm/WpLfmiC5YFj5nFrinSX+UZ\n' +
  'MIk42euBdjYSsWFxbljmWDdUCjstMhG8vRAjz3Nt1QniMCunHHFGujR5rSNLWYHE\n' +
  'vCPhfptIhqOaE/rvkWGZZr2KjTQQN0dRf8dm9Oewy8DHu95c9jW6c9AVgKWUVOni\n' +
  'tTOcJCnrndWjgCIPfKmKgrwaNaMnuQyy5nPIUHl/5EGzuGHrwjwlF+w+cT+Fwdix\n' +
  'C3msEOCwX6wzo6baDs4og2EzuPNyTp4n4UqH5aHhLePgBFboOAyJwWp3+XJNpNGw\n' +
  'GkU56cUUy7+AAn268EVvUNr7uQ65t2t+Ys32bQIDAQABo4IDETCCAw0wHwYDVR0j\n' +
  'BBgwFoAUJG+RP4mHhw4ywkAY38VM60/ISTIwHQYDVR0OBBYEFD1HyRYJ5jqkvYL7\n' +
  'C6TSt8/y3e7hMB0GA1UdEQQWMBSCCSouMTYzLmNvbYIHMTYzLmNvbTAOBgNVHQ8B\n' +
  'Af8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMD0GA1UdHwQ2\n' +
  'MDQwMqAwoC6GLGh0dHA6Ly9jcmwuZGlnaWNlcnQuY24vR2VvVHJ1c3RSU0FDTkNB\n' +
  'RzIuY3JsMD4GA1UdIAQ3MDUwMwYGZ4EMAQICMCkwJwYIKwYBBQUHAgEWG2h0dHA6\n' +
  'Ly93d3cuZGlnaWNlcnQuY29tL0NQUzBxBggrBgEFBQcBAQRlMGMwIwYIKwYBBQUH\n' +
  'MAGGF2h0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNuMDwGCCsGAQUFBzAChjBodHRwOi8v\n' +
  'Y2FjZXJ0cy5kaWdpY2VydC5jbi9HZW9UcnVzdFJTQUNOQ0FHMi5jcnQwCQYDVR0T\n' +
  'BAIwADCCAX4GCisGAQQB1nkCBAIEggFuBIIBagFoAHUA7s3QZNXbGs7FXLedtM0T\n' +
  'ojKHRny87N7DUUhZRnEftZsAAAGHDSE15QAABAMARjBEAiBRpmsJ3F9AI8wFxqOQ\n' +
  'bHp+RL6F8cvNydajQ0Bqxjvd3AIgefAU/po3jBm+96dFVdbX+AG1uss67DL3VL5I\n' +
  'nUmVva8AdgBz2Z6JG0yWeKAgfUed5rLGHNBRXnEZKoxrgBB6wXdytQAAAYcNITZS\n' +
  'AAAEAwBHMEUCID/sUP12odF7uTTEyE0PjCpKo3nF7A3ba3b5wJJsZrDrAiEAxrat\n' +
  'W2eeZTD458LPSPrMMBb1/o6zibWXqJCQye+bVFwAdwBIsONr2qZHNA/lagL6nTDr\n' +
  'HFIBy1bdLIHZu7+rOdiEcwAAAYcNITYeAAAEAwBIMEYCIQCCJ2ktM1F+d1I5mQju\n' +
  'Tn7oDYxy3GCGyG3u/yhu8k7EaAIhANSP8cAaMQFV6y8B2tubKY5eSQtgkF3a6NNq\n' +
  'QJjtPnoHMA0GCSqGSIb3DQEBCwUAA4IBAQC8dK/G4nvs/SyQe/mnK+rUYIdSFs+4\n' +
  'lgzatmq8V/I1tBly+Sv/FPhnn4F3iCrqy9j8y202FP51ev95DGbjlJRTIFPqVAO8\n' +
  'ywYrLhvl1SJhV0b/8NF0Pr3dZVnK5Vfn11+LSBUg0cBB2hcVV30nv3IuVhz3d12n\n' +
  'P+VseYQgMpQf7ad+ttpZtA7yqHzrUm4fzr03G7q88GztACRSHoYiPbOlz99SeTgW\n' +
  '7bzZl1I4taxy2Q3b0ZBGfUt/kPY05tpKzKwDTbbqSErYszCt5X1RfVvf3coxF8Mo\n' +
  '9bHbs2wYIzQBdujDQ/hU0u6ItERer3SUItZoxaSIxdrZ9eXFwVvXsT/g\n' +
  '-----END CERTIFICATE-----\n' +
  '-----BEGIN CERTIFICATE-----\n' +
  'MIIFDzCCA/egAwIBAgIQCxNitu5qnT6WiTDxbiB9OTANBgkqhkiG9w0BAQsFADBh\n' +
  'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\n' +
  'd3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBD\n' +
  'QTAeFw0yMDAzMDQxMjA0NDBaFw0zMDAzMDQxMjA0NDBaMEQxCzAJBgNVBAYTAlVT\n' +
  'MRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxHjAcBgNVBAMTFUdlb1RydXN0IFJTQSBD\n' +
  'TiBDQSBHMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANA1OZJJtZUI\n' +
  '7zj4qFHT79g+Otks4TEfmUEDhrNKBEEjb/i29GBfnpvFdT36azCg2VODJRSjIzFn\n' +
  '4qADcc84EmfKiDEM97HFsQPp9RRkqxH5cB51EU2eBE9Ua95x+wQp/KSdCqITCQ/v\n' +
  'yvm3J4Upjl0wlW8wRCPCWcYw3pKClGRkNzVtI1KXnfpn7fG3N84n7wlBb9IGKJFa\n' +
  'c/6+hxvZx2qnfLsxdIKR0Q/biGoU6Z8Iy/R/p7GoPO8vamV090+QHEL5AdSzKtEh\n' +
  'U9vdvcuWjjLxVnaJLfj/6WoGZj8UWn3zFbEoTVaAfp2xqdzW7yRvi2r148m9ev7l\n' +
  'jDqHo8UX69sCAwEAAaOCAd4wggHaMB0GA1UdDgQWBBQkb5E/iYeHDjLCQBjfxUzr\n' +
  'T8hJMjAfBgNVHSMEGDAWgBQD3lA1VtFMu2bwo+IbG8OXsj3RVTAOBgNVHQ8BAf8E\n' +
  'BAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQI\n' +
  'MAYBAf8CAQAwMwYIKwYBBQUHAQEEJzAlMCMGCCsGAQUFBzABhhdodHRwOi8vb2Nz\n' +
  'cC5kaWdpY2VydC5jbjBABgNVHR8EOTA3MDWgM6Axhi9odHRwOi8vY3JsLmRpZ2lj\n' +
  'ZXJ0LmNuL0RpZ2lDZXJ0R2xvYmFsUm9vdENBLmNybDCB3QYDVR0gBIHVMIHSMIHF\n' +
  'BglghkgBhv1sAQEwgbcwKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LmRpZ2ljZXJ0\n' +
  'LmNvbS9DUFMwgYoGCCsGAQUFBwICMH4MfEFueSB1c2Ugb2YgdGhpcyBDZXJ0aWZp\n' +
  'Y2F0ZSBjb25zdGl0dXRlcyBhY2NlcHRhbmNlIG9mIHRoZSBSZWx5aW5nIFBhcnR5\n' +
  'IEFncmVlbWVudCBsb2NhdGVkIGF0IGh0dHBzOi8vd3d3LmRpZ2ljZXJ0LmNvbS9y\n' +
  'cGEtdWEwCAYGZ4EMAQICMA0GCSqGSIb3DQEBCwUAA4IBAQCzkcXq0TN0oSn4UeXp\n' +
  'FBW7U8zrHBIhH9MXHNBp+Yy/yN19133UY05uuHXHaU2Uv0hxefckjPdkaX7ARso+\n' +
  'O3Ar6nf7YfBwCqSpqsNckKT7KKtf3Ot95wYFpKDa64jcRUfxzRWnmq12IVzczqHI\n' +
  'sIvUZQINw/UHSQcWekdUnMg58bQSHyTjwkj9jcX2RURxaVZkr15wxo/Z3Ydo2PVK\n' +
  '3afEr0/vcuFvE7QeGXiI2DJdVt3JefatZ3rj4VTW2aUZwHGUiWWIUudBfQKR0JEp\n' +
  'lJ8MFaKDh4/A2VEJnXILu1iwvc1m3jCaPuzZKdoHM/1234bznJI2aAfhfIhoHw90\n' +
  'tPO+\n' +
  '-----END CERTIFICATE-----\n';

// 证书链二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certChainData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function certChainToString() {
  let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
  try {
    x509CertChain = await cert.createX509CertChain(encodingBlob);
    console.info('createX509CertChain result: success.');
    console.info('toString success: ' + x509CertChain.toString());
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### hashCode12+

hashCode(): Uint8Array

获取DER格式数据的哈希值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | DER格式数据的哈希值。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let certChainData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIGVjCCBT6gAwIBAgIQBMO0W3CU9LWVw1bE/jqYojANBgkqhkiG9w0BAQsFADBE\n' +
  'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMR4wHAYDVQQDExVH\n' +
  'ZW9UcnVzdCBSU0EgQ04gQ0EgRzIwHhcNMjMwMzIzMDAwMDAwWhcNMjQwNDIyMjM1\n' +
  'OTU5WjB1MQswCQYDVQQGEwJDTjERMA8GA1UECBMIemhlamlhbmcxETAPBgNVBAcT\n' +
  'CGhhbmd6aG91MSwwKgYDVQQKEyNOZXRFYXNlIChIYW5nemhvdSkgTmV0d29yayBD\n' +
  'by4sIEx0ZDESMBAGA1UEAwwJKi4xNjMuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC\n' +
  'AQ8AMIIBCgKCAQEAwELks0Q1Z81u1OpbGdEFE2Snm/WpLfmiC5YFj5nFrinSX+UZ\n' +
  'MIk42euBdjYSsWFxbljmWDdUCjstMhG8vRAjz3Nt1QniMCunHHFGujR5rSNLWYHE\n' +
  'vCPhfptIhqOaE/rvkWGZZr2KjTQQN0dRf8dm9Oewy8DHu95c9jW6c9AVgKWUVOni\n' +
  'tTOcJCnrndWjgCIPfKmKgrwaNaMnuQyy5nPIUHl/5EGzuGHrwjwlF+w+cT+Fwdix\n' +
  'C3msEOCwX6wzo6baDs4og2EzuPNyTp4n4UqH5aHhLePgBFboOAyJwWp3+XJNpNGw\n' +
  'GkU56cUUy7+AAn268EVvUNr7uQ65t2t+Ys32bQIDAQABo4IDETCCAw0wHwYDVR0j\n' +
  'BBgwFoAUJG+RP4mHhw4ywkAY38VM60/ISTIwHQYDVR0OBBYEFD1HyRYJ5jqkvYL7\n' +
  'C6TSt8/y3e7hMB0GA1UdEQQWMBSCCSouMTYzLmNvbYIHMTYzLmNvbTAOBgNVHQ8B\n' +
  'Af8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMD0GA1UdHwQ2\n' +
  'MDQwMqAwoC6GLGh0dHA6Ly9jcmwuZGlnaWNlcnQuY24vR2VvVHJ1c3RSU0FDTkNB\n' +
  'RzIuY3JsMD4GA1UdIAQ3MDUwMwYGZ4EMAQICMCkwJwYIKwYBBQUHAgEWG2h0dHA6\n' +
  'Ly93d3cuZGlnaWNlcnQuY29tL0NQUzBxBggrBgEFBQcBAQRlMGMwIwYIKwYBBQUH\n' +
  'MAGGF2h0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNuMDwGCCsGAQUFBzAChjBodHRwOi8v\n' +
  'Y2FjZXJ0cy5kaWdpY2VydC5jbi9HZW9UcnVzdFJTQUNOQ0FHMi5jcnQwCQYDVR0T\n' +
  'BAIwADCCAX4GCisGAQQB1nkCBAIEggFuBIIBagFoAHUA7s3QZNXbGs7FXLedtM0T\n' +
  'ojKHRny87N7DUUhZRnEftZsAAAGHDSE15QAABAMARjBEAiBRpmsJ3F9AI8wFxqOQ\n' +
  'bHp+RL6F8cvNydajQ0Bqxjvd3AIgefAU/po3jBm+96dFVdbX+AG1uss67DL3VL5I\n' +
  'nUmVva8AdgBz2Z6JG0yWeKAgfUed5rLGHNBRXnEZKoxrgBB6wXdytQAAAYcNITZS\n' +
  'AAAEAwBHMEUCID/sUP12odF7uTTEyE0PjCpKo3nF7A3ba3b5wJJsZrDrAiEAxrat\n' +
  'W2eeZTD458LPSPrMMBb1/o6zibWXqJCQye+bVFwAdwBIsONr2qZHNA/lagL6nTDr\n' +
  'HFIBy1bdLIHZu7+rOdiEcwAAAYcNITYeAAAEAwBIMEYCIQCCJ2ktM1F+d1I5mQju\n' +
  'Tn7oDYxy3GCGyG3u/yhu8k7EaAIhANSP8cAaMQFV6y8B2tubKY5eSQtgkF3a6NNq\n' +
  'QJjtPnoHMA0GCSqGSIb3DQEBCwUAA4IBAQC8dK/G4nvs/SyQe/mnK+rUYIdSFs+4\n' +
  'lgzatmq8V/I1tBly+Sv/FPhnn4F3iCrqy9j8y202FP51ev95DGbjlJRTIFPqVAO8\n' +
  'ywYrLhvl1SJhV0b/8NF0Pr3dZVnK5Vfn11+LSBUg0cBB2hcVV30nv3IuVhz3d12n\n' +
  'P+VseYQgMpQf7ad+ttpZtA7yqHzrUm4fzr03G7q88GztACRSHoYiPbOlz99SeTgW\n' +
  '7bzZl1I4taxy2Q3b0ZBGfUt/kPY05tpKzKwDTbbqSErYszCt5X1RfVvf3coxF8Mo\n' +
  '9bHbs2wYIzQBdujDQ/hU0u6ItERer3SUItZoxaSIxdrZ9eXFwVvXsT/g\n' +
  '-----END CERTIFICATE-----\n' +
  '-----BEGIN CERTIFICATE-----\n' +
  'MIIFDzCCA/egAwIBAgIQCxNitu5qnT6WiTDxbiB9OTANBgkqhkiG9w0BAQsFADBh\n' +
  'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\n' +
  'd3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBD\n' +
  'QTAeFw0yMDAzMDQxMjA0NDBaFw0zMDAzMDQxMjA0NDBaMEQxCzAJBgNVBAYTAlVT\n' +
  'MRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxHjAcBgNVBAMTFUdlb1RydXN0IFJTQSBD\n' +
  'TiBDQSBHMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANA1OZJJtZUI\n' +
  '7zj4qFHT79g+Otks4TEfmUEDhrNKBEEjb/i29GBfnpvFdT36azCg2VODJRSjIzFn\n' +
  '4qADcc84EmfKiDEM97HFsQPp9RRkqxH5cB51EU2eBE9Ua95x+wQp/KSdCqITCQ/v\n' +
  'yvm3J4Upjl0wlW8wRCPCWcYw3pKClGRkNzVtI1KXnfpn7fG3N84n7wlBb9IGKJFa\n' +
  'c/6+hxvZx2qnfLsxdIKR0Q/biGoU6Z8Iy/R/p7GoPO8vamV090+QHEL5AdSzKtEh\n' +
  'U9vdvcuWjjLxVnaJLfj/6WoGZj8UWn3zFbEoTVaAfp2xqdzW7yRvi2r148m9ev7l\n' +
  'jDqHo8UX69sCAwEAAaOCAd4wggHaMB0GA1UdDgQWBBQkb5E/iYeHDjLCQBjfxUzr\n' +
  'T8hJMjAfBgNVHSMEGDAWgBQD3lA1VtFMu2bwo+IbG8OXsj3RVTAOBgNVHQ8BAf8E\n' +
  'BAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQI\n' +
  'MAYBAf8CAQAwMwYIKwYBBQUHAQEEJzAlMCMGCCsGAQUFBzABhhdodHRwOi8vb2Nz\n' +
  'cC5kaWdpY2VydC5jbjBABgNVHR8EOTA3MDWgM6Axhi9odHRwOi8vY3JsLmRpZ2lj\n' +
  'ZXJ0LmNuL0RpZ2lDZXJ0R2xvYmFsUm9vdENBLmNybDCB3QYDVR0gBIHVMIHSMIHF\n' +
  'BglghkgBhv1sAQEwgbcwKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LmRpZ2ljZXJ0\n' +
  'LmNvbS9DUFMwgYoGCCsGAQUFBwICMH4MfEFueSB1c2Ugb2YgdGhpcyBDZXJ0aWZp\n' +
  'Y2F0ZSBjb25zdGl0dXRlcyBhY2NlcHRhbmNlIG9mIHRoZSBSZWx5aW5nIFBhcnR5\n' +
  'IEFncmVlbWVudCBsb2NhdGVkIGF0IGh0dHBzOi8vd3d3LmRpZ2ljZXJ0LmNvbS9y\n' +
  'cGEtdWEwCAYGZ4EMAQICMA0GCSqGSIb3DQEBCwUAA4IBAQCzkcXq0TN0oSn4UeXp\n' +
  'FBW7U8zrHBIhH9MXHNBp+Yy/yN19133UY05uuHXHaU2Uv0hxefckjPdkaX7ARso+\n' +
  'O3Ar6nf7YfBwCqSpqsNckKT7KKtf3Ot95wYFpKDa64jcRUfxzRWnmq12IVzczqHI\n' +
  'sIvUZQINw/UHSQcWekdUnMg58bQSHyTjwkj9jcX2RURxaVZkr15wxo/Z3Ydo2PVK\n' +
  '3afEr0/vcuFvE7QeGXiI2DJdVt3JefatZ3rj4VTW2aUZwHGUiWWIUudBfQKR0JEp\n' +
  'lJ8MFaKDh4/A2VEJnXILu1iwvc1m3jCaPuzZKdoHM/1234bznJI2aAfhfIhoHw90\n' +
  'tPO+\n' +
  '-----END CERTIFICATE-----\n';

// 证书链二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certChainData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

async function certChainHashCode() {
  let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
  try {
    x509CertChain = await cert.createX509CertChain(encodingBlob);
    console.info('createX509CertChain result: success.');
    console.info('hashCode success: ' + x509CertChain.hashCode());
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cert.generateCsr18+

generateCsr(keyInfo: PrivateKeyInfo, config: CsrGenerationConfig): string | Uint8Array

表示使用指定的RSA私钥，传入主体、扩展、摘要算法、输出格式等配置参数去生成CSR。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyInfo | PrivateKeyInfo | 是 | 包含私钥跟口令的配置参数。 |
| config | CsrGenerationConfig | 是 | 包含生成CSR的配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Uint8Array | 表示生成的CSR数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030008 | maybe wrong password. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function createCsrTest() {
  let nameStr = '/CN=John Doe/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS';
  let prikeyEnstr: string =
    '-----BEGIN RSA PRIVATE KEY-----\n'                                  +
      'Proc-Type: 4,ENCRYPTED\n'                                           +
      'DEK-Info: AES-128-CBC,B5FFA3AEEE7176106FDDB0988B532F07\n\n'         +
      't3zNRGKp5X4BNkcsYATad/Le+94yMIX9CoNAGsBIDzQw+773UMGIoeGEYVlXWc8x\n' +
      'N1XWDinn4ytWw9x9OfUYgmNnrdkWRSaIuw+SpQfBgJip+MsNERYOHZ5TYWTR8n3k\n' +
      '7/jHY8eCgTsP3hbNtyaePIrtbTLZGZAHG1YWY5UmLaYoI1O6/Vvobx72lx3b43Tx\n' +
      '4j5lkknpLl85fcs1s4TYMOd8vEwhdpouR4VY8kfRSm44WQLtGXrce0An3MG3pXyZ\n' +
      'GhpmJyTcg0epTEYVzglENlBJrBVDL+bJ8uvHGH4tmeQb77e6ILXoxZntM7zQMMFo\n' +
      'A7dilqO6FBxu20n2TidVGCa0Yn+DZLpry2OdwVUC2nXyCHCehr3jAZz6k20FWg5B\n' +
      'EsU16yOIB+bp9BUKdTpJVtc/pmZJtnlA9pSCUVmWdltOsjjxkE94wfAUOYhO3Mvz\n' +
      'gF9KR1/bdAbLw4t7bGeuyV4N2iYr83FodLLXpupM6Qfb51+HVgHvm2aaHv2Q4sf3\n' +
      'poCVTNlegoVV9x3+7HqXY6MjlG8aU6LcWqH34ySqRBQrKL1PuDzQSY5/RmP7PUhG\n' +
      'ym4l6KbEaRC2H/XS2qKa4VCMgBCgA0hoiw4s48Xd4h2GUTuxLM9wGyW89OEaHky7\n' +
      'VE7t3O9a2zhkRTYDDYQ8QCycKhNrsKySyItRUWn/w2lXvuKM7PpAzYH7Ey3W1eZG\n' +
      'PyyeGG9exjpdIvD3tx5Hl/OWwBkW1DAzO40gT6sdD5FXzRv4fCHuCrIow5QMLF4T\n' +
      'd5Y4a6q13V4O5b73T5INmKl8rEbPGIw7WLR7BNj05QuzNcn5kA1aBFIJqsxQv46l\n' +
      '-----END RSA PRIVATE KEY-----\n';
  let priKeyInfo: cert.PrivateKeyInfo = {
    key: prikeyEnstr,
    password: '123abc'
  }
  let keyUsage: cert.CsrAttribute = {
    type: 'keyUsage',
    value: 'digitalSignature, keyEncipherment'
  };

  let challengePassword: cert.CsrAttribute = {
    type: 'challengePassword',
    value: '123456'
  };
  let attribute: cert.CsrAttribute[] = [
    keyUsage,challengePassword
  ];
  try {
    let data = await cert.createX500DistinguishedName(nameStr);
    console.info('createX500DistinguishedName result: success. ' + data.getName('CN').toString());
    let conf: cert.CsrGenerationConfig = {
      subject: data,
      mdName: 'SHA256',
      outFormat: cert.EncodingBaseFormat.PEM,
      attributes: attribute
    }
    try {
      let csrStr = cert.generateCsr(priKeyInfo, conf)
      console.info('generateCsr result: success, return str is ' + csrStr.toString())
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`generateCsr failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cert.createX500DistinguishedName12+

createX500DistinguishedName(nameStr: string): Promise<X500DistinguishedName>

表示使用字符串格式的名称创建X500DistinguishedName对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nameStr | string | 是 | X509定义的Name字符串格式，使用斜杠'/'进行分割可分辨名称，每个可分辨名称为“属性=值”形式，常用属性包括CN（通用名）、O（组织名）、OU（组织单位）、C（国家/地区）、ST（省/州）、L（市/区）。例如：/CN=example.com/O=Example/C=CN。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<X500DistinguishedName> | 表示X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let nameStr = '/CN=John Doe/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS';
async function createX500DistinguishedName() {
  try {
    cert.createX500DistinguishedName(nameStr)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      })
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cert.createX500DistinguishedName12+

createX500DistinguishedName(nameDer: Uint8Array): Promise<X500DistinguishedName>

表示使用DER格式的名称创建X500DistinguishedName对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nameDer | Uint8Array | 是 | X509定义的Uint8Array类型的DER格式数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<X500DistinguishedName> | 表示X509的可分辨对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030002 | the certificate signature verification failed. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |
| 19030006 | the key cannot be used for signing a certificate. |
| 19030007 | the key cannot be used for digital signature. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameDer =
  new Uint8Array([48, 41, 49, 11, 48, 9, 6, 3, 85, 4, 3, 12, 2, 67, 65, 49, 13, 48, 11, 6, 3, 85, 4, 10, 12, 4, 116,
    101, 115, 116, 49, 11, 48, 9, 6, 3, 85, 4, 6, 19, 2, 67, 78]);

async function createX500DistinguishedName() {
  try {
    cert.createX500DistinguishedName(nameDer)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      })
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### X500DistinguishedName12+

X509定义的Name类型的对象。

#### getName12+

getName(): string

获取可分辨名的字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 可分辨名的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameDer =
  new Uint8Array([48, 41, 49, 11, 48, 9, 6, 3, 85, 4, 3, 12, 2, 67, 65, 49, 13, 48, 11, 6, 3, 85, 4, 10, 12, 4, 116,
    101, 115, 116, 49, 11, 48, 9, 6, 3, 85, 4, 6, 19, 2, 67, 78]);

async function getName() {
  try {
    cert.createX500DistinguishedName(nameDer)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
        console.info('createX500DistinguishedName getName: ' + data.getName());
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      })
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getName12+

getName(type: string): Array<string>

按类型获取可分辨名的字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 指定类型的名称。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<string> | 可分辨名的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=XTS';
async function getName() {
  try {
    cert.createX500DistinguishedName(nameStr)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
        console.info('createX500DistinguishedName getName: ' + data.getName("CN"));
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      })
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getName20+

getName(encodingType: EncodingType): string

根据指定的编码类型获取可分辨名的字符串。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | EncodingType | 是 | 表示编码类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示可分辨名的字符串，使用逗号分隔相对可分辨名称。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The value of encodingType is not in the EncodingType enumeration range. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameStr = '/CN=陕西@西安/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS';
async function getName() {
  try {
    cert.createX500DistinguishedName(nameStr)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
        console.info('createX500DistinguishedName getName: ' + data.getName(cert.EncodingType.ENCODING_UTF8));
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      })
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getEncoded12+

getEncoded(): EncodingBlob

获取X509证书扩展域的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值**：

| 类型 | 说明 |
| --- | --- |
| EncodingBlob | X509证书序列化数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=XTS';
async function getEncoded() {
  try {
    cert.createX500DistinguishedName(nameStr)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
        let encodingBlobData = data.getEncoded();
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      })
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cert.createCmsGenerator18+

createCmsGenerator(contentType: CmsContentType): CmsGenerator

表示创建CmsGenerator对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contentType | CmsContentType | 是 | 指定CMS内容类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CmsGenerator | CmsGenerator对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
  'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
  'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
  'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
  'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
  'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
  'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
  '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
  'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
  'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
  'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
  'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
  'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
  '-----END CERTIFICATE-----\n';

// string转Uint8Array
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function testcreateCmsGenerator() {
  let certEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
    if (error) {
      console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
    } else {
        try {
          let cmsContentType = cert.CmsContentType.SIGNED_DATA;
          let cmsGenerator = cert.createCmsGenerator(cmsContentType);
          console.info('testcreateCmsGenerator createCmsGenerator result: success.');
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          console.error(`createCmsGenerator failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  });
}
```

#### CmsGenerator18+

CmsGenerator对象用于生成CMS（Cryptographic Message Syntax）格式的消息。

PKCS#7是用于存储签名或加密数据的标准语法。注意CMS是PKCS#7的扩展，PKCS#7支持的数据类型包括数据、签名数据、信封数据、

签名和信封数据、摘要数据、加密数据。常用于保护数据的完整性和机密性。

#### addSigner18+

addSigner(cert: X509Cert, keyInfo: PrivateKeyInfo, config: CmsSignerConfig): void;

用于为内容类型为SIGNED_DATA的CMS添加签名者信息。

由于openssl不支持自签名证书的验签操作，因此自签名证书不能作为签名者。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | X509Cert | 是 | 指定X509证书。 |
| keyInfo | PrivateKeyInfo | 是 | 指定私钥信息。 |
| config | CmsSignerConfig | 是 | 指定签名者选项。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19030001 | crypto operation error. |
| 19030008 | maybe wrong password. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
  'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
  'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
  'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
  'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
  'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
  'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
  '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
  'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
  'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
  'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
  'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
  'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
  '-----END CERTIFICATE-----\n';

let rsaStr1024: string  =
  '-----BEGIN RSA PRIVATE KEY-----\n' +
    'Proc-Type: 4,ENCRYPTED\n' +
    'DEK-Info: DES-EDE3-CBC,DB0AC6E3BEE16420\n\n' +
    '1N5xykdckthZnswMV7blxXm2RCqe/OByBfMwFI7JoXR8STtMiStd4xA3W405k1Ma\n' +
    'ExpsHgWwZaS23x+sQ1sL1dsqIPMrw1Vr+KrL20vQcCVjXPpGKauafVbtcWQ1r2PZ\n' +
    'QJ4KWP6FhUp+sGt2ItODW3dK+1GdqL22ZtANrgFzS42Wh8FSn0UMCf6RG62DK62J\n' +
    'z2jtf4XaorrGSjdTeY+fyyGfSyKidIMMBe+IXwlhCgAe7aHSaqXtMsv+BibB7PJ3\n' +
    'XmEp1D/0ptL3r46txyYcuy8jSNCkW8er93KKnlRN6KbuYZPvPNncWkzZBzV17t5d\n' +
    'QgtvVh32AKgqk5jm8YVnspOFiPrbrK9UN3IW15juFkfnhriM3IrKap4/kW+tfawZ\n' +
    'DmHkSyl8xqFK413Rv0UvYBTjOcGbs2BSJYEvp8CIjtA17SvLmNw70K2nXWuQYutY\n' +
    '+HyucPtHfEqUPQRzWTAMMntTru77u7dxo2WMMMxOtMJO5h7MAnZH9bAFiuO3ewcY\n' +
    'eEePg10d8Owcfh9G6kc0HIGT9MMLMi0mTXhpoQTuWPYuSx6uUZL1fsp1x2fuM0qn\n' +
    'bdf3+UnATYUu4tgvBHrMV7405Y6Y3PnqOFxVMeAHeOTo6UThtJ10mfeCPXGcUaHo\n' +
    'P5enw7h4145cha3+S4hNrUwj3skrtavld7tY74p4DvgZSlCMF3JAm3DhpnEMVcYP\n' +
    'Y6TkSevvxOpBvEHE41Y4VBCBwd9clcixI6cSBJKPUU4A/sc/kkNdGFcbzLQCg/zR\n' +
    '1m7YmBROb2qy4w3lv/uwVnPGLg/YV465irRaN3hgz7/1lm8STKQhmQ==\n' +
    '-----END RSA PRIVATE KEY-----\n';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function testAddSigner() {
  let certEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
    if (error) {
      console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
    } else {
        try {
          let cmsContentType = cert.CmsContentType.SIGNED_DATA;
          let cmsGenerator = cert.createCmsGenerator(cmsContentType);
          console.info('testAddSigner createCmsGenerator result: success.');
          let privateKeyInfo: cert.PrivateKeyInfo = {
            key: rsaStr1024,
            password: '123456'
          };
          // addCert设置为true时，第二次addSigner增加相同的证书，会报错。
          let config: cert.CmsSignerConfig = {
            mdName:'SHA256',
            addCert:false,
            addAttr:false,
            addSmimeCapAttr:false
          }
          cmsGenerator.addSigner(x509Cert, privateKeyInfo, config);
          console.info('testAddSigner addSigner result: success.');
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          console.error(`testAddSigner failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  });
}
```

#### addCert18+

addCert(cert: X509Cert): void

用于添加内容类型为SIGNED_DATA的CMS的证书，例如签名证书的颁发者证书。

如果未调用addSigner接口，并且仅添加证书后，生成的CMS签名数据将只包含证书。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | X509Cert | 是 | 要添加的X509证书。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
  'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
  'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
  'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
  'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
  'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
  'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
  '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
  'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
  'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
  'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
  'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
  'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
  '-----END CERTIFICATE-----\n';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function testAddCert() {
  let certEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
    if (error) {
      console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
    } else {
        try {
          let cmsContentType = cert.CmsContentType.SIGNED_DATA;
          let cmsGenerator = cert.createCmsGenerator(cmsContentType);
          console.info('testAddCert createCmsGenerator result: success.');
          // 第二次addCert增加相同的证书，会报错。
          cmsGenerator.addCert(x509Cert);
          console.info('testAddCert addCert result: success.');
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          console.error(`testAddCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  });
}
```

#### setRecipientEncryptionAlgorithm22+

setRecipientEncryptionAlgorithm(algorithm: CmsRecipientEncryptionAlgorithm): void

为内容类型为ENVELOPED_DATA的CMS设置加密算法。

该方法应在创建ENVELOPED_DATA类型的CmsGenerator后立即调用。如果未调用此方法，则默认使用AES_256_GCM作为加密算法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algorithm | CmsRecipientEncryptionAlgorithm | 是 | 用于CMS封装数据的加密算法。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The type of algorithm is invalid or not supported. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

function testSetRecipientEncryptionAlgorithm() {
  try {
    let cmsContentType = cert.CmsContentType.ENVELOPED_DATA;
    let cmsGenerator = cert.createCmsGenerator(cmsContentType);
    console.info(`createCmsGenerator result: success.`);
    let algorithm = cert.CmsRecipientEncryptionAlgorithm.AES_128_CBC;
    cmsGenerator.setRecipientEncryptionAlgorithm(algorithm);
    console.info(`setRecipientEncryptionAlgorithm result: success.`);
  } catch (err) {
    console.error(`testSetRecipientEncryptionAlgorithm failed: errCode: ${err.code}, errMsg: ${err.message}`);
}
```

#### addRecipientInfo22+

addRecipientInfo(recipientInfo: CmsRecipientInfo): Promise<void>

为内容类型为ENVELOPED_DATA的CMS添加接收者信息。使用Promise异步回调。

该方法至少需要设置一个接收者。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipientInfo | CmsRecipientInfo | 是 | 接收者信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The type of recipient certificate is invalid or not supported; 2. The digestAlgorithm of CmsKeyAgreeRecipientInfo is invalid or not supported; 3. The recipientInfo does not have any recipient info. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let eccCertData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICOjCCAd+gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMHkxCzAJBgNVBAYTAmNo\n' +
  'MQ8wDQYDVQQIDAZodWF3ZWkxDTALBgNVBAcMBHhpYW4xDzANBgNVBAoMBmh1YXdl\n' +
  'aTENMAsGA1UECwwEdGVzdDENMAsGA1UEAwwEYW5uZTEbMBkGCSqGSIb3DQEJARYM\n' +
  'dGVzdEAxMjMuY29tMB4XDTI0MTEyNzAzMjQ1MFoXDTM0MTEyNTAzMjQ1MFoweTEL\n' +
  'MAkGA1UEBhMCY2gxDzANBgNVBAgMBmh1YXdlaTENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
  'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR0ZXN0MQ0wCwYDVQQDDARhbm5lMRswGQYJ\n' +
  'KoZIhvcNAQkBFgx0ZXN0QDEyMy5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\n' +
  'AARzg16D6tsNHZa7w0tLHFprXg5kUQgXv/vv3KIM21hY+WDYMz1OST4tmTeQWQF8\n' +
  'kARtjjbHBxtOPufWxMfxf51Wo1MwUTAdBgNVHQ4EFgQUU/P31GCBwyrj3yXkoNaX\n' +
  'xvPp8uIwHwYDVR0jBBgwFoAUU/P31GCBwyrj3yXkoNaXxvPp8uIwDwYDVR0TAQH/\n' +
  'BAUwAwEB/zAKBggqhkjOPQQDAgNJADBGAiEA/wCfbTorAWEEZcgd0CgfXI+EzXu2\n' +
  'Y88BmDD5LFlj3N0CIQDB34h77Li0CSpYpS4+7Mug237zbkFjHR3Q4/VWOT1G1A==\n' +
  '-----END CERTIFICATE-----\n';

let rsaCertData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
  'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
  'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
  'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
  'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
  'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
  'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
  '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
  'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
  'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
  'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
  'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
  'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
  '-----END CERTIFICATE-----\n';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function testAddRecipientInfo() {
  let ecccertEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(eccCertData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let rsacertEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(rsaCertData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  try {
    let eccx509Certcert = await cert.createX509Cert(ecccertEncodingBlob);
    let rsax509Certcert = await cert.createX509Cert(rsacertEncodingBlob);
    let cmsContentType = cert.CmsContentType.ENVELOPED_DATA;
    let cmsGenerator = cert.createCmsGenerator(cmsContentType);
    console.info(`createCmsGenerator result: success.`);

    let eccCert : cert.CmsKeyAgreeRecipientInfo = {
      cert : eccx509Certcert,
      digestAlgorithm : cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256,
    };
    let rsaCert : cert.CmsKeyTransRecipientInfo = {
      cert : rsax509Certcert,
    };
    let recipientInfo: cert.CmsRecipientInfo = {
      keyTransInfo : rsaCert,
      keyAgreeInfo : eccCert,
    };
    await cmsGenerator.addRecipientInfo(recipientInfo);
    console.info(`addRecipientInfo result: success.`);
  } catch (err) {
    console.error(`testAddRecipientInfo failed: errCode: ${err.code}, errMsg: ${err.message}`);
}
```

#### doFinal18+

doFinal(data: Uint8Array, options?: CmsGeneratorOptions): Promise<Uint8Array | string>

用于获取CMS最终数据，例如CMS签名数据或CMS封装数据。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | Cms操作的内容。 |
| options | CmsGeneratorOptions | 否 | Cms操作的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array | string> | 返回Cms最终数据的Promise。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
  'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
  'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
  'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
  'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
  'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
  'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
  '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
  'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
  'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
  'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
  'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
  'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
  '-----END CERTIFICATE-----\n';

let rsaStr1024: string  =
  '-----BEGIN RSA PRIVATE KEY-----\n' +
    'Proc-Type: 4,ENCRYPTED\n' +
    'DEK-Info: DES-EDE3-CBC,DB0AC6E3BEE16420\n\n' +
    '1N5xykdckthZnswMV7blxXm2RCqe/OByBfMwFI7JoXR8STtMiStd4xA3W405k1Ma\n' +
    'ExpsHgWwZaS23x+sQ1sL1dsqIPMrw1Vr+KrL20vQcCVjXPpGKauafVbtcWQ1r2PZ\n' +
    'QJ4KWP6FhUp+sGt2ItODW3dK+1GdqL22ZtANrgFzS42Wh8FSn0UMCf6RG62DK62J\n' +
    'z2jtf4XaorrGSjdTeY+fyyGfSyKidIMMBe+IXwlhCgAe7aHSaqXtMsv+BibB7PJ3\n' +
    'XmEp1D/0ptL3r46txyYcuy8jSNCkW8er93KKnlRN6KbuYZPvPNncWkzZBzV17t5d\n' +
    'QgtvVh32AKgqk5jm8YVnspOFiPrbrK9UN3IW15juFkfnhriM3IrKap4/kW+tfawZ\n' +
    'DmHkSyl8xqFK413Rv0UvYBTjOcGbs2BSJYEvp8CIjtA17SvLmNw70K2nXWuQYutY\n' +
    '+HyucPtHfEqUPQRzWTAMMntTru77u7dxo2WMMMxOtMJO5h7MAnZH9bAFiuO3ewcY\n' +
    'eEePg10d8Owcfh9G6kc0HIGT9MMLMi0mTXhpoQTuWPYuSx6uUZL1fsp1x2fuM0qn\n' +
    'bdf3+UnATYUu4tgvBHrMV7405Y6Y3PnqOFxVMeAHeOTo6UThtJ10mfeCPXGcUaHo\n' +
    'P5enw7h4145cha3+S4hNrUwj3skrtavld7tY74p4DvgZSlCMF3JAm3DhpnEMVcYP\n' +
    'Y6TkSevvxOpBvEHE41Y4VBCBwd9clcixI6cSBJKPUU4A/sc/kkNdGFcbzLQCg/zR\n' +
    '1m7YmBROb2qy4w3lv/uwVnPGLg/YV465irRaN3hgz7/1lm8STKQhmQ==\n' +
    '-----END RSA PRIVATE KEY-----\n';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function testDoFinalByPromise() {
  let certEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
    if (error) {
      console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
    } else {
      try {
        let cmsContentType = cert.CmsContentType.SIGNED_DATA;
        let cmsGenerator = cert.createCmsGenerator(cmsContentType);
        console.info('testDoFinalByPromise createCmsGenerator result: success.');
        let privateKeyInfo: cert.PrivateKeyInfo = {
          key: rsaStr1024,
          password: '123456'
        };
        // addCert设置为true时，第二次addSigner或者addCert增加相同的证书，会报错。
        let config: cert.CmsSignerConfig = {
          mdName:'SHA256',
          addCert:false,
          addAttr:true,
          addSmimeCapAttr:true
        }
        cmsGenerator.addSigner(x509Cert, privateKeyInfo, config);
        console.info('testDoFinalByPromise addSigner result: success.');
        cmsGenerator.addCert(x509Cert);
        console.info('testDoFinalByPromise addCert result: success.');
        let content = new Uint8Array([1,2,3,4]);
        let optionsFinal: cert.CmsGeneratorOptions = {
          contentDataFormat : cert.CmsContentDataFormat.BINARY,
          outFormat : cert.CmsFormat.PEM,
          isDetached : true
        };
        cmsGenerator.doFinal(content, optionsFinal).then(result => {
          console.info('testDoFinalByPromise doFinal result: success, result = %s', result);
        }).catch((error: BusinessError) => {
          console.error(`testDoFinalByPromise failed, errCode: ${error.code}, errMsg: ${error.message}`);
        });
      } catch (err) {
        let e: BusinessError = err as BusinessError;
        console.error(`testDoFinalByPromise failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  });
}
```

#### doFinalSync18+

doFinalSync(data: Uint8Array, options?: CmsGeneratorOptions): Uint8Array | string

用于获取CMS最终数据，例如CMS签名数据或CMS封装数据。（同步方法）。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | Cms操作的内容。 |
| options | CmsGeneratorOptions | 否 | Cms操作的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | string | 返回Cms最终数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
  'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
  'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
  'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
  'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
  'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
  'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
  '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
  'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
  'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
  'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
  'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
  'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
  '-----END CERTIFICATE-----\n';

let rsaStr1024: string  =
  '-----BEGIN RSA PRIVATE KEY-----\n' +
    'Proc-Type: 4,ENCRYPTED\n' +
    'DEK-Info: DES-EDE3-CBC,DB0AC6E3BEE16420\n\n' +
    '1N5xykdckthZnswMV7blxXm2RCqe/OByBfMwFI7JoXR8STtMiStd4xA3W405k1Ma\n' +
    'ExpsHgWwZaS23x+sQ1sL1dsqIPMrw1Vr+KrL20vQcCVjXPpGKauafVbtcWQ1r2PZ\n' +
    'QJ4KWP6FhUp+sGt2ItODW3dK+1GdqL22ZtANrgFzS42Wh8FSn0UMCf6RG62DK62J\n' +
    'z2jtf4XaorrGSjdTeY+fyyGfSyKidIMMBe+IXwlhCgAe7aHSaqXtMsv+BibB7PJ3\n' +
    'XmEp1D/0ptL3r46txyYcuy8jSNCkW8er93KKnlRN6KbuYZPvPNncWkzZBzV17t5d\n' +
    'QgtvVh32AKgqk5jm8YVnspOFiPrbrK9UN3IW15juFkfnhriM3IrKap4/kW+tfawZ\n' +
    'DmHkSyl8xqFK413Rv0UvYBTjOcGbs2BSJYEvp8CIjtA17SvLmNw70K2nXWuQYutY\n' +
    '+HyucPtHfEqUPQRzWTAMMntTru77u7dxo2WMMMxOtMJO5h7MAnZH9bAFiuO3ewcY\n' +
    'eEePg10d8Owcfh9G6kc0HIGT9MMLMi0mTXhpoQTuWPYuSx6uUZL1fsp1x2fuM0qn\n' +
    'bdf3+UnATYUu4tgvBHrMV7405Y6Y3PnqOFxVMeAHeOTo6UThtJ10mfeCPXGcUaHo\n' +
    'P5enw7h4145cha3+S4hNrUwj3skrtavld7tY74p4DvgZSlCMF3JAm3DhpnEMVcYP\n' +
    'Y6TkSevvxOpBvEHE41Y4VBCBwd9clcixI6cSBJKPUU4A/sc/kkNdGFcbzLQCg/zR\n' +
    '1m7YmBROb2qy4w3lv/uwVnPGLg/YV465irRaN3hgz7/1lm8STKQhmQ==\n' +
    '-----END RSA PRIVATE KEY-----\n';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function testDoFinalSync() {
  let certEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
    if (error) {
      console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
    } else {
        try {
          let cmsContentType = cert.CmsContentType.SIGNED_DATA;
          let cmsGenerator = cert.createCmsGenerator(cmsContentType);
          console.info('testDoFinalSync createCmsGenerator result: success.');
          let privateKeyInfo: cert.PrivateKeyInfo = {
            key: rsaStr1024,
            password: '123456'
          };
          // addCert设置为true时，第二次addSigner或者addCert增加相同的证书，会报错。
          let config: cert.CmsSignerConfig = {
            mdName:'SHA256',
            addCert:false,
            addAttr:false,
            addSmimeCapAttr:false
          }
          cmsGenerator.addSigner(x509Cert, privateKeyInfo, config);
          console.info('testDoFinalSync addSigner result: success.');
          cmsGenerator.addCert(x509Cert);
          console.info('testDoFinalSync addCert result: success.');
          let content = new Uint8Array([1,2,3,4]);
          let optionsFinal: cert.CmsGeneratorOptions = {
            contentDataFormat : cert.CmsContentDataFormat.BINARY,
            outFormat : cert.CmsFormat.DER,
            isDetached : false
          };
          let output = cmsGenerator.doFinalSync(content, optionsFinal);
          console.info('testDoFinalSync doFinalSync result: success, output = %s.',output);
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          console.error(`testDoFinalSync failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  });
}
```

#### getEncryptedContentData22+

getEncryptedContentData(): Promise<Uint8Array>

用于获取内容类型为ENVELOPED_DATA的CMS的加密内容数据。使用Promise异步回调。

如果创建了类型为ENVELOPED_DATA的CmsGenerator并使用了数据分离来生成CMS封装数据，使用此方法来获取加密的内容数据。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象, 返回加密的数据内容。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let eccCertData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICOjCCAd+gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMHkxCzAJBgNVBAYTAmNo\n' +
  'MQ8wDQYDVQQIDAZodWF3ZWkxDTALBgNVBAcMBHhpYW4xDzANBgNVBAoMBmh1YXdl\n' +
  'aTENMAsGA1UECwwEdGVzdDENMAsGA1UEAwwEYW5uZTEbMBkGCSqGSIb3DQEJARYM\n' +
  'dGVzdEAxMjMuY29tMB4XDTI0MTEyNzAzMjQ1MFoXDTM0MTEyNTAzMjQ1MFoweTEL\n' +
  'MAkGA1UEBhMCY2gxDzANBgNVBAgMBmh1YXdlaTENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
  'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR0ZXN0MQ0wCwYDVQQDDARhbm5lMRswGQYJ\n' +
  'KoZIhvcNAQkBFgx0ZXN0QDEyMy5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\n' +
  'AARzg16D6tsNHZa7w0tLHFprXg5kUQgXv/vv3KIM21hY+WDYMz1OST4tmTeQWQF8\n' +
  'kARtjjbHBxtOPufWxMfxf51Wo1MwUTAdBgNVHQ4EFgQUU/P31GCBwyrj3yXkoNaX\n' +
  'xvPp8uIwHwYDVR0jBBgwFoAUU/P31GCBwyrj3yXkoNaXxvPp8uIwDwYDVR0TAQH/\n' +
  'BAUwAwEB/zAKBggqhkjOPQQDAgNJADBGAiEA/wCfbTorAWEEZcgd0CgfXI+EzXu2\n' +
  'Y88BmDD5LFlj3N0CIQDB34h77Li0CSpYpS4+7Mug237zbkFjHR3Q4/VWOT1G1A==\n' +
  '-----END CERTIFICATE-----\n';

let rsaCertData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
  'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
  'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
  'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
  'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
  'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
  'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
  '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
  'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
  'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
  'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
  'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
  'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
  '-----END CERTIFICATE-----\n';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function testGetEncryptedContentData() {
  try {
    let ecccertEncodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(eccCertData),
      // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
      encodingFormat: cert.EncodingFormat.FORMAT_PEM
    };

    let rsacertEncodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(rsaCertData),
      // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
      encodingFormat: cert.EncodingFormat.FORMAT_PEM
    };

    let eccx509Certcert = await cert.createX509Cert(ecccertEncodingBlob);
    let rsax509Certcert = await cert.createX509Cert(rsacertEncodingBlob);

    let cmsContentType = cert.CmsContentType.ENVELOPED_DATA;
    let cmsGenerator = cert.createCmsGenerator(cmsContentType);
    console.info(`createCmsGenerator result: success.`);
    let algorithm = cert.CmsRecipientEncryptionAlgorithm.AES_256_GCM;
    cmsGenerator.setRecipientEncryptionAlgorithm(algorithm);
    console.info(`setRecipientEncryptionAlgorithm result: success.`);
    let eccCert : cert.CmsKeyAgreeRecipientInfo = {
      cert : eccx509Certcert,
      digestAlgorithm : cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256,
    };
    let rsaCert : cert.CmsKeyTransRecipientInfo = {
      cert : rsax509Certcert,
    };
    let recipientInfo: cert.CmsRecipientInfo = {
      keyTransInfo : rsaCert,
      keyAgreeInfo : eccCert,
    };
    await cmsGenerator.addRecipientInfo(recipientInfo);
    console.info(`addRecipientInfo result: success.`);
    let content = new Uint8Array([1,2,3,4]);
    let optionsFinal: cert.CmsGeneratorOptions = {
      contentDataFormat : cert.CmsContentDataFormat.BINARY,
      outFormat : cert.CmsFormat.PEM,
      isDetached : true
    };
    let cms = await cmsGenerator.doFinal(content, optionsFinal);
    console.info(`doFinal result: success, cms = %s`, cms);
    let data = await cmsGenerator.getEncryptedContentData();
    console.info(`getEncryptedContentData result: success, data = %s`, data);
  } catch (err) {
    console.error(`testGetEncryptedContentData failed: errCode: ${err.code}, errMsg: ${err.message}`);
}
```

#### cert.createCmsParser22+

createCmsParser(): CmsParser

表示创建CmsParser对象。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CmsParser | CmsParser对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let ECC_256_PUB_ENTRY_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
    'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
    'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
    'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
    'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
    '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
    'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
    'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
    'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
    'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
    '1Cyy/+qufhBUJw5om7E=\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_INTER_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
    'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
    'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
    'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
    'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
    'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
    'ia4tt478nYeQgMChg+xtSw==\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_ROOT_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
    'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
    '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
    'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
    'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
    'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
    'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
    '-----END CERTIFICATE-----';
let ECC_256_PRI_ENTRY_KEY: string =
  '-----BEGIN EC PRIVATE KEY-----\n' +
    'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
    'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
    'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
    '-----END EC PRIVATE KEY-----';

    // string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
      arr.push(str.charCodeAt(i));
  };
  return new Uint8Array(arr);
  }

async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
  let encodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(inStream),
      encodingFormat: cert.EncodingFormat.FORMAT_PEM

  };
  let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);
  return x509Cert;
  }

async function testCmsVerifyTest() {
  try {
    let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
    let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
    let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
    let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
    let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
    let signerConfig: cert.CmsSignerConfig = {
      mdName: 'SHA256',
    };
    let keyInfo: cert.PrivateKeyInfo = {
      key: ECC_256_PRI_ENTRY_KEY
    };
    let option: cert.CmsGeneratorOptions = {
      outFormat: cert.CmsFormat.PEM
    };
    cms.addSigner(x509CertEntry, keyInfo, signerConfig);
    let signData = cms.doFinalSync(plainText, option);
    let config: cert.CmsVerificationConfig = {
      trustCerts: [x509CertRoot, x509CertInter],
    };
    let verify: cert.CmsParser = cert.createCmsParser();
    await verify.setRawData(signData, cert.CmsFormat.PEM);
    await verify.verifySignedData(config);
    console.info('verifySignedData result: success.');
  } catch (error) {
    console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### CmsParser22+

CmsParser对象用于对已签名跟封装的CMS（Cryptographic Message Syntax）格式的消息进行验签和解封装。

PKCS#7是用于存储签名或加密数据的标准语法。注意CMS是PKCS#7的扩展，PKCS#7支持的数据类型包括数据、签名数据、信封数据、

签名和信封数据、摘要数据、加密数据。常用于保护数据的完整性和机密性。

#### setRawData22+

setRawData(data: Uint8Array | string, cmsFormat: CmsFormat): Promise<void>

用于把CMS格式的数据转成CMS对象。使用Promise异步回调。

支持PEM跟DER格式的CMS数据。string对应PEM格式；Uint8Array对应DER格式数据。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | string | 是 | CMS数据内容。 |
| cmsFormat | CmsFormat | 是 | 指定输入的CMS格式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The length of the data is zero or too large; 2. The type of the cmsFormat is invalid or not supported. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let ECC_256_PUB_ENTRY_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
    'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
    'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
    'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
    'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
    '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
    'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
    'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
    'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
    'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
    '1Cyy/+qufhBUJw5om7E=\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_INTER_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
    'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
    'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
    'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
    'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
    'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
    'ia4tt478nYeQgMChg+xtSw==\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_ROOT_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
    'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
    '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
    'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
    'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
    'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
    'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
    '-----END CERTIFICATE-----';
let ECC_256_PRI_ENTRY_KEY: string =
  '-----BEGIN EC PRIVATE KEY-----\n' +
    'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
    'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
    'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
    '-----END EC PRIVATE KEY-----';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
      arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
  }

async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
  let encodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(inStream),
      encodingFormat: cert.EncodingFormat.FORMAT_PEM

  };
  let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

  return x509Cert;
}

async function testCmsVerifyTest() {
  try {
    let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
    let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
    let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
    let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
    let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
    let signerConfig: cert.CmsSignerConfig = {
      mdName: 'SHA256',
    };
    let keyInfo: cert.PrivateKeyInfo = {
      key: ECC_256_PRI_ENTRY_KEY
    };
    let option: cert.CmsGeneratorOptions = {
      outFormat: cert.CmsFormat.PEM
    };
    cms.addSigner(x509CertEntry, keyInfo, signerConfig);
    let signData = cms.doFinalSync(plainText, option);
    let config: cert.CmsVerificationConfig = {
      trustCerts: [x509CertRoot, x509CertInter],
    };
    let verify: cert.CmsParser = cert.createCmsParser();
    await verify.setRawData(signData, cert.CmsFormat.PEM);
    await verify.verifySignedData(config);
    console.info('verifySignedData result: success.');
  } catch (error) {
    console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### getContentType22+

getContentType(): CmsContentType

用于获取CMS的数据类型。当前支持获取签名数据、解封装数据两种类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CmsContentType | 返回CMS数据类型。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let ECC_256_PUB_ENTRY_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
    'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
    'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
    'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
    'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
    '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
    'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
    'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
    'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
    'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
    '1Cyy/+qufhBUJw5om7E=\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_INTER_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
    'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
    'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
    'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
    'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
    'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
    'ia4tt478nYeQgMChg+xtSw==\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_ROOT_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
    'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
    '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
    'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
    'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
    'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
    'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
    '-----END CERTIFICATE-----';
let ECC_256_PRI_ENTRY_KEY: string =
  '-----BEGIN EC PRIVATE KEY-----\n' +
    'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
    'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
    'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
    '-----END EC PRIVATE KEY-----';

    // string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
      arr.push(str.charCodeAt(i));
  };
  return new Uint8Array(arr);
}

async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
  let encodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(inStream),
      encodingFormat: cert.EncodingFormat.FORMAT_PEM

  };
  let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

  return x509Cert;
}

async function testCmsVerifyTest() {
  try {
    let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
    let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
    let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
    let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
    let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
    let signerConfig: cert.CmsSignerConfig = {
      mdName: 'SHA256',
    };
    let keyInfo: cert.PrivateKeyInfo = {
      key: ECC_256_PRI_ENTRY_KEY
    };
    let option: cert.CmsGeneratorOptions = {
      outFormat: cert.CmsFormat.PEM
    };
    cms.addSigner(x509CertEntry, keyInfo, signerConfig);
    let signData = cms.doFinalSync(plainText, option);
    let config: cert.CmsVerificationConfig = {
      trustCerts: [x509CertRoot, x509CertInter],
    };
    let verify: cert.CmsParser = cert.createCmsParser();
    await verify.setRawData(signData, cert.CmsFormat.PEM);
    let contentType: cert.CmsContentType = verify.getContentType();
    console.info('contentType = ' + contentType);
    await verify.verifySignedData(config);
    console.info('verifySignedData result: success.');
  } catch (error) {
    console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### verifySignedData22+

verifySignedData(config: CmsVerificationConfig): Promise<void>

用于验证Signed_DATA内容类型的CMS。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | CmsVerificationConfig | 是 | CMS验签配置内容。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The trustCerts of config is empty; 2. The length of the contentData of config is zero or too large; 3. The contentDataFormat of config is invalid or not supported. |
| 19030001 | crypto operation error. |
| 19030003 | the certificate has not taken effect. |
| 19030004 | the certificate has expired. |
| 19030005 | failed to obtain the certificate issuer. |

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let ECC_256_PUB_ENTRY_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
    'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
    'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
    'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
    'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
    '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
    'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
    'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
    'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
    'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
    '1Cyy/+qufhBUJw5om7E=\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_INTER_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
    'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
    'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
    'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
    'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
    'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
    'ia4tt478nYeQgMChg+xtSw==\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_ROOT_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
    'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
    '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
    'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
    'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
    'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
    'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
    '-----END CERTIFICATE-----';
let ECC_256_PRI_ENTRY_KEY: string =
  '-----BEGIN EC PRIVATE KEY-----\n' +
    'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
    'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
    'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
    '-----END EC PRIVATE KEY-----';

    // string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
      arr.push(str.charCodeAt(i));
  };
  return new Uint8Array(arr);
}

async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
  let encodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(inStream),
      encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

  return x509Cert;
}

async function testCmsVerifyTest() {
  try {
    let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
    let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
    let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
    let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
    let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
    let signerConfig: cert.CmsSignerConfig = {
      mdName: 'SHA256',
    };
    let keyInfo: cert.PrivateKeyInfo = {
      key: ECC_256_PRI_ENTRY_KEY
    };
    let option: cert.CmsGeneratorOptions = {
      outFormat: cert.CmsFormat.PEM
    };
    cms.addSigner(x509CertEntry, keyInfo, signerConfig);
    let signData = cms.doFinalSync(plainText, option);
    let config: cert.CmsVerificationConfig = {
      trustCerts: [x509CertRoot, x509CertInter],
    };
    let verify: cert.CmsParser = cert.createCmsParser();
    await verify.setRawData(signData, cert.CmsFormat.PEM);
    await verify.verifySignedData(config);
    console.info('verifySignedData result: success.');
  } catch (error) {
    console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### getContentData22+

getContentData(): Promise<Uint8Array>

用于从签名类型的CMS数据中获取明文数据。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回CMS原始数据。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let ECC_256_PUB_ENTRY_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
    'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
    'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
    'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
    'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
    '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
    'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
    'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
    'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
    'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
    '1Cyy/+qufhBUJw5om7E=\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_INTER_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
    'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
    'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
    'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
    'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
    'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
    'ia4tt478nYeQgMChg+xtSw==\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_ROOT_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
    'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
    '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
    'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
    'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
    'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
    'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
    '-----END CERTIFICATE-----';
let ECC_256_PRI_ENTRY_KEY: string =
  '-----BEGIN EC PRIVATE KEY-----\n' +
    'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
    'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
    'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
    '-----END EC PRIVATE KEY-----';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
      arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
  let encodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(inStream),
      encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

  return x509Cert;
}

async function testCmsVerifyTest() {
  try {
    let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
    let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
    let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
    let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
    let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
    let signerConfig: cert.CmsSignerConfig = {
      mdName: 'SHA256',
    };
    let keyInfo: cert.PrivateKeyInfo = {
      key: ECC_256_PRI_ENTRY_KEY
    };
    let option: cert.CmsGeneratorOptions = {
      outFormat: cert.CmsFormat.PEM
    };
    cms.addSigner(x509CertEntry, keyInfo, signerConfig);
    let signData = cms.doFinalSync(plainText, option);
    let config: cert.CmsVerificationConfig = {
      trustCerts: [x509CertRoot, x509CertInter],
    };
    let verify: cert.CmsParser = cert.createCmsParser();
    await verify.setRawData(signData, cert.CmsFormat.PEM);
    await verify.verifySignedData(config);
    console.info('verifySignedData result: success.');
    let contentData = await verify.getContentData();
    console.info('getContentData result: success, contentData = ' + contentData);
  } catch (error) {
    console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### getCerts22+

getCerts(type: CmsCertType): Promise<Array<[X509Cert](#ZH-CN_TOPIC_0000002522081410__x509cert)>>

传入枚举值，用于从签名类型的CMS数据中获取证书。当前支持获取签名者证书或全部证书。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | CmsCertType | 是 | 从cms中获取证书的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<X509Cert>> | Promise对象，返回证书集合。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The type of the cmsFormat is invalid or not supported. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let ECC_256_PUB_ENTRY_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
    'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
    'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
    'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
    'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
    '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
    'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
    'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
    'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
    'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
    '1Cyy/+qufhBUJw5om7E=\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_INTER_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
    'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
    'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
    'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
    'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
    'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
    'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
    'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
    'ia4tt478nYeQgMChg+xtSw==\n' +
    '-----END CERTIFICATE-----';

let ECC_256_PUB_ROOT_CERT: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
    'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
    'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
    'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
    'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
    '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
    'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
    'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
    'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
    'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
    '-----END CERTIFICATE-----';
let ECC_256_PRI_ENTRY_KEY: string =
  '-----BEGIN EC PRIVATE KEY-----\n' +
    'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
    'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1eoTUCKHx4UPxsnitVu7dypzInu\n' +
    'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
    '-----END EC PRIVATE KEY-----';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
      arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
  let encodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(inStream),
      encodingFormat: cert.EncodingFormat.FORMAT_PEM

  };
  let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

  return x509Cert;
}

async function testCmsVerifyTest() {
  try {
    let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
    let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
    let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
    let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
    let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
    let signerConfig: cert.CmsSignerConfig = {
      mdName: 'SHA256',
    };
    let keyInfo: cert.PrivateKeyInfo = {
      key: ECC_256_PRI_ENTRY_KEY
    };
    let option: cert.CmsGeneratorOptions = {
      outFormat: cert.CmsFormat.PEM
    };
    cms.addSigner(x509CertEntry, keyInfo, signerConfig);
    let signData = cms.doFinalSync(plainText, option);
    let config: cert.CmsVerificationConfig = {
      trustCerts: [x509CertRoot, x509CertInter],
    };
    let verify: cert.CmsParser = cert.createCmsParser();
    await verify.setRawData(signData, cert.CmsFormat.PEM);
    await verify.verifySignedData(config);
    console.info('verifySignedData result: success.');
    let signerCerts: cert.X509Cert[] = await verify.getCerts(cert.CmsCertType.SIGNER_CERTS);
    console.info('getCerts result: success, signerCerts.length = ' + signerCerts.length);
    await verify.getContentData();
  } catch (error) {
    console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### decryptEnvelopedData22+

decryptEnvelopedData(config: CmsEnvelopedDecryptionConfig): Promise<Uint8Array>

用于验证Enveloped_DATA内容类型的CMS。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | CmsEnvelopedDecryptionConfig | 是 | CMS解封装配置内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回解封装结果。 |

**错误码：**

以下错误码的详细介绍请参见[证书错误码](证书错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19020001 | memory malloc failed. |
| 19020002 | runtime error. Possible causes: 1. Memory copy failed; 2. A null pointer occurs inside the system; 3. Failed to convert parameters between ArkTS and C. |
| 19020003 | parameter check failed. Possible causes: 1. The private key is invalid or not supported; 2. The recipient certificate is invalid or not supported. |
19030001crypto operation error.

**示例：**

```ets
import { cert } from '@kit.DeviceCertificateKit';

let ECC_256_PUBKEY: string =
  '-----BEGIN CERTIFICATE-----\n' +
    'MIICGDCCAb6gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMFcxCzAJBgNVBAYTAkNO\n' +
    'MQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG5rWL\n' +
    '6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwOTE2MDY0MTMwWhcNMzUw\n' +
    'OTE0MDY0MTMwWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8wDQYD\n' +
    'VQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH5rWL\n' +
    '6K+VMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEB06h4SzOryi3d7PW9yN2wACC\n' +
    'VxlduBQjVLWZlDKhFKkdZjve8mUyytSSbBj/rrzR2XmzUzofuNkUbAtje3DDJqN2\n' +
    'MHQwHQYDVR0OBBYEFNtUldgBESf31bwTnYtApIctaSdtMB8GA1UdIwQYMBaAFNtU\n' +
    'ldgBESf31bwTnYtApIctaSdtMAsGA1UdDwQEAwIBBjAJBgNVHREEAjAAMAkGA1Ud\n' +
    'EgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNIADBFAiEAzxzaG2vR\n' +
    'zUnFFL3X3lRQ0IOJrb6cvkSZuaFd4bW2lgUCIHW6QGGnECDFMbDNz7Og9kjkt+3k\n' +
    'FmEJWqEMYudBH3Ul\n' +
    '-----END CERTIFICATE-----';
let ECC_256_PRIVATE: string =
  '-----BEGIN PRIVATE KEY-----\n' +
    'MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgOYwEyIw3ZNIAL4xO\n' +
    'pP6eVcQYcrL2sfnt6vB0z9tKmMmhRANCAAQHTqHhLM6vKLd3s9b3I3bAAIJXGV24\n' +
    'FCNUtZmUMqEUqR1mO97yZTLK1JJsGP+uvNHZebNTOh+42RRsC2N7cMMm\n' +
    '-----END PRIVATE KEY-----';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
      arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
  let encodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(inStream),
      encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

  return x509Cert;
}

async function testCmsDecryptTest() {
  try {
    let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
    let x509CertEc: cert.X509Cert = await createX509Cert(ECC_256_PUBKEY);
    let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.ENVELOPED_DATA);
    let option: cert.CmsGeneratorOptions = {
      outFormat: cert.CmsFormat.PEM
    };
    cms.setRecipientEncryptionAlgorithm(cert.CmsRecipientEncryptionAlgorithm.AES_128_GCM);
    let recipientInfo: cert.CmsRecipientInfo = {
      keyAgreeInfo: {
          cert: x509CertEc,
          digestAlgorithm: cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256
      }
    };
    await cms.addRecipientInfo(recipientInfo);
    console.info('addRecipientInfo result: success, recipientInfo.keyAgreeInfo.digestAlgorithm = ' +
      recipientInfo.keyAgreeInfo?.digestAlgorithm);
    let envelopeData = await cms.doFinal(plainText, option);
    console.info('doFinal result: success, envelopeData = ' + envelopeData);
    let cipherText = await cms.getEncryptedContentData();
    console.info('getEncryptedContentData result: success, cipherText = ' + cipherText);
    let config: cert.CmsEnvelopedDecryptionConfig = {
      keyInfo: {
          key: ECC_256_PRIVATE
      },
    };
    let cmsDecrypt: cert.CmsParser = cert.createCmsParser();
    await cmsDecrypt.setRawData(envelopeData, cert.CmsFormat.PEM);
    let decPlainText: Uint8Array = await cmsDecrypt.decryptEnvelopedData(config);
    console.info('[XTS] Decrypt result: success, decPlainText = ' + decPlainText);
    console.info('decryptEnvelopedData result: success.');
  } catch (error) {
    console.error(`verifySignedData failed: errCode: ${error.code}, errMsg: ${error.message}`);
  }
```