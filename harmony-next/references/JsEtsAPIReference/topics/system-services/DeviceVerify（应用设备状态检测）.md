# DeviceVerify（应用设备状态检测）

本模块提供应用设备状态检测能力，对应用在某台设备上的使用状态进行管理和检测，用于判断应用是否在该设备上首次安装，或在该设备上用户是否已获取了优惠券等的状态检测，以支撑业务进行新用户营销活动。

**起始版本: **5.0.0(12)

#### 导入模块

```ets
import { deviceCertificate } from '@kit.DeviceSecurityKit';
```

#### getDeviceToken

getDeviceToken(): Promise<string>

获取本设备的DeviceToken。使用Promise异步回调。

**元服务API：**从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Security.DeviceCertificate

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<string>

Promise对象，返回本设备的DeviceToken。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)**。**

错误码ID

错误信息

[201](DeviceVerify（应用设备状态检测）.md#section1196513239128)

has no permission.

[1003300005](DeviceVerify（应用设备状态检测）.md#section4523135612196)

internal error.

[1003300006](DeviceVerify（应用设备状态检测）.md#section179661348180)

access cloud server fail.

**示例：**

```ets
import { deviceCertificate } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "DeviceCertificateJsTest";

// 请求deviceToken，并处理结果
try {
  deviceCertificate.getDeviceToken().then((token) => {
      hilog.info(0x0000, TAG, 'Succeeded in executing getDeviceToken');
      // 开发者处理deviceToken
  }).catch((err: BusinessError) => {
      hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', error.code, error.message);
}
```