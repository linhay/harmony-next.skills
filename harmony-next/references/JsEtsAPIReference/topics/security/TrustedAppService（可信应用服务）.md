# TrustedAppService（可信应用服务）

本模块提供应用数据的安全证明服务，支持创建证明密钥、销毁证明密钥、初始化证明会话、结束证明会话和获取安全地理位置，能够为安全摄像头和安全地理位置功能提供安全证明能力，确保图像或位置数据未被篡改。

起始版本： 5.0.0(12)

**导入模块**

```ets
import { trustedAppService } from '@kit.DeviceSecurityKit';
```

**createAttestKey**

createAttestKey(options: AttestOptions): Promise<void>

创建证明密钥，在证明密钥不存在或者不可用的条件下调用，使用Promise异步回调。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | AttestOptions | 是 | 生成证明密钥的参数，需要指定密钥类型和密钥大小。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAppService（可信应用服务）.md) 。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 401 | argument is invalid. |
| 1011500001 | algorithm param is invalid. |
| 1011500002 | algorithm param is missing. |
| 1011500003 | create attestation key failed. |
| 1011500004 | create anonymous certificate failed. |
| 1011500005 | operating file failed. |
| 1011500006 | IPC communication failed. |

示例：

```ets
import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let properties: Array<trustedAppService.AttestParam> = [
  {
    tag: trustedAppService.AttestTag.ATTEST_TAG_ALGORITHM,
    value: trustedAppService.AttestKeyAlg.ATTEST_ALG_ECC
  },
  {
    tag: trustedAppService.AttestTag.ATTEST_TAG_KEY_SIZE,
    value: trustedAppService.AttestKeySize.ATTEST_ECC_KEY_SIZE_256
  }
];
let options: trustedAppService.AttestOptions = {
  properties: properties,
};
await trustedAppService.createAttestKey(options)
  .then(
    (): void => {
      hilog.info(0x0000, 'testTag', 'Succeeded in creating attest key');
    }
  ).catch(
    (error: BusinessError): void => {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', `Failed to create attest key, code:${err.code}, message:${err.message}`);
    });
```

**AttestOptions**

