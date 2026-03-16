# security_antivirus.h

#### 概述

文件中定义了与病毒防护服务管理相关的函数。

**库：** libsecurityantivirus_ndk.z.so

**系统能力：** SystemCapability.Security.SecurityAntivirus

**起始版本：** 6.0.0(20)

**相关模块：**[SecurityAntivirus](../../topics/security/SecurityAntivirus.md)

#### 汇总

#### 结构体

名称

描述

struct [SecurityAntivirus_Antivirus](../../topics/security/SecurityAntivirus_Antivirus.md)

定义病毒防护服务应用信息，包含包名、当前版本号、上次更新时间、病毒防护开关状态、用户ID。

#### 枚举

名称

描述

[SecurityAntivirus_ErrCode](../../topics/security/SecurityAntivirus.md#section7961454596){

SECURITY_ANTIVIRUS_SUCCESS = 0,

SECURITY_ANTIVIRUS_PERMISSION_NOT_GRANTED = 201,

SECURITY_ANTIVIRUS_PARAM_INVALID = 1019900001,

SECURITY_ANTIVIRUS_NO_REGISTER = 1019900002,

SECURITY_ANTIVIRUS_INNER_ERROR = 1019900003

}

定义病毒防护服务管理错误码。

#### 函数

名称

描述

SecurityAntivirus_ErrCode [HMS_SecurityAntivirus_RegisterAntivirus](../../topics/security/SecurityAntivirus.md#section556519812196)(const char* bundleName)

三方EDR应用向HarmonyOS安全防护服务注册。

SecurityAntivirus_ErrCode [HMS_SecurityAntivirus_UnregisterAntivirus](../../topics/security/SecurityAntivirus.md#section3962618203519)(const char* bundleName)

三方EDR应用从HarmonyOS安全防护服务注销。

SecurityAntivirus_ErrCode [HMS_SecurityAntivirus_UpdateAntivirus](../../topics/security/SecurityAntivirus.md#section5548172953619)(const [SecurityAntivirus_Antivirus](../../topics/security/SecurityAntivirus_Antivirus.md)* antivirus)

三方EDR应用向HarmonyOS安全防护服务更新信息，包含包名、当前版本号、上次更新时间、病毒防护开关状态、用户ID。

SecurityAntivirus_ErrCode [HMS_SecurityAntivirus_QueryAntivirus](../../topics/security/SecurityAntivirus.md#section499213812378)([SecurityAntivirus_Antivirus](../../topics/security/SecurityAntivirus_Antivirus.md)** list, uint32_t* length)

零信任应用向HarmonyOS安全防护服务查询当前所有三方EDR注册信息。

SecurityAntivirus_ErrCode [HMS_SecurityAntivirus_QueryPreinstalledAntivirus](../../topics/security/SecurityAntivirus.md#section109159243919)([SecurityAntivirus_Antivirus](../../topics/security/SecurityAntivirus_Antivirus.md)** list, uint32_t* length)

MDM应用向HarmonyOS安全防护服务查询所有用户的防病毒功能状态。

SecurityAntivirus_ErrCode [HMS_SecurityAntivirus_EnablePreinstalledAntivirus](../../topics/security/SecurityAntivirus.md#section284719393418)(void)

MDM应用启用HarmonyOS安全防护服务所有用户的防病毒功能。

SecurityAntivirus_ErrCode [HMS_SecurityAntivirus_DisablePreinstalledAntivirus](../../topics/security/SecurityAntivirus.md#section16629747456)(void)

MDM应用禁用HarmonyOS安全防护服务所有用户的防病毒功能。

SecurityAntivirus_ErrCode [HMS_SecurityAntivirus_EnablePreinstalledAntivirusByAccount](../../topics/security/SecurityAntivirus.md#section1272125114210)(int32_t accountId)

MDM应用启用HarmonyOS安全防护服务中用户ID为accountId的防病毒功能。

SecurityAntivirus_ErrCode [HMS_SecurityAntivirus_DisablePreinstalledAntivirusByAccount](../../topics/security/SecurityAntivirus.md#section373142512429)(int32_t accountId)

MDM应用禁用HarmonyOS安全防护服务中用户ID为accountId的防病毒功能。