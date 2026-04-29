# fido2_api.h

**概述**

定义身份认证扩展的接口。

库： libfido2_ndk.z.so

引用文件： <OnlineAuthenticationKit/fido2_api.h>

系统能力： SystemCapability.Security.FIDO2

起始版本： 6.0.0(20)

相关模块： [FIDO2](通行密钥.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct Uint8Buff | 定义uint8_t字节流。 |
| struct AuthenticationExtensionsClientOutputs | 身份认证扩展。 |
| struct FIDO2_AuthenticatorResponse | 定义获取认证器断言响应的结构体。 |
| struct FIDO2_PublicKeyAssertionCredential | 定义获取认证结果结构体。 |
| struct FIDO2_AuthenticatorTransportArray | 认证器传输方式数组。 |
| struct FIDO2_AuthenticatorAttestationResponse | 认证器声明响应。 |
| struct FIDO2_PublicKeyAttestationCredential | 定义获取注册结果结构体。 |
| struct FIDO2_AuthenticatorSelectionCriteria | 由webAuthn依赖方（即接入协议的应用或网页）指定，与认证器有关。 |
| struct FIDO2_PublicKeyCredentialDescriptor | 用于注册或认证凭据的参数。 |
| struct FIDO2_PublicKeyCredentialParameters | 认证凭据的附加参数。 |
| struct FIDO2_PublicKeyCredentialUserEntity | 创建新凭据时用户的属性。 |
| struct FIDO2_PublicKeyCredentialRpEntity | 创建新凭据时依赖方的属性。 |
| struct FIDO2_PublicKeyCredentialDescriptorArray | PublicKey凭证描述符数组。 |
| struct FIDO2_PublicKeyCredentialHintArray | 认证方式指示数组。 |
| struct FIDO2_PublicKeyCredentialRequestOptions | 定义通行密钥认证请求参数。 |
| struct FIDO2_CredentialCreationOptionArray | 认证凭据的附加参数数组。 |
| struct FIDO2_AttestationFormatsArray | 依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。 |
| struct FIDO2_PublicKeyCredentialCreationOptions | 创建新的认证凭据的选项。 |
| struct FIDO2_CredentialCreationOptions | 凭据请求的选项。 |
| struct FIDO2_AuthenticatorMetadata | 认证器元数据。 |
| struct FIDO2_CredentialRequestOptions | 认证信息字典对象。 |
| struct FIDO2_AuthenticatorMetadataArray | 描述支持的认证器数组。 |
| struct FIDO2_Capability | 通行密钥能力的结构体。 |
| struct FIDO2_CapabilityArray | 描述能力数组。 |
| struct FIDO2_TokenBinding | Token binding协议，用于客户端与依赖方通信。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct Uint8Buff Uint8Buff | 定义uint8_t字节流。 |
| typedef enum FIDO2_TokenBindingStatus FIDO2_TokenBindingStatus | TokenBinding协议的状态。 |
| typedef enum FIDO2_AttestationConveyancePreference FIDO2_AttestationConveyancePreference | 供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。 |
| typedef enum FIDO2_UserVerificationRequirement FIDO2_UserVerificationRequirement | 依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。 |
| typedef enum FIDO2_AuthenticatorAttachment FIDO2_AuthenticatorAttachment | 认证器信息（平台、漫游）。 |
| typedef enum FIDO2_AuthenticatorTransport FIDO2_AuthenticatorTransport | 认证器传输方式的枚举。 |
| typedef enum FIDO2_Algorithm FIDO2_Algorithm | 加密算法的枚举。 |
| typedef enum FIDO2_PublicKeyCredentialHint FIDO2_PublicKeyCredentialHint | 认证方式指示的枚举。 |
| typedef enum FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialType | 公钥凭据类型的枚举。 |
| typedef enum FIDO2_Uvm FIDO2_Uvm | UVM的枚举。 |
| typedef enum FIDO2_ClientCapability FIDO2_ClientCapability | 客户端能力的枚举。 |
| typedef enum FIDO2_CredentialMediationRequirement FIDO2_CredentialMediationRequirement | 用户介入要求的枚举。 |
| typedef enum FIDO2_ErrorCode FIDO2_ErrorCode | 错误码定义。 |
| typedef struct AuthenticationExtensionsClientOutputs AuthenticationExtensionsClientOutputs | 身份认证扩展。 |
| typedef struct FIDO2_AuthenticatorResponse FIDO2_AuthenticatorResponse | 定义获取认证器断言响应的结构体。 |
| typedef struct FIDO2_PublicKeyAssertionCredential FIDO2_PublicKeyAssertionCredential | 定义获取认证结果结构体。 |
| typedef struct FIDO2_AuthenticatorTransportArray FIDO2_AuthenticatorTransportArray | 认证器传输方式数组。 |
| typedef struct FIDO2_AuthenticatorAttestationResponse FIDO2_AuthenticatorAttestationResponse | 认证器声明响应。 |
| typedef struct FIDO2_PublicKeyAttestationCredential FIDO2_PublicKeyAttestationCredential | 定义获取注册结果结构体。 |
| typedef struct FIDO2_AuthenticatorSelectionCriteria FIDO2_AuthenticatorSelectionCriteria | 由webAuthn依赖方指定，与认证器有关。 |
| typedef struct FIDO2_PublicKeyCredentialDescriptor FIDO2_PublicKeyCredentialDescriptor | 用于注册或认证凭据的参数。 |
| typedef struct FIDO2_PublicKeyCredentialParameters FIDO2_PublicKeyCredentialParameters | 认证凭据的附加参数。 |
| typedef struct FIDO2_PublicKeyCredentialUserEntity FIDO2_PublicKeyCredentialUserEntity | 创建新凭据时用户的属性。 |
| typedef struct FIDO2_PublicKeyCredentialRpEntity FIDO2_PublicKeyCredentialRpEntity | 创建新凭据时依赖方的属性。 |
| typedef struct FIDO2_PublicKeyCredentialDescriptorArray FIDO2_PublicKeyCredentialDescriptorArray | PublicKey凭证描述符数组。 |
| typedef struct FIDO2_PublicKeyCredentialHintArray FIDO2_PublicKeyCredentialHintArray | 认证方式指示数组。 |
| typedef struct FIDO2_PublicKeyCredentialRequestOptions FIDO2_PublicKeyCredentialRequestOptions | 定义通行密钥认证请求参数。 |
| typedef struct FIDO2_CredentialCreationOptionArray FIDO2_CredentialCreationOptionArray | 认证凭据的附加参数数组。 |
| typedef struct FIDO2_AttestationFormatsArray FIDO2_AttestationFormatsArray | 依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。 |
| typedef struct FIDO2_PublicKeyCredentialCreationOptions FIDO2_PublicKeyCredentialCreationOptions | 创建新的认证凭据的选项。 |
| typedef struct FIDO2_CredentialCreationOptions FIDO2_CredentialCreationOptions | 凭据请求的选项。 |
| typedef struct FIDO2_AuthenticatorMetadata FIDO2_AuthenticatorMetadata | 认证器元数据。 |
| typedef struct FIDO2_CredentialRequestOptions FIDO2_CredentialRequestOptions | 认证信息字典对象。 |
| typedef struct FIDO2_AuthenticatorMetadataArray FIDO2_AuthenticatorMetadataArray | 描述支持的认证器数组。 |
| typedef struct FIDO2_Capability FIDO2_Capability | 通行密钥能力的结构体。 |
| typedef struct FIDO2_CapabilityArray FIDO2_CapabilityArray | 描述能力数组。 |
| typedef struct FIDO2_TokenBinding FIDO2_TokenBinding | Token binding（协议），用于客户端与依赖方通信。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| FIDO2_TokenBindingStatus { FIDO2_PRESENT = 0, FIDO2_SUPPORTED = 1 } | TokenBinding协议的状态。 |
| FIDO2_AttestationConveyancePreference { FIDO2_NONE = 0, FIDO2_INDIRECT = 1, FIDO2_DIRECT = 2, FIDO2_ENTERPRISE = 3 } | 供WebAuthn依赖方在生成凭据时参考，以指定凭据传递的首选项。 |
| FIDO2_UserVerificationRequirement { FIDO2_REQUIRED = 0, FIDO2_PREFERRED = 1, FIDO2_DISCOURAGED = 2 } | 依赖方可能需要对某些操作进行用户鉴权（认证当前用户是否为用户）， 但不需要对其他操作进行认证。定义枚举类型是为了区分不同的需求级别。 |
| FIDO2_AuthenticatorAttachment { FIDO2_PLATFORM = 0, FIDO2_CROSS_PLATFORM = 1 } | 认证器信息（平台、漫游）。 |
| FIDO2_AuthenticatorTransport { FIDO2_USB = 0, FIDO2_NFC = 1, FIDO2_BLE = 2, FIDO2_SMART_CARD = 3, FIDO2_HYBRID = 4, FIDO2_INTERNAL = 5 } | 认证器传输方式的枚举。 |
| FIDO2_Algorithm { FIDO2_ES256 = -7, FIDO2_ES384 = -35, FIDO2_ES512 = -36, FIDO2_RS256 = -257, FIDO2_RS384 = -258, FIDO2_RS512 = -259, FIDO2_PS256 = -37, FIDO2_PS384 = -38, FIDO2_PS512 = -39 } | 算法的枚举。 |
| FIDO2_PublicKeyCredentialHint { FIDO2_SECURITY_KEY = 0, FIDO2_CLIENT_DEVICE = 1, FIDO2_HINT_HYBRID = 2 } | 认证方式指示的枚举。 |
| FIDO2_PublicKeyCredentialType { FIDO2_PUBLIC_KEY = 0 } | 公钥凭据类型的枚举。 |
| FIDO2_Uvm { FIDO2_UVM_FINGERPRINT = 2, FIDO2_UVM_PIN = 4, FIDO2_UVM_FACEPRINT = 16 } | UVM的枚举。 |
| FIDO2_ClientCapability { FIDO2_CONDITIONAL_CREATE = 0, FIDO2_CONDITIONAL_GET = 1, FIDO2_HYBRID_TRANSPORT = 2, FIDO2_PASSKEY_PLATFORM_AUTHENTICATOR = 3, FIDO2_USER_VERIFYING_PLATFORM_AUTHENTICATOR = 4, FIDO2_RELATED_ORIGINS = 5, FIDO2_SIGNAL_ALL_ACCEPTED_CREDENTIALS = 6, FIDO2_SIGNAL_CURRENT_USER_DETAILS = 7, FIDO2_SIGNAL_UNKNOWN_CREDENTIAL = 8, FIDO2_EXTENSION_UVI = 9 } | 客户端能力的枚举。 |
| FIDO2_CredentialMediationRequirement { FIDO2_SILENT = 0, FIDO2_OPTIONAL = 1, FIDO2_CONDITIONAL = 2, FIDO2_MEDIATION_REQUIRED = 3 } | 用户介入要求的枚举。 |
| FIDO2_ErrorCode { FIDO2_SUCCESS = 0, FIDO2_PERMISSION_DENIED = 201, FIDO2_DEVICE_NOT_SUPPORT = 801, FIDO2_NOT_SUPPORT = 1021300001, FIDO2_INVALID_STATE = 1021300002, FIDO2_INTEGRITY_CHECK_FAILED = 1021300003, FIDO2_USER_ABORT = 1021300004, FIDO2_TIMEOUT = 1021300005, FIDO2_ENCODING_ERROR = 1021300006, FIDO2_UNKNOWN_ERROR = 1021300007, FIDO2_CONSTRAINT_ERROR = 1021300008, FIDO2_DATA_ERROR = 1021300009, FIDO2_USER_REJECTS = 1021300010, FIDO2_CONNECT_SERVICE_FAILED = 1021300011, FIDO2_MAX_CRED_NUM_REACHED = 1021300012, FIDO2_INVALID_CTAP_COMMAND = 1021310001, FIDO2_INVALID_PARAMETERS = 1021310002, FIDO2_INVALID_MESSAGE_OR_ATTRIBUTE_LENGTH = 1021310003, FIDO2_INVALID_CBOR_OR_UNPREDICTABLE = 1021310004, FIDO2_PARSE_CBOR_FAILED = 1021310005, FIDO2_INVALID_CREDENTIALS = 1021310006, FIDO2_NOT_ALLOWED = 1021310007, FIDO2_USER_VERIFICATION_FAILED = 1021310008, FIDO2_OTHER_ERROR = 1021310009 } | 错误码定义。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| void HMS_FIDO2_initCreationOptions (FIDO2_CredentialCreationOptions *options) | 初始化FIDO2_CredentialCreationOptions结构。 |
| void HMS_FIDO2_initTokenBinding (FIDO2_TokenBinding *tokenBinding) | 初始化FIDO2_TokenBinding结构体。 |
| void HMS_FIDO2_initRequestOptions (FIDO2_CredentialRequestOptions *options) | 初始化FIDO2_CredentialRequestOptions结构。 |
| FIDO2_ErrorCode HMS_FIDO2_getClientCapability (FIDO2_CapabilityArray **capability) | 查询当前设备支持的客户端能力列表。当给定功能的值为true时，表示通行密钥客户端当前支持该能力。 |
| FIDO2_ErrorCode HMS_FIDO2_getPlatformAuthenticator (FIDO2_AuthenticatorMetadataArray **authenticators) | 获取支持的平台身份认证器列表。 |
| FIDO2_ErrorCode HMS_FIDO2_register (const FIDO2_CredentialCreationOptions options, const FIDO2_TokenBinding tokenBinding, const char *origin, FIDO2_PublicKeyAttestationCredential **publicKeyAttestationCredential) | 通行密钥注册。 |
| FIDO2_ErrorCode HMS_FIDO2_authenticate (const FIDO2_CredentialRequestOptions options, const FIDO2_TokenBinding tokenBinding, const char *origin, FIDO2_PublicKeyAssertionCredential **publicKeyAssertionCredential) | 基于fido2的认证。 |
| void HMS_FIDO2_CapabilityArray_Destroy (FIDO2_CapabilityArray *capability) | 释放能力的数组。 |
| void HMS_FIDO2_AuthenticatorMetadataArray_Destroy (FIDO2_AuthenticatorMetadataArray *authenticators) | 释放认证者元数据数组。 |
| void HMS_FIDO2_PublicKeyAttestationCredential_Destroy (FIDO2_PublicKeyAttestationCredential *publicKeyAttestationCredential) | 释放PublicKeyAttestationCredential的结构体。 |
| void HMS_FIDO2_PublicKeyAssertionCredential_Destroy (FIDO2_PublicKeyAssertionCredential *publicKeyAssertionCredential) | 释放PublicKeyAssertionCredential的结构体。 |