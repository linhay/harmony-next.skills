[]()[]()

# 通行密钥

[]()[]()

#### 概述

提供通行密钥能力。

**系统能力****：**SystemCapability.Security.FIDO2

**起始版本：** 6.0.0(20)

[]()[]()

#### 汇总

[]()[]()

#### 文件

名称

描述

[fido2_api.h](../../capi/headers/fido2_api.h.md)

本声明用于访问FIDO2的API。提供FIDO2（通行密钥）能力的相关接口。FIDO2的基础核心能力，包含：获取支持的FIDO2能力、获取平台认证器能力、注册通行密钥能力和使用通行密钥认证能力。

[]()[]()

#### 结构体

名称

描述

struct [Uint8Buff](../misc/Uint8Buff.md)

定义uint8_t字节流。

struct [AuthenticationExtensionsClientOutputs](../security/AuthenticationExtensionsClientOutputs.md)

身份认证扩展。

struct [FIDO2_AuthenticatorResponse](../security/FIDO2_AuthenticatorResponse.md)

定义获取认证器断言响应的结构体。

struct [FIDO2_PublicKeyAssertionCredential](../security/FIDO2_PublicKeyAssertionCredential.md)

定义获取认证结果结构体。

struct [FIDO2_AuthenticatorTransportArray](../security/FIDO2_AuthenticatorTransportArray.md)

认证器传输方式数组。

struct [FIDO2_AuthenticatorAttestationResponse](../security/FIDO2_AuthenticatorAttestationResponse.md)

认证器声明响应。

struct [FIDO2_PublicKeyAttestationCredential](../security/FIDO2_PublicKeyAttestationCredential.md)

定义获取注册结果结构体。

struct [FIDO2_AuthenticatorSelectionCriteria](../security/FIDO2_AuthenticatorSelectionCriteria.md)

由webAuthn依赖方（即接入协议的应用或网页）指定，与认证器有关。

struct [FIDO2_PublicKeyCredentialDescriptor](../security/FIDO2_PublicKeyCredentialDescriptor.md)

用于注册或认证凭据的参数。

struct [FIDO2_PublicKeyCredentialParameters](../security/FIDO2_PublicKeyCredentialParameters.md)

认证凭据的附加参数。

struct [FIDO2_PublicKeyCredentialUserEntity](../security/FIDO2_PublicKeyCredentialUserEntity.md)

创建新凭据时用户的属性。

struct [FIDO2_PublicKeyCredentialRpEntity](../security/FIDO2_PublicKeyCredentialRpEntity.md)

创建新凭据时依赖方的属性。

struct [FIDO2_PublicKeyCredentialDescriptorArray](../security/FIDO2_PublicKeyCredentialDescriptorArray.md)

PublicKey凭证描述符数组。

struct [FIDO2_PublicKeyCredentialHintArray](../security/FIDO2_PublicKeyCredentialHintArray.md)

认证方式指示数组。

struct [FIDO2_PublicKeyCredentialRequestOptions](../security/FIDO2_PublicKeyCredentialRequestOptions.md)

定义通行密钥认证请求参数。

struct [FIDO2_CredentialCreationOptionArray](../security/FIDO2_CredentialCreationOptionArray.md)

认证凭据的附加参数数组。

struct [FIDO2_AttestationFormatsArray](../media/FIDO2_AttestationFormatsArray.md)

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。

struct [FIDO2_PublicKeyCredentialCreationOptions](../security/FIDO2_PublicKeyCredentialCreationOptions.md)

创建新的认证凭据的选项。

struct [FIDO2_CredentialCreationOptions](../security/FIDO2_CredentialCreationOptions.md)

凭据请求的选项。

struct [FIDO2_AuthenticatorMetadata](../security/FIDO2_AuthenticatorMetadata.md)

认证器元数据。

struct [FIDO2_CredentialRequestOptions](../security/FIDO2_CredentialRequestOptions.md)

认证信息字典对象。

struct [FIDO2_AuthenticatorMetadataArray](../security/FIDO2_AuthenticatorMetadataArray.md)

描述支持的认证器数组。

struct [FIDO2_Capability](../system-services/FIDO2_Capability.md)

通行密钥能力的结构体。

struct [FIDO2_CapabilityArray](../system-services/FIDO2_CapabilityArray.md)

描述能力数组。

struct [FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md)

Token binding协议，用于客户端与依赖方通信。

[]()[]()

#### 类型定义

名称

描述

typedef struct [Uint8Buff](../misc/Uint8Buff.md)[Uint8Buff](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga8cab8c65834776e285ccd286c92a642b)

定义uint8_t字节流。

typedef enum [FIDO2_TokenBindingStatus](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga3a0c5c93081cd75c8ecd7a1efac8252e)[FIDO2_TokenBindingStatus](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga1ae0f0eb0c0c608a7fcc72f7cf406c16)

TokenBinding协议的状态。

typedef enum [FIDO2_AttestationConveyancePreference](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga1e33947b822678781f03c849ade9f45f)[FIDO2_AttestationConveyancePreference](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga49ab300e6aeca4a1c98c345431155ca4)

供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。

typedef enum [FIDO2_UserVerificationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga632b7b26c16a519650398ccfc3515f7a)[FIDO2_UserVerificationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga0c7660a5c83a231ad0c1f7c6d874bd06)

依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。

typedef enum [FIDO2_AuthenticatorAttachment](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa6aa2fca2e7690e98f6d1d273324e471)[FIDO2_AuthenticatorAttachment](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga4dc2ec8c4f6c553dd2852726c9a79c3b)

认证器信息（平台、漫游）。

typedef enum [FIDO2_AuthenticatorTransport](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga02592e5b749c266e7297333afce03cec)[FIDO2_AuthenticatorTransport](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gad4101bf2c242b7ff9263b0f8ad146856)

认证器传输方式的枚举。

typedef enum [FIDO2_Algorithm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga27cd96fc7f972c4cd8cfe4d92737920a)[FIDO2_Algorithm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga273bffd9251572eac19da58a910b9bb6)

加密算法的枚举。

