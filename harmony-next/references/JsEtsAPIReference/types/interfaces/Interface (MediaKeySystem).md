# Interface (MediaKeySystem)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

支持MediaKeySystem实例管理、设备证书申请与处理、会话创建、离线媒体密钥管理、获取DRM度量记录、设备属性等。在调用MediaKeySystem方法之前，必须使用[createMediaKeySystem](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529285815__drmcreatemediakeysystem)创建一个MediaKeySystem实例。

#### 导入模块

```ets
import { drm } from '@kit.DrmKit';
```

#### setConfigurationString

setConfigurationString(configName: string, value: string): void

设置字符串类型的配置信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明configNamestring是配置属性名，不能为空，属性名参考[PreDefinedConfigName](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285817__predefinedconfigname)，具体支持的属性名由设备上DRM解决方案决定。valuestring是配置属性值。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  mediaKeySystem.setConfigurationString("stringConfigName", "stringConfigValue"); // 确保stringConfigName是可配置的。
} catch (err) {
  let error = err as BusinessError;
  console.error(`setConfigurationString ERROR: ${error}`);
}
```

#### getConfigurationString

getConfigurationString(configName: string): string

获取字符串类型的配置属性值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明configNamestring是配置属性名，不能为空，属性名参考[PreDefinedConfigName](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285817__predefinedconfigname)，具体支持的属性名由设备上DRM解决方案决定。

**返回值：**

类型说明string返回字符串类型的配置属性值。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed, the param's length is zero or too big(exceeds 4096 Bytes).24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  let configValue: string = mediaKeySystem.getConfigurationString("vendor");
} catch (err) {
  let error = err as BusinessError;
  console.error(`getConfigurationString ERROR: ${error}`);
}
```

#### setConfigurationByteArray

setConfigurationByteArray(configName: string, value: Uint8Array): void

设置数组类型的配置信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明configNamestring是配置属性名，不能为空，属性名参考[PreDefinedConfigName](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285817__predefinedconfigname)，具体支持的属性名由设备上DRM解决方案决定。valueUint8Array是数组类型的配置属性值，具体属性值由设备上DRM解决方案决定。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.24700101All unknown errors.24700201Fatal service error, for example, service died.

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
// 按实际需求填写configValue属性值，请按实际值传入。
let configValue: Uint8Array = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
try {
  // 需确认当前DRM解决方案的byteArrayConfigName属性是可配置的。
  mediaKeySystem.setConfigurationByteArray("byteArrayConfigName", configValue);
} catch (err) {
  let error = err as BusinessError;
  console.error(`setConfigurationByteArray ERROR: ${error}`);
}
```

#### getConfigurationByteArray

getConfigurationByteArray(configName: string): Uint8Array

获取数组类型的配置信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明configNamestring是配置属性名，不能为空，属性名参考[PreDefinedConfigName](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285817__predefinedconfigname)，具体支持的属性名由设备上DRM解决方案决定。

**返回值：**

类型说明Uint8Array数组类型的配置属性值。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  let configValue: Uint8Array = mediaKeySystem.getConfigurationByteArray("deviceUniqueId"); // 确保deviceUniqueId属性是存在的。
} catch (err) {
  let error = err as BusinessError;
  console.error(`getConfigurationByteArray ERROR: ${error}`);
}
```

#### getStatistics

getStatistics(): StatisticKeyValue[]

获取性能度量记录。其中包括当前会话数、插件版本信息、每个会话最大三次解密耗时、解密次数和解密失败次数。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

类型说明[StatisticKeyValue[]](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445846__statistickeyvalue)度量记录。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  let statisticKeyValue: drm.StatisticKeyValue[] = mediaKeySystem.getStatistics();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getConfigurationByteArray ERROR: ${error}`);
}
```

#### getMaxContentProtectionLevel

getMaxContentProtectionLevel(): ContentProtectionLevel

获取当前DRM解决方案支持的最大内容保护级别。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

类型说明[ContentProtectionLevel](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285817__contentprotectionlevel)返回设备支持的最大内容保护级别。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  let maxLevel: drm.ContentProtectionLevel = mediaKeySystem.getMaxContentProtectionLevel();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getConfigurationByteArray ERROR: ${error}`);
}
```

#### generateKeySystemRequest

generateKeySystemRequest(): Promise<ProvisionRequest>

生成获取mediaKeySystem设备证书的请求。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

类型说明Promise<[ProvisionRequest](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445846__provisionrequest)>Promise对象，mediaKeySystem设备证书的请求。设备上如果已存在设备证书，会返回失败。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
// 设备上已有设备证书的情况下不需要调用。
mediaKeySystem.generateKeySystemRequest().then((ProvisionRequest: drm.ProvisionRequest) => {
  console.info("generateKeySystemRequest");
}).catch((err: BusinessError) => {
  console.error(`generateKeySystemRequest: ERROR: ${err}`);
});
```

#### processKeySystemResponse

processKeySystemResponse(response: Uint8Array): Promise<void>

处理获得的设备证书请求的响应。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明responseUint8Array是设备证书响应。

**返回值：**

类型说明Promise<void>Promise对象。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
// keySystemResponse是从DRM服务获取的设备证书响应，请按实际值传入；
let keySystemResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
mediaKeySystem.processKeySystemResponse(keySystemResponse).then(() => {
  console.info("processKeySystemResponse");
}).catch((err: BusinessError) => {
  console.error(`processKeySystemResponse: ERROR: ${err}`);
});
```