[createAttestKey](#ZH-CN_TOPIC_0000002553201329__createattestkey)接口的请求参数。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| properties | Array<AttestParam> | 否 | 否 | 开发者应用传入的用于生成证明密钥的配置信息。 |

**AttestParam**

[AttestOptions](#ZH-CN_TOPIC_0000002553201329__attestoptions)配置信息的内容条目。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tag | AttestTag | 否 | 否 | 开发者应用传入的标签，用于生成证明密钥的配置信息。 |
| value | boolean|number|bigint|Uint8Array | 否 | 否 | 开发者应用传入的标签对应的值，用于生成证明密钥的配置信息。 boolean： 预留参数，暂未使用。 number： 1）tag为ATTEST_TAG_ALGORITHM，其值为AttestKeyAlg类型。 2）tag为ATTEST_TAG_KEY_SIZE，其值为AttestKeySize类型。 3）tag为ATTEST_TAG_DEVICE_TYPE，其值为AttestType类型。 bigint： tag为ATTEST_TAG_DEVICE_ID，其值为设备ID，取值范围int64类型的随机值。 Uint8Array： 预留参数，暂未使用。 |

**AttestTag**

配置信息标签类型，使用[AttestTagType](#ZH-CN_TOPIC_0000002553201329__attesttagtype)扩展定义。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATTEST_TAG_INVALID | AttestTagType.ATTEST_TAG_TYPE_INVALID|0 | 不合法标签。 |
| ATTEST_TAG_ALGORITHM | AttestTagType.ATTEST_TAG_TYPE_UINT|1 | 算法标签。 |
| ATTEST_TAG_KEY_SIZE | AttestTagType.ATTEST_TAG_TYPE_UINT|2 | 密钥大小标签。 |
| ATTEST_TAG_DEVICE_TYPE | AttestTagType.ATTEST_TAG_TYPE_UINT|3 | 设备类型标签。 |
| ATTEST_TAG_DEVICE_ID | AttestTagType.ATTEST_TAG_TYPE_UINT|4 | 设备序列号标签。 |

**AttestTagType**

标签类型定义，用于区分数据类型。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATTEST_TAG_TYPE_INVALID | 0<<28 | 不合法标签类型。 |
| ATTEST_TAG_TYPE_INT | 1<<28 | INT类型。 |
| ATTEST_TAG_TYPE_UINT | 2<<28 | UINT类型。 |
| ATTEST_TAG_TYPE_ULONG | 3<<28 | ULONG类型。 |
| ATTEST_TAG_TYPE_BOOL | 4<<28 | BOOL类型。 |
| ATTEST_TAG_TYPE_BYTES | 5<<28 | BYTES类型。 |

**AttestKeyAlg**

证明密钥算法类型。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATTEST_ALG_ECC | 1 | ECC算法类型。 |

**AttestKeySize**

证明密钥长度。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATTEST_ECC_KEY_SIZE_256 | 256 | 证明密钥长度，256位。 |
| ATTEST_ECC_KEY_SIZE_384 | 384 | 证明密钥长度，384位。 |

**destroyAttestKey**

destroyAttestKey(): Promise<void>

销毁证明密钥，使用Promise异步回调。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAppService（可信应用服务）.md) 。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 1011500005 | operating file failed. |
| 1011500006 | IPC communication failed. |
| 1011500007 | item not found. |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

示例：

```ets
import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

await trustedAppService.destroyAttestKey().then(
  (): void => {
    hilog.info(0x0000, 'testTag', 'Succeeded in destroying attest key');
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', `Failed to destroy attest key, code:${err.code}, message:${err.message}`);
  }
);
```

**initializeAttestContext**

initializeAttestContext(userData: string, options: AttestOptions): Promise<AttestReturnResult>

初始化证明会话，在创建证明密钥成功后使用，使用Promise异步回调。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userData | string | 是 | 打开证明会话的参数，传入的用户数据，长度在16到127字节之间。 |
| options | AttestOptions | 是 | 打开证明会话的参数，需要指定设备类型和设备ID。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AttestReturnResult> | 生成的匿名证书链。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAppService（可信应用服务）.md) 。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 401 | argument is invalid. |
| 1011500002 | param is missing. |
| 1011500005 | operating file failed. |
| 1011500006 | IPC communication failed. |
| 1011500007 | item not found. |
| 1011500008 | anonymous certificate verify failed. |
| 1011500009 | anonymous certificate has expired. |
| 1011500010 | get attestation key failed. |
| 1011500011 | initialize secure camera failed. |

**AttestType**

证明会话类型。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATTEST_TYPE_LOCATION | 1 | 安全地理位置类型。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_TYPE_CAMERA | 2 | 安全摄像头类型。 |
| ATTEST_TYPE_SECIMAGE_PROCESS | 3 | 安全图像处理类型。起始版本：5.1.0(18)。 |

**AttestReturnResult**

[initializeAttestContext](#ZH-CN_TOPIC_0000002553201329__initializeattestcontext)接口的返回值。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certChains | Array<string> | 否 | 否 | 打开证明会话成功之后返回的匿名证书链 |

示例：

```ets
import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// device_id 需要指定为 Bigint类型
let device_id_tt = 12581;
// userdata的长度需要超过16个Bytes，最大长度为127 Bytes
let user_data = "test_user_data_0000"
let properties2: Array<trustedAppService.AttestParam> = [
  {
    tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
    value: trustedAppService.AttestType.ATTEST_TYPE_LOCATION
  },
  {
    tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_ID,
    value: BigInt(device_id_tt)
  },
];
let options2: trustedAppService.AttestOptions = {
  properties: properties2,
};
await trustedAppService.initializeAttestContext(user_data, options2).then(
  (returnResult: trustedAppService.AttestReturnResult): void => {
    let chains = returnResult.certChains as Array<string>;
    for (const item of chains) {
      hilog.info(0x0000, 'testTag', 'item: ' + item);
    };
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', `Failed to initialize attest context, code:${err.code}, message:${err.message}`);
  }
);
```

**AttestExceptionErrCode**

可信应用服务中创建证明密钥、销毁证明密钥、初始化证明会话、结束证明会话、获取当前安全位置等接口的错误码。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATTEST_ERROR_NO_PERMISSION | 201 | 权限校验失败。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_ILLEGAL_ARGUMENT | 401 | 参数检查失败。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_INVALID_ALG_ARGUMENT | 1011500001 | 无效的算法参数。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_MISSING_ARGUMENT | 1011500002 | 参数传入不足。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_KEY_GENERATOR_FAILED | 1011500003 | 密钥生成失败。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_CERTS_CREATION_FAILED | 1011500004 | 证书创建失败。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_FILE_OPERATION_FAILED | 1011500005 | 文件操作失败。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_COMMUNICATION_FAILED | 1011500006 | IPC通信失败。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_ITEM_NOT_FOUND | 1011500007 | 密钥不存在。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_CERTS_VERIFICATION_FAILED | 1011500008 | 证书校验失败。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_CERTS_EXPIRED | 1011500009 | 证书已过期。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_KEY_NOT_MATCHED | 1011500010 | 密钥不匹配。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_SECURE_CAMERA_INITIALIZATION_FAILED | 1011500011 | 安全相机初始化失败。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_CONTEXT_BAD_STATE | 1011500012 | 证明会话上下文异常。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_KEY_EXPIRED | 1011500013 | 密钥已过期。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_LOCATION_SERVICE_UNAVAILABLE | 1011500014 | 位置服务不可用。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_LOCATION_SWITCH_OFF | 1011500015 | 位置信息开关关闭。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_LOCATION_FAILED | 1011500016 | 位置信息获取失败。 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST_ERROR_SIGNATURE_VERIFICATION_FAILED | 1011500017 | 签名验签失败。 起始版本：5.1.0(18)。 |
| ATTEST_ERROR_SECIMAGE_PROCESS_FAILED | 1011500018 | 安全图像处理失败。 起始版本：5.1.0(18)。 |

**finalizeAttestContext**

finalizeAttestContext(options: AttestOptions): Promise<void>

结束证明会话，在结束安全证明服务后调用，使用Promise异步回调。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | AttestOptions | 是 | 关闭证明会话的参数，需要指定设备类型。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAppService（可信应用服务）.md) 。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 401 | argument is invalid. |
| 1011500002 | param is missing. |
| 1011500006 | IPC communication failed. |
| 1011500007 | item not found. |

示例：

```ets
import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let properties: Array<trustedAppService.AttestParam> = [
  {
    tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
    value: trustedAppService.AttestType.ATTEST_TYPE_CAMERA
  }
];
let options: trustedAppService.AttestOptions = {
  properties: properties,
};
await trustedAppService.finalizeAttestContext(options).then(
  (): void => {
    hilog.info(0x0000, 'testTag', 'Succeeded in finalizing attest context');
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', `Failed to finalize attest context, code:${err.code}, message:${err.message}`);
  }
);
```

**getCurrentSecureLocation**

getCurrentSecureLocation(timeout : number, priority: LocatingPriority): Promise<SecureLocation>

获取当前安全位置，使用Promise异步回调。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Location

需要权限：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 单次位置请求的超时时间，单位是毫秒（milliseconds），最小为1000毫秒。取值范围为大于等于1000。 |
| priority | LocatingPriority | 是 | 获取安全地理位置的优先级策略。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<SecureLocation> | 获取的安全位置 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAppService（可信应用服务）.md) 。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | has no permission. |
| 401 | argument is invalid. |
| 1011500012 | attestation context not initialized. |
| 1011500013 | attestation key has expired. |
| 1011500014 | location service is unavailable. |
| 1011500015 | The location switch is off. |
| 1011500016 | Failed to obtain the secure geographical location. |

