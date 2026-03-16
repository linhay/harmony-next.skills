# SecurityAntivirus_Antivirus

#### 概述

定义防病毒应用信息。

**起始版本：** 6.0.0(20)

**相关模块：**[SecurityAntivirus](SecurityAntivirus.md)

**所在头文件：**[security_antivirus.h](../../capi/headers/security_antivirus.h.md)

#### 汇总

#### 成员变量

名称

描述

const char *[bundleName](#ZH-CN_TOPIC_0000002515108491__zh-cn_topic_0000002337386737_a165e68661c3730398273e1481d7f37f9)

防病毒应用包名

const char *[metadata](#ZH-CN_TOPIC_0000002515108491__zh-cn_topic_0000002337386737_ae66aa2161522f515b0ec6e1a5e4732e0)

防病毒应用信息（当前版本号、上次更新时间、病毒防护开关状态、用户ID）

#### 结构体成员变量说明

#### bundleName

```ets
const char *SecurityAntivirus_Antivirus::bundleName
```

**描述**

防病毒应用包名，包名字段要求请参见[链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file)。

#### metadata

```ets
const char *SecurityAntivirus_Antivirus::metadata
```

**描述**

防病毒应用信息（包含当前版本号、上次更新时间、病毒防护状态、用户ID的json字符串），其中版本号字段要求请参见[链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file)，上次更新时间为10位秒级或13位毫秒级时间戳，病毒防护状态仅限on或off，user_id为用户ID。示例格式如下：

```ets
{
"version": "1.0.0.0",
"last_update_time": "1751877696",
"protection_status": "on/off"，
"user_id": "100"
}
```