#### getCertificateStatus

getCertificateStatus():CertificateStatus

获取设备证书状态值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

类型说明[CertificateStatus](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285817__certificatestatus)设备证书状态值。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  let certificateStatus: drm.CertificateStatus = mediaKeySystem.getCertificateStatus();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getCertificateStatus ERROR: ${error}`);
}
```

#### on('keySystemRequired')

on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void

监听设备证书请求事件，获取事件信息。使用callback异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明typestring是事件类型，通过[createMediaKeySystem](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529285815__drmcreatemediakeysystem)成功创建MediaKeySystem实例后可监听，需要设备证书时触发该事件。callback(eventInfo: [EventInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445846__eventinfo)) => void是回调函数，返回事件信息。只要有该事件返回就证明需请求设备证书。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.24700101All unknown errors

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
mediaKeySystem.on('keySystemRequired', (eventInfo: drm.EventInfo) => {
  console.info('keySystemRequired ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
});
```

#### off('keySystemRequired')

off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void

注销设备证书请求事件的监听。使用callback异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明typestring是监听事件类型，通过[createMediaKeySystem](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529285815__drmcreatemediakeysystem)成功创建MediaKeySystem实例后可监听。callback(eventInfo: [EventInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445846__eventinfo)) => void否回调函数，返回事件信息。可选。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.24700101All unknown errors

**示例：**

```ets
import { drm } from '@kit.DrmKit';
let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
mediaKeySystem.off('keySystemRequired');
```

#### createMediaKeySession

createMediaKeySession(level: ContentProtectionLevel): MediaKeySession

创建指定内容保护级别的MediaKeySession实例。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明level[ContentProtectionLevel](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285817__contentprotectionlevel)是内容保护级别。

**返回值：**

类型说明[MediaKeySession](Interface (MediaKeySession).md)MediaKeySession实例。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.The param level exceeds reasonable range, please use value in ContentProtectionLevel.24700101All unknown errors24700104Meet max MediaKeySession num limit24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession(drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
} catch (err) {
  let error = err as BusinessError;
  console.error(`createMediaKeySession ERROR: ${error}`);
}
```

#### createMediaKeySession

createMediaKeySession(): MediaKeySession

创建DRM解决方案默认内容保护级别的MediaKeySession实例。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

类型说明[MediaKeySession](Interface (MediaKeySession).md)MediaKeySession实例。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息24700101All unknown errors24700104Meet max MediaKeySession num limit24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
} catch (err) {
  let error = err as BusinessError;
  console.error(`createMediaKeySession ERROR: ${error}`);
}
```

#### getOfflineMediaKeyIds

getOfflineMediaKeyIds(): Uint8Array[]

获取离线媒体密钥标识列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

类型说明Uint8Array[]离线媒体密钥标识列表。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  let offlineMediaKeyIds: Uint8Array[] = mediaKeySystem.getOfflineMediaKeyIds();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getOfflineMediaKeyIds ERROR: ${error}`);
}
```

#### getOfflineMediaKeyStatus

getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus

获取指定离线媒体密钥标识的媒体密钥的状态值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明mediaKeyIdUint8Array是离线媒体密钥标识。

**返回值：**

类型说明[OfflineMediaKeyStatus](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285817__offlinemediakeystatus)离线媒体密钥状态值。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
// mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际值传入。
let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
try {
  let configValue: drm.OfflineMediaKeyStatus = mediaKeySystem.getOfflineMediaKeyStatus(mediaKeyId);
} catch (err) {
  let error = err as BusinessError;
  console.error(`getOfflineMediaKeyStatus ERROR: ${error}`);
}
```

#### clearOfflineMediaKeys

clearOfflineMediaKeys(mediaKeyId: Uint8Array): void

删除指定媒体密钥标识的离线媒体密钥。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明mediaKeyIdUint8Array是离线媒体密钥标识。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed.Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
// mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际值传入。
let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
try {
  mediaKeySystem.clearOfflineMediaKeys(mediaKeyId);
} catch (err) {
  let error = err as BusinessError;
  console.error(`clearOfflineMediaKeys ERROR: ${error}`);
}
```

#### destroy

destroy(): void

销毁MediaKeySystem实例。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
try {
  mediaKeySystem.destroy();
} catch (err) {
  let error = err as BusinessError;
  console.error(`mediaKeySystem destroy ERROR: ${error}`);
}
```