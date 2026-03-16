[]()[]()

# Functions

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { drm } from '@kit.DrmKit';
```

[]()[]()

#### drm.createMediaKeySystem

createMediaKeySystem(name: string): MediaKeySystem

创建MediaKeySystem实例。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明namestring是DRM解决方案名称，如"com.wiseplay.drm"。

**返回值：**

类型说明[MediaKeySystem](../../types/interfaces/Interface (MediaKeySystem).md)MediaKeySystem实例。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.24700101All unknown errors24700103Meet max MediaKeySystem num limit24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
} catch (err) {
  let error = err as BusinessError;
  console.error(`createMediaKeySystem ERROR: ${error}`);
}
```

[]()[]()

#### drm.isMediaKeySystemSupported

isMediaKeySystemSupported(name: string): boolean

判断设备是否支持指定的DRM解决方案。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明namestring是DRM解决方案名称，如"com.wiseplay.drm"。

**返回值：**

类型说明boolean返回是否支持。true表示支持指定的DRM解决方案，false表示不支持指定的DRM解决方案。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed, the param name's length is zero or too big(exceeds 4096 Bytes).24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let supported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm");
  console.info("isMediaKeySystemSupported: ", supported);
} catch (err) {
  let error = err as BusinessError;
  console.error(`isMediaKeySystemSupported ERROR: ${error}`);
}
```

[]()[]()

#### drm.isMediaKeySystemSupported

isMediaKeySystemSupported(name: string, mimeType: string): boolean

判断设备是否支持指定DRM解决方案及媒体类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明namestring是DRM解决方案名称。建议先调用[isMediaKeySystemSupported](Functions (arkts-apis-drm-f).md#ZH-CN_TOPIC_0000002529285815__drmismediakeysystemsupported)判断是否是支持的解决方案名称。mimeTypestring是媒体类型，支持的媒体类型取决于DRM解决方案，如：video/avc、video/hev。

**返回值：**

类型说明boolean返回是否支持。true表示支持指定DRM解决方案及媒体类型，false表示不支持指定DRM解决方案及媒体类型。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let supported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm", "video/avc");
  console.info("isMediaKeySystemSupported: ", supported);
} catch (err) {
  let error = err as BusinessError;
  console.error(`isMediaKeySystemSupported ERROR: ${error}`);
}
```

[]()[]()

#### drm.isMediaKeySystemSupported

isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean

判断设备是否支持指定DRM解决方案、媒体类型以及内容保护级别。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明namestring是DRM解决方案名称。建议先调用[isMediaKeySystemSupported](Functions (arkts-apis-drm-f).md#ZH-CN_TOPIC_0000002529285815__drmismediakeysystemsupported)判断是否是支持的解决方案名称。mimeTypestring是媒体类型，支持的媒体类型取决于DRM解决方案。建议先调用[isMediaKeySystemSupported](Functions (arkts-apis-drm-f).md#ZH-CN_TOPIC_0000002529285815__drmismediakeysystemsupported-1)判断是否是DRM解决方案支持的类型。level[ContentProtectionLevel](Enums (arkts-apis-drm-e).md#ZH-CN_TOPIC_0000002529285817__contentprotectionlevel)是内容保护级别。

**返回值：**

类型说明boolean返回是否支持。true表示支持指定DRM解决方案、媒体类型以及内容保护级别，false表示不支持指定DRM解决方案、媒体类型以及内容保护级别。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let supported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm", "video/avc", drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
  console.info("isMediaKeySystemSupported: ", supported);
} catch (err) {
  let error = err as BusinessError;
  console.error(`isMediaKeySystemSupported ERROR: ${error}`);
}
```

[]()[]()

#### drm.getMediaKeySystemUuid12+

getMediaKeySystemUuid(name: string): string;

获取DRM解决方案支持的DRM内容保护系统唯一标识。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

参数名类型必填说明namestring是DRM解决方案名称，支持的解决方案名称可通过[isMediaKeySystemSupported](Functions (arkts-apis-drm-f).md#ZH-CN_TOPIC_0000002529285815__drmismediakeysystemsupported)判断。

**返回值：**

类型说明stringDRM内容保护系统的唯一标识。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息401The parameter check failed.Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let uuid: string = drm.getMediaKeySystemUuid("com.wiseplay.drm");
  console.info("getMediaKeySystemUuid: ", uuid);
} catch (err) {
  let error = err as BusinessError;
  console.error(`getMediaKeySystemUuid ERROR: ${error}`);
}
```

[]()[]()

#### drm.getMediaKeySystems12+

getMediaKeySystems(): MediaKeySystemDescription[]

获取设备支持的插件信息列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

类型说明[MediaKeySystemDescription[]](zh-cn_topic_0000002497445846.html#ZH-CN_TOPIC_0000002497445846__mediakeysystemdescription12)设备支持的插件信息列表。

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](../../errors/DRM错误码.md)。

错误码ID错误信息24700101All unknown errors24700201Fatal service error, for example, service died

**示例：**

```ets
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getMediaKeySystems ERROR: ${error}`);
}
```