typedef enum [FIDO2_PublicKeyCredentialHint](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gab7b1367ea48debe767ae103f8ac9e96c)[FIDO2_PublicKeyCredentialHint](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga4a6398c601fd44bf26ff2b2953cb2532)

认证方式指示的枚举。

typedef enum [FIDO2_PublicKeyCredentialType](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa46edbba8f1162737d26681080eea727)[FIDO2_PublicKeyCredentialType](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga72f2e8f694b926204f917ae7c5d54715)

公钥凭据类型的枚举。

typedef enum [FIDO2_Uvm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga60fda18b064802349b186de072b43e98)[FIDO2_Uvm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga432d421e134e783bfab234fee9c9a81a)

UVM的枚举。

typedef enum [FIDO2_ClientCapability](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gae8cdc5641132b84e0313c7412d13bbbe)[FIDO2_ClientCapability](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gae997777dcf71d750e456a9eecafbd3ea)

客户端能力的枚举。

typedef enum [FIDO2_CredentialMediationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga16035d1941d25a1ea71203ad72809b93)[FIDO2_CredentialMediationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gafdaefa0e120bb74bf4ebafef76437242)

用户介入要求的枚举。

typedef enum [FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693)[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga313648b7100419fc2cd6c1a73b0ad7ec)

错误码定义。

typedef struct [AuthenticationExtensionsClientOutputs](../security/AuthenticationExtensionsClientOutputs.md)[AuthenticationExtensionsClientOutputs](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga880558921a13840936325beb26efe45b)

身份认证扩展。

typedef struct [FIDO2_AuthenticatorResponse](../security/FIDO2_AuthenticatorResponse.md)[FIDO2_AuthenticatorResponse](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaca490762d995a753f559380626aa60ee)

定义获取认证器断言响应的结构体。

typedef struct [FIDO2_PublicKeyAssertionCredential](../security/FIDO2_PublicKeyAssertionCredential.md)[FIDO2_PublicKeyAssertionCredential](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaf60e65485855aee47dbad266920de8a7)

定义获取认证结果结构体。

typedef struct [FIDO2_AuthenticatorTransportArray](../security/FIDO2_AuthenticatorTransportArray.md)[FIDO2_AuthenticatorTransportArray](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga5d080d620d78fd43051d4af61fef77a9)

认证器传输方式数组。

typedef struct [FIDO2_AuthenticatorAttestationResponse](../security/FIDO2_AuthenticatorAttestationResponse.md)[FIDO2_AuthenticatorAttestationResponse](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga006189911a767560f30a97e22b9be84e)

认证器声明响应。

typedef struct [FIDO2_PublicKeyAttestationCredential](../security/FIDO2_PublicKeyAttestationCredential.md)[FIDO2_PublicKeyAttestationCredential](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaeb82b4593aeff244d31cd40be08eb368)

定义获取注册结果结构体。

typedef struct [FIDO2_AuthenticatorSelectionCriteria](../security/FIDO2_AuthenticatorSelectionCriteria.md)[FIDO2_AuthenticatorSelectionCriteria](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga0816ff84d850cc5bc64fd60b0198765e)

由webAuthn依赖方指定，与认证器有关。

typedef struct [FIDO2_PublicKeyCredentialDescriptor](../security/FIDO2_PublicKeyCredentialDescriptor.md)[FIDO2_PublicKeyCredentialDescriptor](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa99238931c603213556f2d4742a7af04)

用于注册或认证凭据的参数。

typedef struct [FIDO2_PublicKeyCredentialParameters](../security/FIDO2_PublicKeyCredentialParameters.md)[FIDO2_PublicKeyCredentialParameters](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gac43d4448abcb19a8ef63ebfb83b1ad6a)

认证凭据的附加参数。

typedef struct [FIDO2_PublicKeyCredentialUserEntity](../security/FIDO2_PublicKeyCredentialUserEntity.md)[FIDO2_PublicKeyCredentialUserEntity](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gafdbfb4f0e894bfe4b9bffa2e04a6d3eb)

创建新凭据时用户的属性。

typedef struct [FIDO2_PublicKeyCredentialRpEntity](../security/FIDO2_PublicKeyCredentialRpEntity.md)[FIDO2_PublicKeyCredentialRpEntity](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga810af4d05788d90543b3b10a5ffadf9e)

创建新凭据时依赖方的属性。

typedef struct [FIDO2_PublicKeyCredentialDescriptorArray](../security/FIDO2_PublicKeyCredentialDescriptorArray.md)[FIDO2_PublicKeyCredentialDescriptorArray](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaaa0a2bd23e9d18811cd1cf0ea04bc9a6)

PublicKey凭证描述符数组。

typedef struct [FIDO2_PublicKeyCredentialHintArray](../security/FIDO2_PublicKeyCredentialHintArray.md)[FIDO2_PublicKeyCredentialHintArray](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga49183130db95a71da3c945452e702676)

认证方式指示数组。

typedef struct [FIDO2_PublicKeyCredentialRequestOptions](../security/FIDO2_PublicKeyCredentialRequestOptions.md)[FIDO2_PublicKeyCredentialRequestOptions](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga509d2dcd89ac955c0f03bb5e4238abb5)

定义通行密钥认证请求参数。

typedef struct [FIDO2_CredentialCreationOptionArray](../security/FIDO2_CredentialCreationOptionArray.md)[FIDO2_CredentialCreationOptionArray](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga2c517a89040b570e15517f7719ed4cad)

认证凭据的附加参数数组。

typedef struct [FIDO2_AttestationFormatsArray](../media/FIDO2_AttestationFormatsArray.md)[FIDO2_AttestationFormatsArray](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gae6d363b5e0bb786bbb1b28d4863c84c2)

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。

typedef struct [FIDO2_PublicKeyCredentialCreationOptions](../security/FIDO2_PublicKeyCredentialCreationOptions.md)[FIDO2_PublicKeyCredentialCreationOptions](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga41d2d104407689b7cfc1ed38c1ed2726)

创建新的认证凭据的选项。

