# security_antivirus.h

**概述**

文件中定义了与病毒防护服务管理相关的函数。

引用文件： <DeviceSecurityKit/security_antivirus.h>

库： libsecurityantivirus_ndk.z.so

系统能力： SystemCapability.Security.SecurityAntivirus

起始版本： 6.0.0(20)

相关模块： [SecurityAntivirus](SecurityAntivirus.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct SecurityAntivirus_Antivirus | 定义病毒防护服务应用信息，包含包名、当前版本号、上次更新时间、病毒防护开关状态、用户ID。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| SecurityAntivirus_ErrCode{ SECURITY_ANTIVIRUS_SUCCESS = 0, SECURITY_ANTIVIRUS_PERMISSION_NOT_GRANTED = 201, SECURITY_ANTIVIRUS_PARAM_INVALID = 1019900001, SECURITY_ANTIVIRUS_NO_REGISTER = 1019900002, SECURITY_ANTIVIRUS_INNER_ERROR = 1019900003 } | 定义病毒防护服务管理错误码。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_RegisterAntivirus(const char* bundleName) | 三方EDR应用向HarmonyOS安全防护服务注册。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_UnregisterAntivirus(const char* bundleName) | 三方EDR应用从HarmonyOS安全防护服务注销。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_UpdateAntivirus(const SecurityAntivirus_Antivirus* antivirus) | 三方EDR应用向HarmonyOS安全防护服务更新信息，包含包名、当前版本号、上次更新时间、病毒防护开关状态、用户ID。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_QueryAntivirus(SecurityAntivirus_Antivirus** list, uint32_t* length) | 零信任应用向HarmonyOS安全防护服务查询当前所有三方EDR注册信息。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_QueryPreinstalledAntivirus(SecurityAntivirus_Antivirus** list, uint32_t* length) | MDM应用向HarmonyOS安全防护服务查询所有用户的防病毒功能状态。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_EnablePreinstalledAntivirus(void) | MDM应用启用HarmonyOS安全防护服务所有用户的防病毒功能。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_DisablePreinstalledAntivirus(void) | MDM应用禁用HarmonyOS安全防护服务所有用户的防病毒功能。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_EnablePreinstalledAntivirusByAccount(int32_t accountId) | MDM应用启用HarmonyOS安全防护服务中用户ID为accountId的防病毒功能。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_DisablePreinstalledAntivirusByAccount(int32_t accountId) | MDM应用禁用HarmonyOS安全防护服务中用户ID为accountId的防病毒功能。 |