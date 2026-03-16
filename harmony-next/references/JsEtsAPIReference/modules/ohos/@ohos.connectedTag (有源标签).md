# @ohos.connectedTag (有源标签)

本模块提供有源标签的使用，包括初始化有源标签芯片、读取有源标签内容、写入内容到有源标签等。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { connectedTag } from '@kit.ConnectivityKit';
```

#### connectedTag.init(deprecated)

init(): boolean

初始化有源标签芯片。

从API version 8开始支持，从API version 9开始废弃，建议使用[initialize](#ZH-CN_TOPIC_0000002497605422__connectedtaginitialize9)替代。

**需要权限**：ohos.permission.NFC_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

**类型****说明**boolean

true：初始化成功。

false：初始化失败。

#### connectedTag.initialize9+

initialize(): void

初始化有源标签芯片。

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[NFC错误码](../../errors/NFC错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.3200101Connected NFC tag running state is abnormal in service.

#### connectedTag.uninit(deprecated)

uninit(): boolean

卸载有源标签芯片资源。

从API version 8开始支持，从API version 9开始废弃，建议使用[uninitialize](#ZH-CN_TOPIC_0000002497605422__connectedtaguninitialize9)替代。

**需要权限**：ohos.permission.NFC_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

**类型****说明**boolean

true：卸载操作成功。

false：卸载操作失败。

#### connectedTag.uninitialize9+

uninitialize(): void

卸载有源标签芯片资源。

**需要权限:** ohos.permission.NFC_TAG

**系统能力:** SystemCapability.Communication.ConnectedTag

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[NFC错误码](../../errors/NFC错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.3200101Connected NFC tag running state is abnormal in service.

#### connectedTag.readNdefTag(deprecated)

readNdefTag(): Promise<string>

读取有源标签内容，使用promise方式作为异步方法。

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.read](#ZH-CN_TOPIC_0000002497605422__connectedtagread9)替代。

**需要权限**：ohos.permission.NFC_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

**类型****说明**Promise<string>返回读取有源标签内容。

**示例：**

```ets
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

connectedTag.readNdefTag().then((data) => {
    console.info("connectedTag readNdefTag Promise data = " + data);
}).catch((err: BusinessError)=> {
    console.error("connectedTag readNdefTag Promise err: " + err);
});
```

#### connectedTag.read9+

read(): Promise<number[]>

读取有源标签内容，使用promise方式作为异步方法。

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**返回值：**

**类型****说明**Promise<number[]>返回读取有源标签内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[NFC错误码](../../errors/NFC错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.3200101Connected NFC tag running state is abnormal in service.

**示例：**

```ets
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

connectedTag.read().then((data) => {
    console.info("connectedTag read Promise data = " + data);
}).catch((err: BusinessError)=> {
    console.error("connectedTag read Promise err: " + err);
});
```

#### connectedTag.readNdefTag(deprecated)

readNdefTag(callback: AsyncCallback<string>): void

读取有源标签内容，使用AsyncCallback方式作为异步方法。

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.read](#ZH-CN_TOPIC_0000002497605422__connectedtagread9)替代。

**需要权限**：ohos.permission.NFC_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

**参数名****类型****必填****说明**callbackAsyncCallback<string>是读取有源标签内容回调函数。

**示例：**

```ets
import { connectedTag } from '@kit.ConnectivityKit';

connectedTag.readNdefTag((err, data)=> {
    if (err) {
        console.error("connectedTag readNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag readNdefTag AsyncCallback data: " + data);
    }
});
```

#### connectedTag.read9+

read(callback: AsyncCallback<number[]>): void

读取有源标签内容，使用AsyncCallback方式作为异步方法。

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

**参数名****类型****必填****说明**callbackAsyncCallback<number[]>是读取有源标签内容回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[NFC错误码](../../errors/NFC错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.3200101Connected NFC tag running state is abnormal in service.

**示例：**

```ets
import { connectedTag } from '@kit.ConnectivityKit';

