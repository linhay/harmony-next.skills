[]()[]()

# BusinessRiskIntelligentDetection（业务风险检测）

- 识别当前设备的涉诈行为风险。

**起始版本: **5.0.0(12)

- 提供自动化点击、设备墙等作弊行为检测能力。

**起始版本: **6.0.0(20)

[]()[]()

#### 导入模块

```ets
import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
```

[]()[]()

#### FraudDetectionRequest

涉诈剧本检测的请求参数。

**系统能力：**SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

nonce

Uint8Array

否

否

开发者应用传入的一个随机生成的nonce值，用于防重放攻击，在检测结果中会包含该值。nonce值必须为24至80字节之间。

algorithm

[SigningAlgorithm](#section10182122284411)

否

否

数字签名算法。

version

number

否

是

检测结果消息格式的版本，默认值为1，可选1和2，取值为2时检测结果的Tag标签中带有时间属性和风险等级，其中时间属性表示该标签对应线索的最后一次发生时间，风险等级表示该标签对应的风险级别，取值为1时，检测结果Tag标签中不带时间属性和风险等级。

**起始版本：**5.1.0(18)

[]()[]()

#### SimulatedClickDetectionRequest

模拟点击检测的请求参数。

**系统能力****：**SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：**6.0.0(20)

**名称**

**类型**

只读

可选

**说明**

version

number

否

是

检测结果消息格式的版本，默认值为1，当前只支持1。

[]()[]()

#### SimulatedClickDetectionEnhancedRequest

模拟点击增强检测的请求参数。

系统能力：SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：**6.0.2(22)

**名称**

**类型**

只读

可选

**说明**

nonce

Uint8Array

否

否

开发者应用传入的一个随机生成的nonce值，用于防重放攻击，在检测结果中会包含该值。nonce值必须为24至80字节之间。

algorithm

[SigningAlgorithm](#section10182122284411)

否

否

数字签名算法。

version

number

否

是

检测结果消息格式的版本，默认值为1，当前版本号只支持1。

[]()[]()

#### SigningAlgorithm

数字签名算法。

**系统能力：**SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：**5.0.0(12)

名称

值

说明

ES256

0

SHA256withECDSA。

[]()[]()

#### detectFraudRisk

detectFraudRisk(params: [FraudDetectionRequest](#section165215281222)): Promise<string>

获取本设备的涉诈行为风险。使用Promise异步回调。

**系统能力：**SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：**5.0.0(12)

**参数**：

参数名

类型

必填

说明

params

[FraudDetectionRequest](#section165215281222)

是

请求参数。

**返回值：**

类型

说明

Promise<string>

Promise对象，返回涉诈风险检测结果，一个JSON Web Signature格式的字符串，使用Base64URL编码，如果发生异常或错误，则返回错误码。

JWS的Header字段如下：

```ets
{
    "alg": "ES256",
    "x5c": ["",""]
}
```

- "alg"：数字签名算法，ES256表示为SHA256withECDSA。
- "x5c"：华为签名服务器对JWS签名的证书链，x5c[0]为给JWS签名的证书，x5c[1]为华为设备CA。

JWS的Payload字段如下：

1.当请求参数FraudDetectionRequest中的version为1，Payload样例：

```ets
{
    "timestampMs": 9xxxxxxxxx,
    "nonce": "Rxxxxxxxxx",
    "appId": "xxxxxxxxx",
    "version": 1,
    "riskScore": 90,
    "tags": [
        "phishing",
        "malware",
        "interdiction",
        "control"
    ]
}
```

2. 当请求参数FraudDetectionRequest中的version为2，Payload样例：

```ets
{
    "timestampMs": 9xxxxxxxxx,
    "nonce": "Rxxxxxxxxx",
    "appId": "xxxxxxxxx",
    "version": 2,
    "riskScore": 90,
    "tags": [
        {"tag": "phishing", "level": "high", "lastTime": 9876543216548},
        {"tag": "malware", "level": "low", "lastTime": 965432198756},
        {"tag": "interdiction", "level": "medium", "lastTime": 965432198756},
        {"tag": "control", "level": "medium", "lastTime": 965432198123}
    ]
}
```

 说明：

- nonce：调用detectFraudRisk接口时传入的nonce值Base64编码。
- timestampMs：华为签名服务器生成的时间戳。
- appId：签名信息中的appId。
- riskScore：当前设备上涉诈风险评分，分数范围0~100，分数越高标识风险越大。
- tags：涉诈风险线索。如果tags列表为空，表示未发现涉诈风险。
- version：检测结果消息格式的版本。

tags值含义如下

tags值

含义

phishing

过去一段时间设备上发生了涉诈信息引导行为。命中一个或多个下面的风险因子：

近期接听过涉诈电话

近期接收到诈骗短信

近期访问涉诈网址

malware

过去一段时间设备上安装/运行的应用可能成为诈骗分子使用的工具。命中一个或多个下面的风险因子：

近期安装过/正在运行小众聊天类APP

近期安装过/正在运行投资理财类APP

近期安装过/正在运行视频会议类APP

interdiction

当前设备上存在阻碍用户接听电话的行为。命中一个或多个下面的风险因子：

当前已开启呼叫转移

当前已开启飞行模式

当前处于在电话语音中

control

当前设备上是否存在被操控的风险。命中一个或多个下面的风险因子：

当前启用了共享屏幕

level值含义如下

level值

含义

low

当前风险标签对应的风险等级为低

medium

当前风险标签对应的风险等级为中

high

当前风险标签对应的风险等级为高

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/BusinessRiskIntelligentDetection（业务风险检测） (devicesecurity-arktsapi-errcode-brid).md)**。**

错误码ID

错误信息

401

Invalid parameters.

1012500001

Internal error.

1012500002

The network is unreachable.

1012500003

Access cloud server fail.

1012500004

Verify cloud capability fail.

**示例：**

```ets
import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "[BusinessRiskIntelligentDetectionModel]";

let rand = cryptoFramework.createRandom();
let len = 48;
let randData = rand.generateRandomSync(len);
let params = {
  nonce: randData.data,
  algorithm: businessRiskIntelligentDetection.SigningAlgorithm.ES256
} as businessRiskIntelligentDetection.FraudDetectionRequest;
try {
  hilog.info(0x0000, TAG, 'Detect fraud risk begin.');
  businessRiskIntelligentDetection.detectFraudRisk(params).then((result: string) => {
    hilog.info(0x0000, TAG, 'Detect fraud risk success: %{public}s', result);
  }).catch((error: Error) => {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, TAG, 'Detect fraud risk failed: %{public}d %{public}s', e.code, e.message);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, TAG, 'Detect fraud risk failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### detectSimulatedClickRisk

detectSimulatedClickRisk(params: [SimulatedClickDetectionRequest](#section157731058201714)): Promise<string>

获取自动化点击、设备墙等作弊行为检测结果。使用Promise异步回调。

**系统能力：**SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

params

[SimulatedClickDetectionRequest](#section157731058201714)

是

请求参数

**返回值：**

类型

说明

Promise<string>

Promise对象，返回模拟点击检测结果。

JSON字段如下：

```ets
{
    "timestampMs": 9860437986543,
    "version": 1,
    "riskDecision": "fake",
    "tags": ["AbnormalTap"]
}
```

 说明：

- timestampMs：发起请求时生成的时间戳。
- riskDecision：风险检测结果。
- version：检测结果消息格式的版本。默认值为1，当前只支持1。
- tags：模拟点击关键特征。如果tags列表为空，表示未发现关键特征。如果tags列表不为空，表示发现关键特征。

tags值

含义

AbnormalDeviceIntegrity

设备完整性遭到破坏。

AbnormalDeviceBehavior

设备行为异常，例如，设备连接状态、传感器状态等行为异常。

AbnormalTap

存在异常点击行为，例如，点击事件注入，自动化点击等。

riskDecision值

含义

fake

当前设备存在作弊风险行为。存在自动化操控行为或设备墙作弊行为，详情见tags。

likelyReal

当前操作设备的是真人用户的可能性较高。

unknown

未知。未检测到明显特征，无法识别。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/BusinessRiskIntelligentDetection（业务风险检测） (devicesecurity-arktsapi-errcode-brid).md)**。**

错误码ID

错误信息

1012500001

Internal error.

1012500002

The network is unreachable.

1012500003

Access cloud server fail.

1012500004

Verify cloud capability fail.

1012500005

The interface access frequency exceeds the limit.

1012500006

Internal timeout.

1012500007

Invalid parameters.

**示例：**

```ets
import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "BusinessRiskIntelligentDetectionJsTest";

let params = {
    version: 1
} as businessRiskIntelligentDetection.SimulatedClickDetectionRequest;
try {
    hilog.info(0x0000, TAG, 'Detect simulated click risk begin.');
    businessRiskIntelligentDetection.detectSimulatedClickRisk(params).then((result: string) => {
        hilog.info(0x0000, TAG, 'Detect simulated click risk success: %{public}s', result);
    }).catch((error: Error) => {
        let e: BusinessError = error as BusinessError;
        hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
    });
} catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### detectSimulatedClickRiskEnhanced

detectSimulatedClickRiskEnhanced(params: SimulatedClickDetectionEnhancedRequest): Promise<string>

获取自动化点击、设备墙等作弊行为的增强检测结果。使用Promise异步回调。

**系统能力：**SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：**6.0.2(22)

**参数**：

参数名

类型

必填

说明

params

[SimulatedClickDetectionEnhancedRequest](#section97791919183510)

是

请求参数

**返回值：**

类型

说明

Promise<string>

Promise对象，返回模拟点击增强检测结果，一个JSON Web Signature格式的字符串，使用Base64URL编码，如果发生异常或错误，则返回错误码。

JWS的Header字段如下：

```ets
{
    "alg": "ES256",
    "x5c": ["",""],
    "nonce": "R2Rra24fVm5xa2Mg",
    "appId": "xxxxxxxxx"
}
```

 说明：

"alg"：数字签名算法，ES256表示为SHA256withECDSA。

"x5c"：华为签名服务器对JWS签名的证书链，x5c[0]为给JWS签名的证书，x5c[1]为签名证书链二级CA。

"nonce"：请求参数SimulatedClickDetectionEnhancedRequest中传入的nonce值的Base64编码。

"appId"：您在[华为开发者联盟](https://developer.huawei.com/consumer/cn)网站上申请的APP ID。

JWS的Payload字段如下：

```ets
{
    "timestampMs": 9860437986543,
    "version": 1,
    "riskDecision": "fake",
    "tags": ["AbnormalTap"]
}
```

 说明：

- timestampMs：华为签名服务器生成的时间戳。
- riskDecision：风险检测结果。
- version：检测结果消息格式的版本。默认值为1，当前只支持1。
- tags：模拟点击关键特征。如果tags列表为空，表示未发现关键特征。如果tags列表不为空，表示发现关键特征。

tags值

含义

AbnormalDeviceIntegrity

设备完整性遭到破坏。

AbnormalDeviceBehavior

设备行为异常，例如，设备连接状态、传感器状态等行为异常。

AbnormalTap

存在异常点击行为，例如，点击事件注入，自动化点击等。

riskDecision值

含义

fake

当前设备存在作弊风险行为。存在自动化操控行为或设备墙作弊行为，详情见tags。

likelyReal

当前操作设备的是真人用户的可能性较高。

unknown

未知。未检测到明显特征，无法识别。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/BusinessRiskIntelligentDetection（业务风险检测） (devicesecurity-arktsapi-errcode-brid).md)**。**

错误码ID

错误信息

1012500001

Internal error

1012500002

The network is unreachable.

1012500003

Access cloud server fail.

1012500005

The interface access frequency exceeds the limit.

1012500006

Internal timeout.

1012500007

Invalid parameters.

**示例：**

```ets
import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import {cryptoFramework} from '@kit.CryptoArchitectureKit'

const TAG = "BusinessRiskIntelligentDetectionJsTest";

let nonceLength = 48;
let nonceBlob = cryptoFramework.createRandom().generateRandomSync(nonceLength);
let params = {
    version: 1,
    nonce: nonceBlob.data,
    algorithm: businessRiskIntelligentDetection.SigningAlgorithm.ES256
} as businessRiskIntelligentDetection.SimulatedClickDetectionEnhancedRequest;
try {
    hilog.info(0x0000, TAG, 'Detect simulated click risk enhanced begin.');
    businessRiskIntelligentDetection.detectSimulatedClickRiskEnhanced(params).then((result: string) => {
        hilog.info(0x0000, TAG, 'Detect simulated click risk enhanced success: %{public}s', result);
    }).catch((error: Error) => {
        let e: BusinessError = error as BusinessError;
        hilog.error(0x0000, TAG, 'Detect simulated click risk enhanced failed: %{public}d %{public}s', e.code, e.message);
    });
} catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, TAG, 'Detect simulated click risk enhanced failed: %{public}d %{public}s', e.code, e.message);
}
```