typedef struct [FIDO2_CredentialCreationOptions](../security/FIDO2_CredentialCreationOptions.md)[FIDO2_CredentialCreationOptions](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga6cd8020c0afbf089d298aaf751345bff)

凭据请求的选项。

typedef struct [FIDO2_AuthenticatorMetadata](../security/FIDO2_AuthenticatorMetadata.md)[FIDO2_AuthenticatorMetadata](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gafdb5807d009529053a96c737b2ee7c55)

认证器元数据。

typedef struct [FIDO2_CredentialRequestOptions](../security/FIDO2_CredentialRequestOptions.md)[FIDO2_CredentialRequestOptions](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga4db55935548b74ad18c5fb6f15f80a7b)

认证信息字典对象。

typedef struct [FIDO2_AuthenticatorMetadataArray](../security/FIDO2_AuthenticatorMetadataArray.md)[FIDO2_AuthenticatorMetadataArray](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga1e40d19100575390959d7d7dfe13a52a)

描述支持的认证器数组。

typedef struct [FIDO2_Capability](../system-services/FIDO2_Capability.md)[FIDO2_Capability](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga483e50693a9bf926f524ba9ed1178f0b)

通行密钥能力的结构体。

typedef struct [FIDO2_CapabilityArray](../system-services/FIDO2_CapabilityArray.md)[FIDO2_CapabilityArray](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga674019e8f264253ca8f3390ce93ad46f)

描述能力数组。

typedef struct [FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md)[FIDO2_TokenBinding](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga80db96062ec07eff0f2807e516b5a5f1)

Token binding（协议），用于客户端与依赖方通信。

[]()[]()

#### 枚举

名称

描述

[FIDO2_TokenBindingStatus](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga3a0c5c93081cd75c8ecd7a1efac8252e) { FIDO2_PRESENT = 0, FIDO2_SUPPORTED = 1 }

TokenBinding协议的状态。

[FIDO2_AttestationConveyancePreference](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga1e33947b822678781f03c849ade9f45f) { FIDO2_NONE = 0, FIDO2_INDIRECT = 1, FIDO2_DIRECT = 2, FIDO2_ENTERPRISE = 3 }

供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。

[FIDO2_UserVerificationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga632b7b26c16a519650398ccfc3515f7a) { FIDO2_REQUIRED = 0, FIDO2_PREFERRED = 1, FIDO2_DISCOURAGED = 2 }

依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。

[FIDO2_AuthenticatorAttachment](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa6aa2fca2e7690e98f6d1d273324e471) { FIDO2_PLATFORM = 0, FIDO2_CROSS_PLATFORM = 1 }

认证器信息（平台、漫游）。

[FIDO2_AuthenticatorTransport](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga02592e5b749c266e7297333afce03cec) {

FIDO2_USB = 0, FIDO2_NFC = 1, FIDO2_BLE = 2, FIDO2_SMART_CARD = 3,

FIDO2_HYBRID = 4, FIDO2_INTERNAL = 5

}

认证器传输方式的枚举。

[FIDO2_Algorithm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga27cd96fc7f972c4cd8cfe4d92737920a) {

FIDO2_ES256 = -7, FIDO2_ES384 = -35, FIDO2_ES512 = -36, FIDO2_RS256 = -257,

FIDO2_RS384 = -258, FIDO2_RS512 = -259, FIDO2_PS256 = -37, FIDO2_PS384 = -38,

FIDO2_PS512 = -39

}

算法的枚举。

[FIDO2_PublicKeyCredentialHint](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gab7b1367ea48debe767ae103f8ac9e96c) { FIDO2_SECURITY_KEY = 0, FIDO2_CLIENT_DEVICE = 1, FIDO2_HINT_HYBRID = 2 }

认证方式指示的枚举。

[FIDO2_PublicKeyCredentialType](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa46edbba8f1162737d26681080eea727) { FIDO2_PUBLIC_KEY = 0 }

公钥凭据类型的枚举。

[FIDO2_Uvm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga60fda18b064802349b186de072b43e98) { FIDO2_UVM_FINGERPRINT = 2, FIDO2_UVM_PIN = 4, FIDO2_UVM_FACEPRINT = 16 }

UVM的枚举。

[FIDO2_ClientCapability](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gae8cdc5641132b84e0313c7412d13bbbe) {

FIDO2_CONDITIONAL_CREATE = 0, FIDO2_CONDITIONAL_GET = 1, FIDO2_HYBRID_TRANSPORT = 2, FIDO2_PASSKEY_PLATFORM_AUTHENTICATOR = 3,

FIDO2_USER_VERIFYING_PLATFORM_AUTHENTICATOR = 4, FIDO2_RELATED_ORIGINS = 5, FIDO2_SIGNAL_ALL_ACCEPTED_CREDENTIALS = 6, FIDO2_SIGNAL_CURRENT_USER_DETAILS = 7,

FIDO2_SIGNAL_UNKNOWN_CREDENTIAL = 8, FIDO2_EXTENSION_UVI = 9

}

客户端能力的枚举。

[FIDO2_CredentialMediationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga16035d1941d25a1ea71203ad72809b93) { FIDO2_SILENT = 0, FIDO2_OPTIONAL = 1, FIDO2_CONDITIONAL = 2, FIDO2_MEDIATION_REQUIRED = 3 }

用户介入要求的枚举。