connectedTag.read((err, data)=> {
    if (err) {
        console.error("connectedTag read AsyncCallback err: " + err);
    } else {
        console.info("connectedTag read AsyncCallback data: " + data);
    }
});
```

#### connectedTag.writeNdefTag(deprecated)

writeNdefTag(data: string): Promise<void>

写入内容到有源标签，使用promise方式作为异步方法。

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.write](#ZH-CN_TOPIC_0000002497605422__connectedtagwrite9)替代。

**需要权限**：ohos.permission.NFC_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

**参数名****类型****必填****说明**datastring是有源标签内容, 最大长度为1024个字节。

**返回值：**

**类型****说明**Promise<void>无返回值。

**示例：**

```ets
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData).then(() => {
    console.info("connectedTag.writeNdefTag Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.writeNdefTag Promise err: " + err);
});
```

#### connectedTag.write9+

write(data: number[]): Promise<void>

写入内容到有源标签，使用promise方式作为异步方法。

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

**参数名****类型****必填****说明**datanumber[]是有源标签内容, 由十六进制数字组成。范围：0x00至0xFF。

**返回值：**

**类型****说明**Promise<void>无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[NFC错误码](../../errors/NFC错误码.md)。

错误码ID错误信息201Permission denied.401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3200101Connected NFC tag running state is abnormal in service.

**示例：**

```ets
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData).then(() => {
    console.info("connectedTag.writeNdefTag Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.writeNdefTag Promise err: " + err);
});
```

#### connectedTag.writeNdefTag(deprecated)

writeNdefTag(data: string, callback: AsyncCallback<void>): void

写入内容到有源标签，使用AsyncCallback方式作为异步方法。

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.write](#ZH-CN_TOPIC_0000002497605422__connectedtagwrite9)替代。

**需要权限**：ohos.permission.NFC_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

**参数名****类型****必填****说明**datastring是有源标签内容, 最大长度为1024个字节。callbackAsyncCallback<void>是读取有源标签内容回调函数。

**示例：**

```ets
import { connectedTag } from '@kit.ConnectivityKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.writeNdefTag AsyncCallback success.");
    }
});
```

#### connectedTag.write9+

write(data: number[], callback: AsyncCallback<void>): void

写入内容到有源标签，使用AsyncCallback方式作为异步方法。

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

**参数名****类型****必填****说明**datanumber[]是有源标签内容, 由十六进制数字组成。范围：0x00至0xFF。callbackAsyncCallback<void>是读取有源标签内容回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[NFC错误码](../../errors/NFC错误码.md)。

错误码ID错误信息201Permission denied.401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3200101Connected NFC tag running state is abnormal in service.

**示例：**

```ets
import { connectedTag } from '@kit.ConnectivityKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.writeNdefTag AsyncCallback success.");
    }
});
```

#### connectedTag.on('notify')

on(type: "notify", callback: Callback<number>): void

注册NFC场强状态事件。

**需要权限**：ohos.permission.NFC_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

**参数名****类型****必填****说明**typestring是固定填"notify"字符串。callbackCallback<number>是状态改变回调函数，返回值参见[NfcRfType](#ZH-CN_TOPIC_0000002497605422__nfcrftype)。

#### connectedTag.off('notify')

off(type: "notify", callback?: Callback<number>): void

取消NFC场强状态事件的注册。

**需要权限**：ohos.permission.NFC_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

**参数名****类型****必填****说明**typestring是固定填"notify"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将“去注册”该事件关联的所有回调函数。

**示例：**

```ets
import { connectedTag } from '@kit.ConnectivityKit';

function nfcStatusCb(rfState: connectedTag.NfcRfType) {
    console.info("connectedTag on Callback rfState: ", rfState);
}

// 有源nfc标签的使用流程
async function nfcTagTestOn(): Promise<void> {
    try {
        console.info("connectedTag initialize");
        connectedTag.initialize();
    } catch (error) {
        console.error("initialize error:" + error);
    }
    // 注册回调以接收nfc进离场状态更改通知
    connectedTag.on("notify", nfcStatusCb);
    try {
        let tag = [3, 1, 0];
        console.info("connectedTag write: tag=" + tag);
        await connectedTag.write(tag);
        let data = await connectedTag.read();
        console.info("connectedTag read: data=" + data);
    } catch (error) {
        console.error("connectedTag error: " + error);
    }
}

// 业务退出时，取消注册回调、取消初始化
async function nfcTagTestOff(): Promise<void> {
    // 取消注册回调
    connectedTag.off("notify", nfcStatusCb);
    try {
        console.info("connectedTag uninitialize");
        connectedTag.uninitialize();
    } catch (error) {
        console.error("connectedTag error: " + error);
    }
}

export { nfcTagTestOn, nfcTagTestOff }
```

#### NfcRfType

表示NFC场强状态的枚举。

**系统能力**：SystemCapability.Communication.ConnectedTag

名称值说明NFC_RF_LEAVE0NFC离场事件。NFC_RF_ENTER1NFC进场事件。