**LocatingPriority**

获取安全地理位置的优先级策略。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Location

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRIORITY_ACCURACY | 0 | 精度优先，保证获取最高精度。 |
| PRIORITY_LOCATING_SPEED | 1 | 速度优先，保证位置获取速度。 |

**SecureLocation**

获取的安全地理位置。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Location

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| originalLocation | Location | 否 | 否 | 地理位置信息。 |
| userData | String | 否 | 否 | 用户数据，长度在16到127字节之间。 |
| signature | String | 否 | 否 | 签名结果。 当证明密钥长度为256位时，signature长度为96字节； 当证明密钥长度为384位时，signature长度为136或者140字节。 |

**Location**

获取的安全地理位置信息。

元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.TrustedAppService.Location

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 纬度，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。 |
| longitude | number | 否 | 否 | 经度，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。 |
| altitude | number | 否 | 否 | 高度，单位米。 |
| accuracy | number | 否 | 否 | 精度，单位米，取值大于等于0。 |
| timestamp | number | 否 | 否 | 时间戳，单位毫秒，取值大于等于0。 |

示例：

```ets
import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const secureLocation = await trustedAppService.getCurrentSecureLocation(3000, trustedAppService.LocatingPriority.PRIORITY_LOCATING_SPEED);
  hilog.info(0x0000, 'testTag', 'Succeeded in getting secure location, result = ${JSON.stringify(secureLocation)}');
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to get secure location, code:${err.code}, message:${err.message}`);
}
```

**procSecImageTransform**

procSecImageTransform(srcSecImage: ArrayBuffer, procParams: SecImageProcParamsArray): Promise<SecImageBuffer>

处理安全图像压缩、裁剪操作，使用Promise异步回调。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcSecImage | ArrayBuffer | 是 | 安全相机返回签名后的安全图像。 |
| procParams | SecImageProcParamsArray | 是 | 安全图像压缩、裁剪处理的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<SecImageBuffer> | 返回压缩、裁剪处理后签名的安全图像 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAppService（可信应用服务）.md) 。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1011500011 | secure image processing is not supported. |
| 1011500012 | attestation context not initialized. |
| 1011500013 | attestation key has expired. |
| 1011500017 | signature verification failed. |
| 1011500018 | secure image process failed. |

**SecImageProcParamsArray**

[procSecImageTransform](#ZH-CN_TOPIC_0000002553201329__procsecimagetransform)接口的请求参数。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| properties | Array<SecImageProcParams> | 否 | 否 | 开发者应用传入的用于安全图像压缩、裁剪处理的配置信息。 |

**SecImageProcParams**

[SecImageProcParamsArray](#ZH-CN_TOPIC_0000002553201329__secimageprocparamsarray)配置信息的内容条目。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tag | SecImageProcTag | 否 | 否 | 开发者应用传入的标签，用于安全图像压缩、裁剪处理的配置信息。 |
| value | number | CropRegion | 否 | 否 | 开发者应用传入的标签对应的值，用于安全图像压缩、裁剪处理的配置信息。 number： 1）tag为SECIMAGE_TAG_SRC_IMAGE_FORMAT或者 SECIMAGE_TAG_DEST_IMAGE_FORMAT ，其值为SecImageProcParamsArray类型； 2）tag为SECIMAGE_TAG_PROC_OPERATION，其值为SecImageProcOperation类型； 3）tag为SECIMAGE_TAG_COMPRESSION_QUALITY，其值为1到100之间； CropRegion： tag为SECIMAGE_TAG_CROP_REGION，其值为CropRegion类型。 |

**SecImageProcTag**

安全图像压缩、裁剪处理的配置信息标签类型，使用[AttestTagType](#ZH-CN_TOPIC_0000002553201329__attesttagtype)扩展定义。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SECIMAGE_TAG_INVALID | AttestTagType.ATTEST_TAG_TYPE_INVALID|0 | 不合法标签。 |
| SECIMAGE_TAG_SRC_IMAGE_FORMAT | AttestTagType.ATTEST_TAG_TYPE_UINT|1 | 原始安全图像的格式。 |
| SECIMAGE_TAG_DEST_IMAGE_FORMAT | AttestTagType.ATTEST_TAG_TYPE_UINT|2 | 压缩、裁剪处理后的安全图像的格式。 |
| SECIMAGE_TAG_PROC_OPERATION | AttestTagType.ATTEST_TAG_TYPE_UINT|3 | 安全图像的处理命令，支持：压缩命令、裁剪命令、压缩并裁剪命令。 |
| SECIMAGE_TAG_COMPRESSION_QUALITY | AttestTagType.ATTEST_TAG_TYPE_UINT|4 | 安全图像压缩处理的压缩质量。 |
| SECIMAGE_TAG_CROP_REGION | AttestTagType.ATTEST_TAG_TYPE_UINT|5 | 安全图像裁剪处理的裁剪区域。 |

**SecImageProcOperation**

安全图像的处理命令。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SECIMAGE_COMPRESSION | 0 | 安全图像压缩命令。 |
| SECIMAGE_CROPPING | 1 | 安全图像裁剪命令。 |
| SECIMAGE_COMPRESSION_AND_CROPPING | 2 | 安全图像压缩并裁剪命令。 |

**SecImageProcFormat**

安全图像的格式。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SECIMAGE_FORMAT_INVALID | 0 | 无效的安全图像格式。 |
| SECIMAGE_FORMAT_YUV_NV21 | 1 | YUV420 NV21格式的安全图像。输入原始安全图像格式，以及裁剪命令返回的安全图像格式均为SECIMAGE_FORMAT_YUV_NV21。 |
| SECIMAGE_FORMAT_JPEG | 2 | JPEG格式的安全图像。压缩命令、压缩并裁剪命令返回的安全图像格式均为SECIMAGE_FORMAT_JPEG。 |

**CropRegion**

安全图像裁剪处理的裁剪区域。裁剪区域参数作用如下图所示。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 裁剪区域左上角点在水平方向（横向）上相对于整个图像左边界的偏移量，取值范围在 0 到 640 之间的偶数。单位是像素（pixel）。 |
| y | number | 否 | 否 | 裁剪区域左上角点在垂直方向（纵向）上相对于整个图像上边界的偏移量，取值范围在 0 到 480 之间的偶数。单位是像素（pixel）。 |
| width | number | 否 | 否 | 裁剪区域的宽度，即横向的长度，取值范围在 0 到 640 之间的偶数，且需满足 x 与 width 的和不大于 640。单位是像素（pixel）。 |
| height | number | 否 | 否 | 裁剪区域的高度，即纵向的长度，取值范围在 0 到 480 之间的偶数，且需满足 y 与 height 的和不大于 480。单位是像素（pixel）。 |

![image](public_sys-resources/zh-cn_image_0000002553365709.webp)

**SecImageBuffer**

获得压缩、裁剪处理后签名的安全图像。

系统能力： SystemCapability.Security.TrustedAppService.Core

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| secImage | ArrayBuffer | 否 | 否 | 返回压缩、裁剪处理后签名的安全图像。 |

安全图像压缩示例：

```ets
import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const srcSecImageBuffer = new  ArrayBuffer(461844);// 实际使用请替换为Camera Kit获取到的安全图像buffer