[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693) {

FIDO2_SUCCESS = 0, FIDO2_PERMISSION_DENIED = 201, FIDO2_DEVICE_NOT_SUPPORT = 801, FIDO2_NOT_SUPPORT = 1021300001, FIDO2_INVALID_STATE = 1021300002,

FIDO2_INTEGRITY_CHECK_FAILED = 1021300003, FIDO2_USER_ABORT = 1021300004, FIDO2_TIMEOUT = 1021300005, FIDO2_ENCODING_ERROR = 1021300006,

FIDO2_UNKNOWN_ERROR = 1021300007, FIDO2_CONSTRAINT_ERROR = 1021300008, FIDO2_DATA_ERROR = 1021300009, FIDO2_USER_REJECTS = 1021300010,

FIDO2_CONNECT_SERVICE_FAILED = 1021300011, FIDO2_MAX_CRED_NUM_REACHED = 1021300012, FIDO2_INVALID_CTAP_COMMAND = 1021310001, FIDO2_INVALID_PARAMETERS = 1021310002, FIDO2_INVALID_MESSAGE_OR_ATTRIBUTE_LENGTH = 1021310003,

FIDO2_INVALID_CBOR_OR_UNPREDICTABLE = 1021310004, FIDO2_PARSE_CBOR_FAILED = 1021310005, FIDO2_INVALID_CREDENTIALS = 1021310006, FIDO2_NOT_ALLOWED = 1021310007,

FIDO2_USER_VERIFICATION_FAILED = 1021310008, FIDO2_OTHER_ERROR = 1021310009

}

错误码定义。

[]()[]()

#### 函数

名称

描述

void [HMS_FIDO2_initCreationOptions](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga1d655e31c512e2cb8dfc3c1e616d03aa) ([FIDO2_CredentialCreationOptions](../security/FIDO2_CredentialCreationOptions.md) *options)

初始化FIDO2_CredentialCreationOptions结构。

void [HMS_FIDO2_initTokenBinding](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga46853c19611bf506dca76820b2446c19) ([FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md) *tokenBinding)

初始化FIDO2_TokenBinding结构体。

void [HMS_FIDO2_initRequestOptions](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga5ae4e44e8d06e0c247308d7329970c3a) ([FIDO2_CredentialRequestOptions](../security/FIDO2_CredentialRequestOptions.md) *options)

初始化FIDO2_CredentialRequestOptions结构。

[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693)[HMS_FIDO2_getClientCapability](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga3745265749b2776403960fbeece3de77) ([FIDO2_CapabilityArray](../system-services/FIDO2_CapabilityArray.md) **capability)

查询当前设备/版本支持的客户端能力列表。当给定功能的值为true时，表示通行密钥客户端当前支持该能力。

[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693)[HMS_FIDO2_getPlatformAuthenticator](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga18b569cb28a659f4282acbb64e198195) ([FIDO2_AuthenticatorMetadataArray](../security/FIDO2_AuthenticatorMetadataArray.md) **authenticators)

获取支持的平台身份认证器列表。

[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693)[HMS_FIDO2_register](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaaaed812197e7dc4d5f9a3354d5349665) (const [FIDO2_CredentialCreationOptions](../security/FIDO2_CredentialCreationOptions.md) options, const [FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md) tokenBinding, const char *origin, [FIDO2_PublicKeyAttestationCredential](../security/FIDO2_PublicKeyAttestationCredential.md) **publicKeyAttestationCredential)

通行密钥注册。

[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693)[HMS_FIDO2_authenticate](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaac4365229064efc78dc25dceb7c932a3) (const [FIDO2_CredentialRequestOptions](../security/FIDO2_CredentialRequestOptions.md) options, const [FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md) tokenBinding, const char *origin, [FIDO2_PublicKeyAssertionCredential](../security/FIDO2_PublicKeyAssertionCredential.md) **publicKeyAssertionCredential)

基于fido2的认证。

void [HMS_FIDO2_CapabilityArray_Destroy](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga4287e078ad1dbe55804ea73133173949) ([FIDO2_CapabilityArray](../system-services/FIDO2_CapabilityArray.md) *capability)

释放能力的数组。

void [HMS_FIDO2_AuthenticatorMetadataArray_Destroy](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa5f5050def714db82bfed358922c897c) ([FIDO2_AuthenticatorMetadataArray](../security/FIDO2_AuthenticatorMetadataArray.md) *authenticators)

释放认证者元数据数组。

void [HMS_FIDO2_PublicKeyAttestationCredential_Destroy](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga10cff1c35e596a604fbd4289abc5696b) ([FIDO2_PublicKeyAttestationCredential](../security/FIDO2_PublicKeyAttestationCredential.md) *publicKeyAttestationCredential)

释放PublicKeyAttestationCredential的结构体。

void [HMS_FIDO2_PublicKeyAssertionCredential_Destroy](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaba286b4df1149f3632d5a44c15a5ee1e) ([FIDO2_PublicKeyAssertionCredential](../security/FIDO2_PublicKeyAssertionCredential.md) *publicKeyAssertionCredential)

释放PublicKeyAssertionCredential的结构体。

[]()[]()

#### 类型定义说明

[]()[]()

#### AuthenticationExtensionsClientOutputs

```ets
typedef struct [AuthenticationExtensionsClientOutputs](../security/AuthenticationExtensionsClientOutputs.md) [AuthenticationExtensionsClientOutputs](../security/AuthenticationExtensionsClientOutputs.md)
```

**描述**

身份认证扩展。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_Algorithm

```ets
typedef enum [FIDO2_Algorithm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga27cd96fc7f972c4cd8cfe4d92737920a) [FIDO2_Algorithm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga27cd96fc7f972c4cd8cfe4d92737920a)
```

**描述**

算法的枚举。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AttestationConveyancePreference

```ets
typedef enum [FIDO2_AttestationConveyancePreference](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga1e33947b822678781f03c849ade9f45f) [FIDO2_AttestationConveyancePreference](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga1e33947b822678781f03c849ade9f45f)
```

**描述**

供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AttestationFormatsArray

```ets
typedef struct [FIDO2_AttestationFormatsArray](../media/FIDO2_AttestationFormatsArray.md) [FIDO2_AttestationFormatsArray](../media/FIDO2_AttestationFormatsArray.md)
```

**描述**

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AuthenticatorAttachment

```ets
typedef enum [FIDO2_AuthenticatorAttachment](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa6aa2fca2e7690e98f6d1d273324e471) [FIDO2_AuthenticatorAttachment](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa6aa2fca2e7690e98f6d1d273324e471)
```

**描述**

认证器信息（平台、漫游）。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AuthenticatorAttestationResponse

