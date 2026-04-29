# Interface (MediaKeySession)

支持媒体密钥管理。在调用MediaKeySession方法之前，必须使用[createMediaKeySession](Interface (MediaKeySystem).md#ZH-CN_TOPIC_0000002553201917__createmediakeysession)获取一个MediaKeySession实例。


本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { drm } from '@kit.DrmKit';
```

#### generateMediaKeyRequest

generateMediaKeyRequest(mimeType: string, initData: Uint8Array, mediaKeyType: number, options?: OptionsData[]): Promise<MediaKeyRequest>

生成媒体密钥请求。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 媒体类型，DRM解决方案名称，可通过[isMediaKeySystemSupported](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529285815__drmismediakeysystemsupported-1)查询。 |
| initData | Uint8Array | 是 | 初始数据。 |
| mediaKeyType | number | 是 | 媒体密钥类型。0表示在线，1表示离线。 |
| options | OptionsData[] | 否 | 可选数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MediaKeyRequest> | Promise对象，媒体密钥请求。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码]([DRM错误码](../../errors/DRM错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
// pssh数据为版权保护系统描述头，封装在加密码流中，mp4文件中位于pssh box、dash码流中位于mpd及mp4的pssh box、hls+ts的码流位于m3u8及每个ts片段中，请按实际值传入。
let uint8pssh = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
mediaKeySession.generateMediaKeyRequest("video/avc", uint8pssh, drm.MediaKeyType.MEDIA_KEY_TYPE_ONLINE).then((mediaKeyRequest: drm.MediaKeyRequest) =>{
  console.info('generateMediaKeyRequest' + mediaKeyRequest);
}).catch((err: BusinessError) => {
  console.error(`generateMediaKeyRequest: ERROR: ${err}`);
});
```

#### processMediaKeyResponse

processMediaKeyResponse(response: Uint8Array): Promise<Uint8Array>

处理媒体密钥响应。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | Uint8Array | 是 | 媒体密钥响应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，媒体密钥标识。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
// mediaKeyResponse是从DRM服务获取的媒体密钥响应，按实际值填入。
let mediaKeyResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
mediaKeySession.processMediaKeyResponse(mediaKeyResponse).then((mediaKeyId: Uint8Array) => {
  console.info('processMediaKeyResponse:' + mediaKeyId);
}).catch((err: BusinessError) => {
  console.error(`processMediaKeyResponse: ERROR: ${err}`);
});
```

#### checkMediaKeyStatus

 checkMediaKeyStatus(): MediaKeyStatus[]

检查当前媒体密钥状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| MediaKeyStatus[] | 当前媒体密钥状态值。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
try {
  let keyStatus: drm.MediaKeyStatus[] =  mediaKeySession.checkMediaKeyStatus();
} catch (err) {
  let error = err as BusinessError;
  console.error(`checkMediaKeyStatus ERROR: ${error}`);
}
```

#### clearMediaKeys

clearMediaKeys(): void

清除当前媒体密钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
// mediaKeyResponse是从DRM服务获取的媒体密钥响应，按实际值填入。
let mediaKeyResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
mediaKeySession.processMediaKeyResponse(mediaKeyResponse).then((mediaKeyId: Uint8Array) => {
  console.info('processMediaKeyResponse:' + mediaKeyId);
}).catch((err: BusinessError) => {
  console.error(`processMediaKeyResponse: ERROR: ${err}`);
});
try {
  mediaKeySession.clearMediaKeys();
} catch (err) {
  let error = err as BusinessError;
  console.error(`clearMediaKeys ERROR: ${error}`);
}
```

#### generateOfflineReleaseRequest

generateOfflineReleaseRequest(mediaKeyId: Uint8Array): Promise<Uint8Array>

生成离线媒体密钥释放请求。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | 离线媒体密钥标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，设备上的DRM解决方案支持离线媒体密钥释放处理，则返回离线媒体密钥释放请求。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
// mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际值传入。
let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
mediaKeySession.generateOfflineReleaseRequest(mediaKeyId).then((offlineReleaseRequest: Uint8Array) => {
  console.info('generateOfflineReleaseRequest:' + offlineReleaseRequest);
}).catch((err: BusinessError) => {
  console.error(`generateOfflineReleaseRequest: ERROR: ${err}`);
});
```

#### processOfflineReleaseResponse

processOfflineReleaseResponse(mediaKeyId: Uint8Array, response: Uint8Array): Promise<void>

处理离线媒体密钥释放响应。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | 离线媒体密钥标识。 |
| response | Uint8Array | 是 | 离线媒体密钥释放响应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，设备上的DRM解决方案支持离线媒体密钥释放处理，则返回。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
// mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际长度申请内存。
let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
mediaKeySession.generateOfflineReleaseRequest(mediaKeyId).then((offlineReleaseRequest: Uint8Array) => {
  console.info('generateOfflineReleaseRequest:' + offlineReleaseRequest);
}).catch((err: BusinessError) => {
  console.error(`generateOfflineReleaseRequest: ERROR: ${err}`);
});
// offlineReleaseResponse是从DRM服务获取的离线媒体密钥释放响应，请按实际长度申请内存。
let offlineReleaseResponse = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
mediaKeySession.processOfflineReleaseResponse(mediaKeyId, offlineReleaseResponse).then(() => {
  console.info('processOfflineReleaseResponse');
}).catch((err: BusinessError) => {
  console.error(`processOfflineReleaseResponse: ERROR: ${err}`);
});
```

#### restoreOfflineMediaKeys

restoreOfflineMediaKeys(mediaKeyId: Uint8Array): Promise<void>

恢复离线媒体密钥。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | 离线媒体密钥标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
// mediaKeyId是processMediaKeyResponse或getOfflineMediaKeyIds接口返回的媒体密钥标识，请按实际数据传入。
let mediaKeyId = new Uint8Array([0x00, 0x00, 0x00, 0x00]);
mediaKeySession.restoreOfflineMediaKeys(mediaKeyId).then(() => {
  console.info("restoreOfflineMediaKeys");
}).catch((err: BusinessError) => {
  console.error(`restoreOfflineMediaKeys: ERROR: ${err}`);
});
```

#### get[ContentProtectionLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002529285817__contentprotectionlevel)

get[ContentProtectionLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002529285817__contentprotectionlevel)(): ContentProtectionLevel

获取当前会话的内容保护级别。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContentProtectionLevel](../enums/Enums.md#ZH-CN_TOPIC_0000002529285817__contentprotectionlevel) | 返回当前会话内容保护级别。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
try {
  let contentProtectionLevel: drm.ContentProtectionLevel = mediaKeySession.getContentProtectionLevel();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getContentProtectionLevel ERROR: ${error}`);
}
```

#### requireSecureDecoderModule

requireSecureDecoderModule(mimeType: string): boolean

是否需要安全解码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 媒体类型，支持的媒体类型取决于DRM解决方案，可通过[isMediaKeySystemSupported](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529285815__drmismediakeysystemsupported-1)查询。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否需要安全解码，true表示需要安全解码，false表示不需要安全解码。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
try {
  let status: boolean = mediaKeySession.requireSecureDecoderModule("video/avc");
} catch (err) {
  let error = err as BusinessError;
  console.error(`requireSecureDecoderModule ERROR: ${error}`);
}
```

#### on('keyRequired')

on(type: 'keyRequired', callback: (eventInfo: EventInfo) => void): void

监听密钥请求事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定为'keyRequired'，当播放DRM节目需要获取媒体密钥时触发。 |
| callback | (eventInfo: EventInfo) => void | 是 | 回调函数，返回事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.on('keyRequired', (eventInfo: drm.EventInfo) => {
  console.info('keyRequired ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
});
```

#### off('keyRequired')

off(type: 'keyRequired', callback?: (eventInfo: EventInfo) => void): void

注销密钥请求事件监听。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keyRequired'。 |
| callback | (eventInfo: EventInfo) => void | 否 | 回调函数，返回事件信息。可选。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.off('keyRequired');
```

#### on('keyExpired')

on(type: 'keyExpired', callback: (eventInfo: EventInfo) => void): void

监听密钥过期事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keyExpired'。密钥过期时触发。 |
| callback | (eventInfo: EventInfo) => void | 是 | 回调函数，返回事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.on('keyExpired', (eventInfo: drm.EventInfo) => {
  console.info('keyExpired ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
});
```

#### off('keyExpired')

off(type: 'keyExpired', callback?: (eventInfo: EventInfo) => void): void

注销密钥过期事件监听。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keyExpired'。 |
| callback | (eventInfo: EventInfo) => void | 否 | 回调函数，返回事件信息。可选。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.off('keyExpired');
```

#### on('vendorDefined')

on(type: 'vendorDefined', callback: (eventInfo: EventInfo) => void): void

监听DRM解决方案自定义事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'vendorDefined'。自定义事件发生时触发。 |
| callback | (eventInfo: EventInfo) => void | 是 | 回调函数，返回事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.on('vendorDefined', (eventInfo: drm.EventInfo) => {
  console.info('vendorDefined ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
});
```

#### off('vendorDefined')

off(type: 'vendorDefined', callback?: (eventInfo: EventInfo) => void): void

注销DRM解决方案自定义事件监听。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'vendorDefined'。 |
| callback | (eventInfo: EventInfo) => void | 否 | 回调函数，返回事件信息。可选。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.off('vendorDefined');
```

#### on('expirationUpdate')

on(type: 'expirationUpdate', callback: (eventInfo: EventInfo) => void): void

监听密钥过期更新事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'expirationUpdate'。密钥过期更新时触发。 |
| callback | (eventInfo: EventInfo) => void | 是 | 回调函数，返回事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.on('expirationUpdate', (eventInfo: drm.EventInfo) => {
  console.info('expirationUpdate ' + 'extra: ' + eventInfo.extraInfo + 'data: ' + eventInfo.info);
});
```

#### off('expirationUpdate')

off(type: 'expirationUpdate', callback?: (eventInfo: EventInfo) => void): void

注销过期更新事件监听。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'expirationUpdate'。 |
| callback | (eventInfo: EventInfo) => void | 否 | 回调函数，返回事件信息。可选。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.off('expirationUpdate');
```

#### on('keysChange')

on(type: 'keysChange', callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void

监听密钥变化事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keysChange'。密钥变化时触发。 |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void | 是 | 回调函数，返回事件信息，包含密钥标识和密钥状态描述的列表及密钥是否可用。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.on('keysChange', (keyInfo: drm.KeysInfo[], newKeyAvailable: boolean) => {
  for (let i = 0; i < keyInfo.length; i++) {
    console.info('keysChange' + 'keyId:' + keyInfo[i].keyId + ' data:' + keyInfo[i].value);
  }
});
```

#### off('keysChange')

off(type: 'keysChange', callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void

注销密钥变化事件监听。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，固定为'keysChange'。 |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void | 否 | 回调函数，返回事件信息，包含密钥标识和密钥状态描述的列表及密钥是否可用。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
mediaKeySession.off('keysChange');
```

#### destroy

destroy(): void

销毁MediaKeySession实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](DRM错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
let mediaKeySession: drm.MediaKeySession = mediaKeySystem.createMediaKeySession();
try {
  mediaKeySession.destroy();
} catch (err) {
  let error = err as BusinessError;
  console.error(`mediaKeySession destroy ERROR: ${error}`);
}
```