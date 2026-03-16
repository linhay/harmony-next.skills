# @ohos.multimodalAwareness.metadataBinding (记忆链接)

本模块提供记忆链接能力调用，包括编码内容传递、订阅事件和取消订阅事件。

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

#### metadataBinding.submitMetadata

submitMetadata(metadata: string): void

第三方应用将需要编码的内容传递给MSDP，MSDP决定适时将内容传递给调用编码接口的系统应用或服务。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.MultimodalAwareness.MetadataBinding

**参数**：

参数名类型必填说明metadatastring是要嵌入图片中的信息。

**错误码**：

以下错误码的详细介绍请参见[记忆链接错误码](../../errors/记忆链接错误码.md)。

错误码ID错误信息32100001Internal handling failed. Set Meta data to screenshot app fail.

**示例**：

```ets
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let metadata: string = "";
try {
  metadataBinding.submitMetadata(metadata);
} catch (error) {
  console.error("submit metadata error" + error);
}
```

#### metadataBinding.on('operationSubmitMetadata')

on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void

订阅系统事件以获取编码内容，应用注册回调，事件发生时回传编码内容。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.MultimodalAwareness.MetadataBinding

**参数**：

参数名类型必填说明typestring是事件类型，type为‘operationSubmitMetadata’，表示系统应用获取编码内容。bundleNamestring是应用包名，标识注册应用的包名。callbackCallback<number>是回调函数，用于返回编码内容。

**错误码**：

以下错误码的详细介绍请参见[记忆链接错误码](../../errors/记忆链接错误码.md)。

错误码ID错误信息32100001Internal handling failed. Service exception.32100004Subscribe Failed. Possible causes: 1. Abnormal system capability; 2. IPC communication abnormality; 3. Algorithm loading exception.

**示例：**

```ets
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let bundleName: string = '';
try {
  metadataBinding.on('operationSubmitMetadata', bundleName, (event: number) => {
    if (event == 1) {
      console.info("The screenshot request is intercepted and the app link is obtained");
    }
  });
} catch (error) {
  console.error("register screenshot event error");
}
```

#### metadataBinding.off('operationSubmitMetadata')

off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void

取消订阅系统获取编码内容的事件。取消注册回调接口。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.MultimodalAwareness.MetadataBinding

**参数**：

参数名类型必填说明typestring是事件类型，type为“operationSubmitMetadata”，表示系统应用获取编码内容。bundleNamestring是应用包名，标识注册应用的包名。callbackCallback<number>否回调函数，返回编码内容。

**错误码**：

以下错误码的详细介绍请参见[记忆链接错误码](../../errors/记忆链接错误码.md)。

错误码ID错误信息32100001Internal handling failed. Service exception.32100005Unsubscribe Failed. Possible causes: 1. Abnormal system capability; 2. IPC communication abnormality.

**示例**：

```ets
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let bundleName: string = '';
try {
  metadataBinding.off('operationSubmitMetadata', bundleName, (event: number) => {
  });
} catch (error) {
  console.error("unsubscript screenshot event" + error);
}
```