```ets
typedef struct [FIDO2_AuthenticatorAttestationResponse](../security/FIDO2_AuthenticatorAttestationResponse.md) [FIDO2_AuthenticatorAttestationResponse](../security/FIDO2_AuthenticatorAttestationResponse.md)
```

**描述**

认证器声明响应。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AuthenticatorMetadata

```ets
typedef struct [FIDO2_AuthenticatorMetadata](../security/FIDO2_AuthenticatorMetadata.md) [FIDO2_AuthenticatorMetadata](../security/FIDO2_AuthenticatorMetadata.md)
```

**描述**

认证器元数据。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AuthenticatorMetadataArray

```ets
typedef struct [FIDO2_AuthenticatorMetadataArray](../security/FIDO2_AuthenticatorMetadataArray.md) [FIDO2_AuthenticatorMetadataArray](../security/FIDO2_AuthenticatorMetadataArray.md)
```

**描述**

描述支持的认证器数组。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AuthenticatorResponse

```ets
typedef struct [FIDO2_AuthenticatorResponse](../security/FIDO2_AuthenticatorResponse.md) [FIDO2_AuthenticatorResponse](../security/FIDO2_AuthenticatorResponse.md)
```

**描述**

定义获取认证器断言响应的结构体。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AuthenticatorSelectionCriteria

```ets
typedef struct [FIDO2_AuthenticatorSelectionCriteria](../security/FIDO2_AuthenticatorSelectionCriteria.md) [FIDO2_AuthenticatorSelectionCriteria](../security/FIDO2_AuthenticatorSelectionCriteria.md)
```

**描述**

由webAuthn依赖方指定，与认证器有关。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AuthenticatorTransport

```ets
typedef enum [FIDO2_AuthenticatorTransport](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga02592e5b749c266e7297333afce03cec) [FIDO2_AuthenticatorTransport](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga02592e5b749c266e7297333afce03cec)
```

**描述**

认证器传输方式的枚举。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_AuthenticatorTransportArray

```ets
typedef struct [FIDO2_AuthenticatorTransportArray](../security/FIDO2_AuthenticatorTransportArray.md) [FIDO2_AuthenticatorTransportArray](../security/FIDO2_AuthenticatorTransportArray.md)
```

**描述**

认证器传输方式数组。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_Capability

```ets
typedef struct [FIDO2_Capability](../system-services/FIDO2_Capability.md) [FIDO2_Capability](../system-services/FIDO2_Capability.md)
```

**描述**

通行密钥能力的结构体。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_CapabilityArray

```ets
typedef struct [FIDO2_CapabilityArray](../system-services/FIDO2_CapabilityArray.md) [FIDO2_CapabilityArray](../system-services/FIDO2_CapabilityArray.md)
```

**描述**

描述能力数组。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_ClientCapability

```ets
typedef enum [FIDO2_ClientCapability](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gae8cdc5641132b84e0313c7412d13bbbe) [FIDO2_ClientCapability](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gae8cdc5641132b84e0313c7412d13bbbe)
```

**描述**

客户端能力的枚举。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_CredentialCreationOptionArray

```ets
typedef struct [FIDO2_CredentialCreationOptionArray](../security/FIDO2_CredentialCreationOptionArray.md) [FIDO2_CredentialCreationOptionArray](../security/FIDO2_CredentialCreationOptionArray.md)
```

**描述**

认证凭据的附加参数数组。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_CredentialCreationOptions

```ets
typedef struct [FIDO2_CredentialCreationOptions](../security/FIDO2_CredentialCreationOptions.md) [FIDO2_CredentialCreationOptions](../security/FIDO2_CredentialCreationOptions.md)
```

**描述**

凭据请求的选项。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_CredentialMediationRequirement

```ets
typedef enum [FIDO2_CredentialMediationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga16035d1941d25a1ea71203ad72809b93) [FIDO2_CredentialMediationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga16035d1941d25a1ea71203ad72809b93)
```

**描述**

用户介入要求的枚举。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_CredentialRequestOptions

```ets
typedef struct [FIDO2_CredentialRequestOptions](../security/FIDO2_CredentialRequestOptions.md) [FIDO2_CredentialRequestOptions](../security/FIDO2_CredentialRequestOptions.md)
```

**描述**

认证信息字典对象。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_ErrorCode

```ets
typedef enum [FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693) [FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693)
```

**描述**

错误码定义。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyAssertionCredential

```ets
typedef struct [FIDO2_PublicKeyAssertionCredential](../security/FIDO2_PublicKeyAssertionCredential.md) [FIDO2_PublicKeyAssertionCredential](../security/FIDO2_PublicKeyAssertionCredential.md)
```

**描述**

定义获取认证结果结构体。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyAttestationCredential

```ets
typedef struct [FIDO2_PublicKeyAttestationCredential](../security/FIDO2_PublicKeyAttestationCredential.md) [FIDO2_PublicKeyAttestationCredential](../security/FIDO2_PublicKeyAttestationCredential.md)
```

**描述**

定义获取注册结果结构体。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialCreationOptions

```ets
typedef struct [FIDO2_PublicKeyCredentialCreationOptions](../security/FIDO2_PublicKeyCredentialCreationOptions.md) [FIDO2_PublicKeyCredentialCreationOptions](../security/FIDO2_PublicKeyCredentialCreationOptions.md)
```

**描述**

创建新的认证凭据的选项。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialDescriptor

```ets
typedef struct [FIDO2_PublicKeyCredentialDescriptor](../security/FIDO2_PublicKeyCredentialDescriptor.md) [FIDO2_PublicKeyCredentialDescriptor](../security/FIDO2_PublicKeyCredentialDescriptor.md)
```

**描述**

用于注册或认证凭据的参数。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialDescriptorArray

```ets
typedef struct [FIDO2_PublicKeyCredentialDescriptorArray](../security/FIDO2_PublicKeyCredentialDescriptorArray.md) [FIDO2_PublicKeyCredentialDescriptorArray](../security/FIDO2_PublicKeyCredentialDescriptorArray.md)
```

**描述**

PublicKey凭证描述符数组。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialHint

```ets
typedef enum [FIDO2_PublicKeyCredentialHint](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gab7b1367ea48debe767ae103f8ac9e96c) [FIDO2_PublicKeyCredentialHint](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gab7b1367ea48debe767ae103f8ac9e96c)
```

**描述**

认证方式指示的枚举。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialHintArray

```ets
typedef struct [FIDO2_PublicKeyCredentialHintArray](../security/FIDO2_PublicKeyCredentialHintArray.md) [FIDO2_PublicKeyCredentialHintArray](../security/FIDO2_PublicKeyCredentialHintArray.md)
```

**描述**

认证方式指示数组。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialParameters

```ets
typedef struct [FIDO2_PublicKeyCredentialParameters](../security/FIDO2_PublicKeyCredentialParameters.md) [FIDO2_PublicKeyCredentialParameters](../security/FIDO2_PublicKeyCredentialParameters.md)
```

**描述**

认证凭据的附加参数。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialRequestOptions

```ets
typedef struct [FIDO2_PublicKeyCredentialRequestOptions](../security/FIDO2_PublicKeyCredentialRequestOptions.md) [FIDO2_PublicKeyCredentialRequestOptions](../security/FIDO2_PublicKeyCredentialRequestOptions.md)
```

**描述**

定义通行密钥认证请求参数。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialRpEntity

```ets
typedef struct [FIDO2_PublicKeyCredentialRpEntity](../security/FIDO2_PublicKeyCredentialRpEntity.md) [FIDO2_PublicKeyCredentialRpEntity](../security/FIDO2_PublicKeyCredentialRpEntity.md)
```

**描述**

创建新凭据时依赖方的属性。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialType

```ets
typedef enum [FIDO2_PublicKeyCredentialType](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa46edbba8f1162737d26681080eea727) [FIDO2_PublicKeyCredentialType](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa46edbba8f1162737d26681080eea727)
```

**描述**

公钥凭据类型的枚举。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_PublicKeyCredentialUserEntity

```ets
typedef struct [FIDO2_PublicKeyCredentialUserEntity](../security/FIDO2_PublicKeyCredentialUserEntity.md) [FIDO2_PublicKeyCredentialUserEntity](../security/FIDO2_PublicKeyCredentialUserEntity.md)
```

**描述**

创建新凭据时用户的属性。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_TokenBinding

```ets
typedef struct [FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md) [FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md)
```

**描述**

Token binding协议，用于客户端与依赖方通信。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_TokenBindingStatus

```ets
typedef enum [FIDO2_TokenBindingStatus](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga3a0c5c93081cd75c8ecd7a1efac8252e) [FIDO2_TokenBindingStatus](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga3a0c5c93081cd75c8ecd7a1efac8252e)
```

**描述**

TokenBinding协议的状态。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_UserVerificationRequirement

```ets
typedef enum [FIDO2_UserVerificationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga632b7b26c16a519650398ccfc3515f7a) [FIDO2_UserVerificationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga632b7b26c16a519650398ccfc3515f7a)
```

**描述**

依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。

**起始版本：** 6.0.0(20)

[]()[]()

#### FIDO2_Uvm

```ets
typedef enum [FIDO2_Uvm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga60fda18b064802349b186de072b43e98) [FIDO2_Uvm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga60fda18b064802349b186de072b43e98)
```

**描述**

UVM的枚举。

**起始版本：** 6.0.0(20)

[]()[]()

#### Uint8Buff

```ets
typedef struct [Uint8Buff](../misc/Uint8Buff.md) [Uint8Buff](../misc/Uint8Buff.md)
```

**描述**

定义uint8_t字节流。

**起始版本：** 6.0.0(20)

[]()[]()

#### 枚举类型说明

[]()[]()

#### FIDO2_Algorithm

```ets
enum [FIDO2_Algorithm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga27cd96fc7f972c4cd8cfe4d92737920a)
```

**描述**

加密算法的枚举。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_ES256

ES256算法。

****FIDO2_ES384

ES384算法。

****FIDO2_ES512

ES512算法。

****FIDO2_RS256

RS256算法。

****FIDO2_RS384

RS384算法。

****FIDO2_RS512

RS512算法。

****FIDO2_PS256

PS256算法。

****FIDO2_PS384

PS384算法。

****FIDO2_PS512

PS512算法。

[]()[]()

#### FIDO2_AttestationConveyancePreference

```ets
enum [FIDO2_AttestationConveyancePreference](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga1e33947b822678781f03c849ade9f45f)
```

**描述**

供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_NONE

依赖方对认证者证明不感兴趣，默认值为none。

****FIDO2_INDIRECT

间接依赖方倾向于提供可认证的证明声明文档，但允许用户决定如何获得这种证明声明。

****FIDO2_DIRECT

直接依赖方希望接收认证者生成的证明声明。

****FIDO2_ENTERPRISE

依赖方希望接收企业证明。企业证明是一个证明声明， 其中可能包括唯一标识认证者的信息。

[]()[]()

#### FIDO2_AuthenticatorAttachment

```ets
enum [FIDO2_AuthenticatorAttachment](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa6aa2fca2e7690e98f6d1d273324e471)
```

**描述**

认证器信息（平台、漫游）。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_PLATFORM

平台认证器，例如PIN码、指纹、人脸等。

****FIDO2_CROSS_PLATFORM

跨平台认证器，即漫游认证器，包括蓝牙、NFC、USB等。

[]()[]()

#### FIDO2_AuthenticatorTransport

```ets
enum [FIDO2_AuthenticatorTransport](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga02592e5b749c266e7297333afce03cec)
```

**描述**

认证器传输方式的枚举，表示认证器和客户端设备之间传递认证数据的方式。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_USB

USB方式。

****FIDO2_NFC

NFC方式。

****FIDO2_BLE

BLE方式。

****FIDO2_SMART_CARD

智能卡方式。

****FIDO2_HYBRID

混合方式。即支持多种传输方式

****FIDO2_INTERNAL

内部方式。

[]()[]()

#### FIDO2_ClientCapability

```ets
enum [FIDO2_ClientCapability](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gae8cdc5641132b84e0313c7412d13bbbe)
```

