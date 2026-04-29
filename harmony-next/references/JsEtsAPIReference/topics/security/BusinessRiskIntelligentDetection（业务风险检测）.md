# BusinessRiskIntelligentDetection（业务风险检测）

- 识别当前设备的涉诈行为风险。

起始版本： 5.0.0(12)

- 提供自动化点击、设备墙等作弊行为检测能力。

起始版本： 6.0.0(20)

**导入模块**

```ets
import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
```

**FraudDetectionRequest**

涉诈剧本检测的请求参数。

系统能力： SystemCapability.Security.BusinessRiskIntelligentDetection

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nonce | Uint8Array | 否 | 否 | 开发者应用传入的一个随机生成的nonce值，用于防重放攻击，在检测结果中会包含该值。nonce值必须为24至80字节之间。 |
| algorithm | SigningAlgorithm | 否 | 否 | 数字签名算法。 |
| version | number | 否 | 是 | 检测结果消息格式的版本，默认值为1，可选1和2，取值为2时检测结果的Tag标签中带有时间属性和风险等级，其中时间属性表示该标签对应线索的最后一次发生时间，风险等级表示该标签对应的风险级别，取值为1时，检测结果Tag标签中不带时间属性和风险等级。 起始版本： 5.1.0(18) |

**SimulatedClickDetectionRequest**

模拟点击检测的请求参数。

系统能力： SystemCapability.Security.BusinessRiskIntelligentDetection

起始版本： 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| version | number | 否 | 是 | 检测结果消息格式的版本，默认值为1，当前只支持1。 |

**SimulatedClickDetectionEnhancedRequest**

模拟点击增强检测的请求参数。

系统能力：SystemCapability.Security.BusinessRiskIntelligentDetection

起始版本： 6.0.2(22)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nonce | Uint8Array | 否 | 否 | 开发者应用传入的一个随机生成的nonce值，用于防重放攻击，在检测结果中会包含该值。nonce值必须为24至80字节之间。 |
| algorithm | SigningAlgorithm | 否 | 否 | 数字签名算法。 |
| version | number | 否 | 是 | 检测结果消息格式的版本，默认值为1，当前版本号只支持1。 |

**SigningAlgorithm**

数字签名算法。

系统能力： SystemCapability.Security.BusinessRiskIntelligentDetection

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ES256 | 0 | SHA256withECDSA。 |

**detectFraudRisk**

detectFraudRisk(params: [FraudDetectionRequest](#ZH-CN_TOPIC_0000002522081368__frauddetectionrequest)): Promise<string>

获取本设备的涉诈行为风险。使用Promise异步回调。

系统能力： SystemCapability.Security.BusinessRiskIntelligentDetection

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | FraudDetectionRequest | 是 | 请求参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回涉诈风险检测结果，一个JSON Web Signature格式的字符串，使用Base64URL编码，如果发生异常或错误，则返回错误码。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](BusinessRiskIntelligentDetection（业务风险检测）.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters. |
| 1012500001 | Internal error. |
| 1012500002 | The network is unreachable. |
| 1012500003 | Access cloud server fail. |
| 1012500004 | Verify cloud capability fail. |

示例：

```ets
import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

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

**detectSimulatedClickRisk**

detectSimulatedClickRisk(params: [SimulatedClickDetectionRequest](#ZH-CN_TOPIC_0000002522081368__simulatedclickdetectionrequest)): Promise<string>

获取自动化点击、设备墙等作弊行为检测结果。使用Promise异步回调。

系统能力： SystemCapability.Security.BusinessRiskIntelligentDetection

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | SimulatedClickDetectionRequest | 是 | 请求参数 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回模拟点击检测结果。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](BusinessRiskIntelligentDetection（业务风险检测）.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1012500001 | Internal error. |
| 1012500002 | The network is unreachable. |
| 1012500003 | Access cloud server fail. |
| 1012500004 | Verify cloud capability fail. |
| 1012500005 | The interface access frequency exceeds the limit. |
| 1012500006 | Internal timeout. |
| 1012500007 | Invalid parameters. |

示例：

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

**detectSimulatedClickRiskEnhanced**

detectSimulatedClickRiskEnhanced(params: SimulatedClickDetectionEnhancedRequest): Promise<string>

获取自动化点击、设备墙等作弊行为的增强检测结果。使用Promise异步回调。

系统能力： SystemCapability.Security.BusinessRiskIntelligentDetection

起始版本： 6.0.2(22)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | SimulatedClickDetectionEnhancedRequest | 是 | 请求参数 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回模拟点击增强检测结果，一个JSON Web Signature格式的字符串，使用Base64URL编码，如果发生异常或错误，则返回错误码。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](BusinessRiskIntelligentDetection（业务风险检测）.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1012500001 | Internal error |
| 1012500002 | The network is unreachable. |
| 1012500003 | Access cloud server fail. |
| 1012500005 | The interface access frequency exceeds the limit. |
| 1012500006 | Internal timeout. |
| 1012500007 | Invalid parameters. |

示例：

```ets
import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

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