let properties: Array<trustedAppService.SecImageProcParams> = [
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
    value: trustedAppService.SecImageProcOperation.SECIMAGE_COMPRESSION,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩、裁剪命令输入的原始图像格式都为：YUV420 NV21 格式
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_JPEG, // 安全图像压缩命令返回的图像格式为：JPEG 格式
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_COMPRESSION_QUALITY,
    value: 90, // 实际使用请替换为业务场景需要的压缩质量
  },
];
let procParams: trustedAppService.SecImageProcParamsArray = {
  properties: properties,
};
await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
  (returnResult: trustedAppService.SecImageBuffer): void => {
    let returnSecImageBuffer = returnResult.secImage;
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', `Failed to process secureImage compression, code:${err.code}, message:${err.message}`);
  }
);
```

安全图像裁剪示例：

```ets
import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const srcSecImageBuffer = new  ArrayBuffer(461844);// 实际使用请替换为Camera Kit获取到的安全图像buffer

let properties: Array<trustedAppService.SecImageProcParams> = [
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
    value: trustedAppService.SecImageProcOperation.SECIMAGE_CROPPING,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩、裁剪命令输入的原始图像格式都为：YUV420 NV21 格式
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩命令返回的图像格式为：JPEG 格式
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_CROP_REGION,
    value: { x : 0, y ：0, width : 320, height : 240 }, // 实际使用请替换为业务场景需要的裁剪区域范围
  },
];
let procParams: trustedAppService.SecImageProcParamsArray = {
  properties: properties,
};
await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
  (returnResult: trustedAppService.SecImageBuffer): void => {
    let returnSecImageBuffer = returnResult.secImage;
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', `Failed to process secureImage cropping, code:${err.code}, message:${err.message}`);
  }
);
```

安全图像压缩并裁剪示例：

```ets
import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const srcSecImageBuffer = new  ArrayBuffer(461844);// 实际使用请替换为Camera Kit获取到的安全图像buffer

let properties: Array<trustedAppService.SecImageProcParams> = [
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
    value: trustedAppService.SecImageProcOperation.SECIMAGE_COMPRESSION_AND_CROPPING,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_JPEG,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_COMPRESSION_QUALITY,
    value: 90, // 实际使用请替换为业务场景需要的压缩质量
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_CROP_REGION,
    value: { x : 0, y ：0, width : 320, height : 240 }, // 实际使用请替换为业务场景需要的裁剪区域范围
  },
];
let procParams: trustedAppService.SecImageProcParamsArray = {
  properties: properties,
};
await trustedAppService.procSecImageTransform(srcSecImageBuffer, options).then(
  (returnResult: trustedAppService.SecImageBuffer): void => {
    let returnSecImageBuffer = returnResult.secImage;
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', `Failed to process secureImage cropping, code:${err.code}, message:${err.message}`);
  }
);
```