**描述**

客户端能力的枚举。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_CONDITIONAL_CREATE

通行密钥注册。

****FIDO2_CONDITIONAL_GET

通行密钥认证。

****FIDO2_HYBRID_TRANSPORT

混合传输，表示支持多种传输方式。

****FIDO2_PASSKEY_PLATFORM_AUTHENTICATOR

Passkey平台认证器。

****FIDO2_USER_VERIFYING_PLATFORM_AUTHENTICATOR

用户认证平台认证器

****FIDO2_RELATED_ORIGINS

支持相关源/域的凭据操作。

****FIDO2_SIGNAL_ALL_ACCEPTED_CREDENTIALS

发送所有接受的凭据。

****FIDO2_SIGNAL_CURRENT_USER_DETAILS

发送当前用户详细信息。

****FIDO2_SIGNAL_UNKNOWN_CREDENTIAL

发送未知凭据。

****FIDO2_EXTENSION_UVI

uvi的扩展参数。

[]()[]()

#### FIDO2_CredentialMediationRequirement

```ets
enum [FIDO2_CredentialMediationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga16035d1941d25a1ea71203ad72809b93)
```

**描述**

用户介入要求的枚举。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_SILENT

禁止用户介入指定的操作。如果可以在不需要用户介入的情况下进行操作，则正常。 如果需要用户介入，则操作将返回null。

****FIDO2_OPTIONAL

如果在没有用户介入的情况下，可以为给定的操作传递凭据，则正常传递。 如果需要用户介入，那么用户代理将让用户介入决策。

****FIDO2_CONDITIONAL

有条件的需要用户介入。对于认证场景，如果设备有凭据，则需要用户介入以选择凭据。对于注册场景，如果用户之前已同意创建凭据，可在无用户介入的情况下创建凭据。

****FIDO2_MEDIATION_REQUIRED

在没有用户介入的情况下，用户代理将不会移交凭证。

[]()[]()

#### FIDO2_ErrorCode

```ets
enum [FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693)
```

**描述**

错误码定义。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_SUCCESS

成功。

****FIDO2_PERMISSION_DENIED

权限被拒绝。

FIDO2_DEVICE_NOT_SUPPORT

设备类型错误。

**起始版本**：6.0.1(21)

****FIDO2_NOT_SUPPORT

系统不支持。

****FIDO2_INVALID_STATE

无效的状态。

****FIDO2_INTEGRITY_CHECK_FAILED

系统完整性校验失败。

****FIDO2_USER_ABORT

用户中止。

****FIDO2_TIMEOUT

超时。

****FIDO2_ENCODING_ERROR

编码错误。

****FIDO2_UNKNOWN_ERROR

未知错误。

****FIDO2_CONSTRAINT_ERROR

约束条件错误。

****FIDO2_DATA_ERROR

数据错误。

****FIDO2_USER_REJECTS

用户拒绝。

****FIDO2_CONNECT_SERVICE_FAILED

连接服务失败。

FIDO2_MAX_CRED_NUM_REACHED

凭据达到上限。

****FIDO2_INVALID_CTAP_COMMAND

无效的CTAP命令。

****FIDO2_INVALID_PARAMETERS

命令包含无效参数。

****FIDO2_INVALID_MESSAGE_OR_ATTRIBUTE_LENGTH

无效的消息或属性长度。

****FIDO2_INVALID_CBOR_OR_UNPREDICTABLE

无效的CBOR或不可预知的错误。

****FIDO2_PARSE_CBOR_FAILED

解析CBOR失败。

****FIDO2_INVALID_CREDENTIALS

未提供有效凭据。

FIDO2_NOT_ALLOWED

不允许。

****FIDO2_USER_VERIFICATION_FAILED

用户认证失败。

****FIDO2_OTHER_ERROR

其他错误。

[]()[]()

#### FIDO2_PublicKeyCredentialHint

```ets
enum [FIDO2_PublicKeyCredentialHint](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gab7b1367ea48debe767ae103f8ac9e96c)
```

**描述**

认证方式指示的枚举，用于指示用户选用哪种认证方式。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_SECURITY_KEY

安全密钥。

****FIDO2_CLIENT_DEVICE

客户端设备。

****FIDO2_HINT_HYBRID

混合。

[]()[]()

#### FIDO2_PublicKeyCredentialType

```ets
enum [FIDO2_PublicKeyCredentialType](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__gaa46edbba8f1162737d26681080eea727)
```

**描述**

公钥凭据类型的枚举。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_PUBLIC_KEY

公钥。

[]()[]()

#### FIDO2_TokenBindingStatus

```ets
enum [FIDO2_TokenBindingStatus](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga3a0c5c93081cd75c8ecd7a1efac8252e)
```

**描述**

TokenBinding协议的状态。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_PRESENT

正常通信时的状态。

****FIDO2_SUPPORTED

支持令牌绑定，但是在与依赖方通信时未进行协商。

[]()[]()

#### FIDO2_UserVerificationRequirement

```ets
enum [FIDO2_UserVerificationRequirement](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga632b7b26c16a519650398ccfc3515f7a)
```

**描述**

依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_REQUIRED

需要进行用户认证。

****FIDO2_PREFERRED

在可能的情况下，依赖方优先处理操作的用户认证， 但如果响应没有设置用户认证标志，则不会失败。

****FIDO2_DISCOURAGED

依赖方在操作过程中不希望使用用户鉴权。

[]()[]()

#### FIDO2_Uvm

```ets
enum [FIDO2_Uvm](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga60fda18b064802349b186de072b43e98)
```

**描述**

UVM的枚举。

**起始版本：** 6.0.0(20)

枚举值

描述

****FIDO2_UVM_FINGERPRINT

指纹认证器。

****FIDO2_UVM_PIN

PIN认证器。

****FIDO2_UVM_FACEPRINT

3D人脸认证器。

[]()[]()

#### 函数说明

[]()[]()

#### HMS_FIDO2_authenticate()

```ets
[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693) HMS_FIDO2_authenticate (const [FIDO2_CredentialRequestOptions](../security/FIDO2_CredentialRequestOptions.md) options, const [FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md) tokenBinding, const char * origin, [FIDO2_PublicKeyAssertionCredential](../security/FIDO2_PublicKeyAssertionCredential.md) ** publicKeyAssertionCredential)
```

**描述**

通行密钥认证。仅支持非UI线程调用。

**申请权限：**ohos.permission.ACCESS_FIDO2_ONLINEAUTH

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

options

认证请求选项。

tokenBinding

认证令牌绑定。

origin

调用该方法时的安全来源。长度限制0到256。

publicKeyAssertionCredential

认证响应。

**返回：**

如果函数执行成功，则返回FIDO2_SUCCESS；如果函数执行失败，则返回特定的错误代码。详细信息请参见[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga313648b7100419fc2cd6c1a73b0ad7ec)。

[]()[]()

#### HMS_FIDO2_AuthenticatorMetadataArray_Destroy()

```ets
void HMS_FIDO2_AuthenticatorMetadataArray_Destroy ([FIDO2_AuthenticatorMetadataArray](../security/FIDO2_AuthenticatorMetadataArray.md) * authenticators)
```

**描述**

释放认证者元数据数组。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

authenticators

要释放的鉴权字元数据数组。

[]()[]()

#### HMS_FIDO2_CapabilityArray_Destroy()

```ets
void HMS_FIDO2_CapabilityArray_Destroy ([FIDO2_CapabilityArray](../system-services/FIDO2_CapabilityArray.md) * capability)
```

**描述**

释放能力的数组。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

capability

要释放的能力的数组。

[]()[]()

#### HMS_FIDO2_getClientCapability()

```ets
[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693) HMS_FIDO2_getClientCapability ([FIDO2_CapabilityArray](../system-services/FIDO2_CapabilityArray.md) ** capability)
```

**描述**

查询当前设备/版本支持的客户端能力列表。当给定功能的值为true时，表示通行密钥客户端当前支持该能力。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

capability

客户端是否支持此特性。

**返回：**

如果函数执行成功，则返回FIDO2_SUCCESS； 如果函数执行失败，则返回错误代码。详细信息请参见[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga313648b7100419fc2cd6c1a73b0ad7ec)。

[]()[]()

#### HMS_FIDO2_getPlatformAuthenticator()

```ets
[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693) HMS_FIDO2_getPlatformAuthenticator ([FIDO2_AuthenticatorMetadataArray](../security/FIDO2_AuthenticatorMetadataArray.md) ** authenticators)
```

**描述**

获取支持的平台身份认证器列表。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

authenticators

支持的平台认证器列表。

**返回：**

如果函数执行成功，则返回FIDO2_SUCCESS；如果函数执行失败，则返回错误代码。详细信息请参见[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga313648b7100419fc2cd6c1a73b0ad7ec)。

[]()[]()

#### HMS_FIDO2_initCreationOptions()

```ets
void HMS_FIDO2_initCreationOptions ([FIDO2_CredentialCreationOptions](../security/FIDO2_CredentialCreationOptions.md) * options)
```

**描述**

初始化FIDO2_CredentialCreationOptions结构。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

options

指向要初始化的FIDO2_CredentialCreationOptions结构体的指针。

[]()[]()

#### HMS_FIDO2_initRequestOptions()

```ets
void HMS_FIDO2_initRequestOptions ([FIDO2_CredentialRequestOptions](../security/FIDO2_CredentialRequestOptions.md) * options)
```

**描述**

初始化FIDO2_CredentialRequestOptions结构。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

options

指向要初始化的FIDO2_CredentialRequestOptions结构体的指针。

[]()[]()

#### HMS_FIDO2_initTokenBinding()

```ets
void HMS_FIDO2_initTokenBinding ([FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md) * tokenBinding)
```

**描述**

初始化FIDO2_TokenBinding结构体。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

tokenBinding

指向要初始化的FIDO2_TokenBinding结构体的指针。

[]()[]()

#### HMS_FIDO2_PublicKeyAssertionCredential_Destroy()

```ets
void HMS_FIDO2_PublicKeyAssertionCredential_Destroy ([FIDO2_PublicKeyAssertionCredential](../security/FIDO2_PublicKeyAssertionCredential.md) * publicKeyAssertionCredential)
```

**描述**

释放PublicKeyAssertionCredential的结构体。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

publicKeyAssertionCredential

要释放的PublicKeyAssertionCredential的结构体。

[]()[]()

#### HMS_FIDO2_PublicKeyAttestationCredential_Destroy()

```ets
void HMS_FIDO2_PublicKeyAttestationCredential_Destroy ([FIDO2_PublicKeyAttestationCredential](../security/FIDO2_PublicKeyAttestationCredential.md) * publicKeyAttestationCredential)
```

**描述**

释放PublicKeyAttestationCredential的结构体。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

publicKeyAttestationCredential

要释放的PublicKeyAttestationCredential的结构体。

[]()[]()

#### HMS_FIDO2_register()

```ets
[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga759dad4964a084008360c4b99e2ec693) HMS_FIDO2_register (const [FIDO2_CredentialCreationOptions](../security/FIDO2_CredentialCreationOptions.md) options, const [FIDO2_TokenBinding](../security/FIDO2_TokenBinding.md) tokenBinding, const char * origin, [FIDO2_PublicKeyAttestationCredential](../security/FIDO2_PublicKeyAttestationCredential.md) ** publicKeyAttestationCredential)
```

**描述**

通行密钥注册。仅支持非UI线程调用。

**申请权限：**ohos.permission.ACCESS_FIDO2_ONLINEAUTH

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

options

注册请求选项。

tokenBinding

注册令牌绑定。

origin

调用该方法时的来源。长度限制0到256。

publicKeyAttestationCredential

注册响应。

**返回：**

如果函数执行成功，则返回FIDO2_SUCCESS；如果函数执行失败，则返回错误代码。详细信息请参见[FIDO2_ErrorCode](通行密钥 (passkey).md#ZH-CN_TOPIC_0000002523299537__ga313648b7100419fc2cd6c1a73b0ad7ec)。