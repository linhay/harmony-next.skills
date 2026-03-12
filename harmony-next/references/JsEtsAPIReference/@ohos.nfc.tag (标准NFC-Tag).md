# @ohos.nfc.tag (标准NFC-Tag)

本模块主要用于操作及管理NFC Tag，提供后台读卡和前台应用优先分发两种读卡模式。

后台读卡是指不需要打开应用程序，电子设备通过NFC读取标签卡片后，根据标签卡片的类型匹配到一个或多个应用程序。如果仅匹配到一个，则直接拉起应用程序的读卡页面；如果是多个则弹出应用选择器，让用户选择指定的读卡应用。后台读卡不涉及tag相关接口，示例参考[nfc-tag开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide#后台读取标签)。

前台读卡是指提前打开应用程序，并进入对应的NFC读卡页面后读卡，只会把读到的标签卡片信息分发给前台应用程序。

1. 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
1. 调用本模块接口和常量时请使用canIUse("SystemCapability.Communication.NFC.Tag")判断设备是否支持NFC能力，否则可能导致应用运行稳定性问题，参考[nfc-tag开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide)。
1. 导入tag模块编辑器报错，在某个具体设备型号上能力可能超出工程默认设备定义的能力集范围，如需要使用此部分能力需额外配置自定义syscap，参考[syscap开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap#syscap开发指导)。

#### **导入模块**

```ets
import { tag } from '@kit.ConnectivityKit';
```

#### **tag.TagInfo**

在对相关Tag类型卡片进行读写之前，必须先获取[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)相关属性值，以确认设备读取到的Tag卡片支持哪些技术类型。这样Tag应用程序才能调用正确的接口和所读取到的Tag卡片进行通信。

```ets
import { tag } from '@kit.ConnectivityKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want : Want, launchParam: AbilityConstant.LaunchParam) {
        // 添加其他功能代码...

        // want由nfc服务初始化，包含找到的tag
        let tagInfo : tag.TagInfo | null = null;
        try {
            tagInfo = tag.getTagInfo(want);
        } catch (error) {
            console.error("tag.getTagInfo catch error: " + error);
        }
        if (tagInfo == null) {
            console.error("no TagInfo to be created, ignore it.");
            return;
        }

        // 获取发现标签的支持技术
        let isNfcATag =  false;
        let isIsoDepTag =  false;
        for (let i = 0; i < tagInfo.technology.length; i++) {
            if (tagInfo.technology[i] == tag.NFC_A) {
                isNfcATag = true;
            }
            if (tagInfo.technology[i] == tag.ISO_DEP) {
                isIsoDepTag = true;
            }
        // 检查其他技术类型: tag.NFC_B/NFC_F/NFC_V/NDEF/MIFARE_CLASSIC/MIFARE_ULTRALIGHT/NDEF_FORMATABLE
        }

        // 使用 NfcA APIs 去访问发现的标签
        if (isNfcATag) {
            let nfcA : tag.NfcATag | null = null;
            try {
                nfcA = tag.getNfcA(tagInfo);
            } catch (error) {
                console.error("tag.getNfcA catch error: " + error);
            }
            // 其他代码：对发现的标签执行读取或写入
        }

        // 使用 IsoDep APIs 去访问发现的标签
        if (isIsoDepTag) {
            let isoDep : tag.IsoDepTag | null = null;
            try {
                isoDep = tag.getIsoDep(tagInfo);
            } catch (error) {
                console.error("tag.getIsoDep catch error: " + error);
            }
            // 其他代码：对发现的标签执行读取或写入
        }
        // 使用相同的代码来处理 "NfcA/NfcB/NfcF/NfcV/Ndef/MifareClassic/MifareUL/NdefFormatable".
    }
}
```

#### tag.getNfcATag(deprecated)

getNfcATag(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NfcATag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__nfcatag)

获取NFC A类型Tag对象，通过该对象可访问NfcA技术类型的Tag。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tag.getNfcA](#ZH-CN_TOPIC_0000002529445389__taggetnfca9)替代。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NfcATag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcatag)NFC A类型Tag对象。

#### tag.getNfcA9+

getNfcA(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NfcATag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__nfcatag)

获取NFC A类型Tag对象，通过该对象可访问NfcA技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NfcATag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcatag)NFC A类型Tag对象。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getNfcBTag(deprecated)

getNfcBTag(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NfcBTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__nfcbtag)

获取NFC B类型Tag对象，通过该对象可访问NfcB技术类型的Tag。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tag.getNfcB](#ZH-CN_TOPIC_0000002529445389__taggetnfcb9)替代。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NfcBTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcbtag)NFC B类型Tag对象。

#### tag.getNfcB9+

getNfcB(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NfcBTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__nfcbtag)

获取NFC B类型Tag对象，通过该对象可访问NfcB技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NfcBTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcbtag)NFC B类型Tag对象。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getNfcFTag(deprecated)

getNfcFTag(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NfcFTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__nfcftag)

获取NFC F类型Tag对象，通过该对象可访问NfcF技术类型的Tag。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tag.getNfcF](#ZH-CN_TOPIC_0000002529445389__taggetnfcf9)替代。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NfcFTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcftag)NFC F类型Tag对象。

#### tag.getNfcF9+

getNfcF(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NfcFTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__nfcftag)

获取NFC F类型Tag对象，通过该对象可访问NfcF技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NfcFTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcftag)NFC F类型Tag对象。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getNfcVTag(deprecated)

getNfcVTag(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NfcVTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__nfcvtag)

获取NFC V类型Tag对象，通过该对象可访问NfcV技术类型的Tag。

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tag.getNfcV](#ZH-CN_TOPIC_0000002529445389__taggetnfcv9)替代。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NfcVTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcvtag)NFC V类型Tag对象。

#### tag.getNfcV9+

getNfcV(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NfcVTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__nfcvtag)

获取NFC V类型Tag对象，通过该对象可访问NfcV技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NfcVTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcvtag)NFC V类型Tag对象。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getIsoDep9+

getIsoDep(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [IsoDepTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__isodeptag9)

获取IsoDep类型Tag对象，通过该对象可访问支持IsoDep技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[IsoDepTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__isodeptag9)IsoDep类型Tag对象，通过该对象访问IsoDep类型的相关接口。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getNdef9+

getNdef(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NdefTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__ndeftag9)

获取NDEF类型Tag对象，通过该对象可访问支持NDEF技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NdefTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndeftag9)NDEF类型Tag对象，通过该对象访问NDEF类型的相关接口。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getMifareClassic9+

getMifareClassic(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [MifareClassicTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__mifareclassictag9)

获取MIFARE Classic类型Tag对象，通过该对象访问支持MIFARE Classic技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[MifareClassicTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__mifareclassictag9)MIFARE Classic类型Tag对象，通过该对象访问MIFARE Classic类型的相关接口。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getMifareUltralight9+

getMifareUltralight(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [MifareUltralightTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__mifareultralighttag9)

获取MIFARE Ultralight类型Tag对象，通过该对象可访问支持MIFARE Ultralight技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[MifareUltralightTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__mifareultralighttag9)MIFARE Ultralight类型Tag对象，通过该对象访问MIFARE Ultralight类型的相关接口。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getNdefFormatable9+

getNdefFormatable(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [NdefFormatableTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__ndefformatabletag9)

获取NDEF Formatable类型Tag对象，通过该对象可访问支持NDEF Formatable技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

**类型****说明**[NdefFormatableTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndefformatabletag9)NDEF Formatable类型Tag对象，通过该对象访问NDEF Formatable类型的相关接口。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getBarcodeTag18+

getBarcodeTag(tagInfo: [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)): [BarcodeTag](zh-cn_topic_0000002497605426.html#ZH-CN_TOPIC_0000002497605426__barcodetag18)

获取BarcodeTag类型Tag对象，通过该对象可访问BarcodeTag技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tagInfo[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)是包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](#ZH-CN_TOPIC_0000002529445389__taggettaginfo9)获取。

**返回值：**

类型说明[BarcodeTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__barcodetag18)BarcodeTag类型Tag对象。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

#### tag.getTagInfo9+

getTagInfo(want: [Want](@ohos.app.ability.Want (Want).md#ZH-CN_TOPIC_0000002529284603__want)): [TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)

从Want中获取TagInfo，Want是被NFC服务初始化，包含了TagInfo所需的属性值。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md#ZH-CN_TOPIC_0000002529284603__want)是分发Ability时，在系统onCreate入口函数的参数中获取。

**返回值：**

**类型****说明**[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)TagInfo对象，用于获取不同技术类型的Tag对象。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.

#### tag.registerForegroundDispatch10+

registerForegroundDispatch(elementName: [ElementName](ElementName.md), discTech: number[], callback: AsyncCallback<[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)>): void

注册对NFC Tag读卡事件的监听，实现前台应用优先分发的目的。通过discTech设置支持的读卡技术类型，通过callback方式获取读取到Tag的[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)信息。应用必须在前台才能调用。需要与取消监听接口[tag.unregisterForegroundDispatch](#ZH-CN_TOPIC_0000002529445389__tagunregisterforegrounddispatch10)成对使用。如果已注册事件监听，需要在页面退出前台或页面销毁前调用取消注册。使用callback异步回调。

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明elementName[ElementName](ElementName.md)是所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。discTechnumber[]是前台应用指定的NFC读卡技术类型，不可以为空，至少指定一种读卡技术类型。每个number值表示所支持技术类型的常量值型，根据number值设置NFC读卡轮询的Tag技术类型（仅包含[NFC_A](#ZH-CN_TOPIC_0000002529445389__常量), [NFC_B](#ZH-CN_TOPIC_0000002529445389__常量), [NFC_F](#ZH-CN_TOPIC_0000002529445389__常量), [NFC_V](#ZH-CN_TOPIC_0000002529445389__常量)中的一种或多种）。callbackAsyncCallback<[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)>是前台读卡监听回调函数，返回读到的Tag信息，不可以为空。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息201Permission denied.401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.3100202The element state is invalid.

**示例：**

示例请参见[tag.unregisterForegroundDispatch](#ZH-CN_TOPIC_0000002529445389__tagunregisterforegrounddispatch10)接口的示例。

#### tag.unregisterForegroundDispatch10+

unregisterForegroundDispatch(elementName: [ElementName](ElementName.md)): void

取消注册对NFC Tag读卡事件的监听，退出前台应用优先分发。如果已注册事件监听，需要在页面退出前台或页面销毁前调用取消注册。

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明elementName[ElementName](ElementName.md)是所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息201Permission denied.401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

let discTech : number[] = [tag.NFC_A, tag.NFC_B]; // 用前台ability时所需要的技术代替
let elementName : bundleManager.ElementName;
function foregroundCb(err : BusinessError, tagInfo : tag.TagInfo) {
    if (!err) {
        console.info("foreground callback: tag found tagInfo = ", JSON.stringify(tagInfo));
    } else {
        console.error("foreground callback err: " + err.message);
        return;
    }
  // taginfo的其他操作
}

export default class MainAbility extends UIAbility {
    OnCreate(want : Want, launchParam : AbilityConstant.LaunchParam) {
        console.info("OnCreate");
        elementName = {
            bundleName: want.bundleName as string,
            abilityName: want.abilityName as string,
            moduleName: want.moduleName as string
        }
    }

    onForeground() {
        console.info("onForeground");
        try {
            tag.registerForegroundDispatch(elementName, discTech, foregroundCb);
        } catch (e) {
            console.error("registerForegroundDispatch error: " + (e as BusinessError).message);
        }
    }

    onBackground() {
        console.info("onBackground");
        try {
            tag.unregisterForegroundDispatch(elementName);
        } catch (e) {
            console.error("unregisterForegroundDispatch error: " + (e as BusinessError).message);
        }
    }

    onWindowStageDestroy() {
        console.info("onWindowStageDestroy");
        try {
            tag.unregisterForegroundDispatch(elementName);
        } catch (e) {
            console.error("unregisterForegroundDispatch error: " + (e as BusinessError).message);
        }
    }

  // ability生命周期内的其他功能
}
```

#### tag.on11+

on(type: 'readerMode', elementName: [ElementName](ElementName.md), discTech: number[], callback: AsyncCallback<[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)>): void

订阅NFC Tag读卡事件，实现前台应用优先分发。设备会进入读卡器模式，同时关闭卡模拟。通过discTech设置支持的读卡技术类型，通过callback方式获取到Tag的[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)信息。需要与取消读卡器模式的[tag.off](#ZH-CN_TOPIC_0000002529445389__tagoff11)成对使用，如果已通过on进行设置，需要在页面退出前台或页面销毁时调用[tag.off](#ZH-CN_TOPIC_0000002529445389__tagoff11)。使用callback异步回调。

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明typestring是要注册的回调类型，固定填"readerMode"字符串。elementName[ElementName](ElementName.md)是所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。discTechnumber[]是前台应用指定的NFC读卡技术类型，不可以为空，至少指定一种读卡技术类型。每个number值表示所支持技术类型的常量值型，根据number值设置NFC读卡轮询的Tag技术类型（仅包含[NFC_A](#ZH-CN_TOPIC_0000002529445389__常量), [NFC_B](#ZH-CN_TOPIC_0000002529445389__常量), [NFC_F](#ZH-CN_TOPIC_0000002529445389__常量), [NFC_V](#ZH-CN_TOPIC_0000002529445389__常量)中的一种或多种）。callbackAsyncCallback<[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)>是读卡器模式监听回调函数，返回读到的Tag信息，不可以为空。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息201Permission denied.401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.3100202The element state is invalid.

**示例：**

示例请参见[tag.off](#ZH-CN_TOPIC_0000002529445389__tagoff11)接口的示例。

#### tag.off11+

off(type: 'readerMode', elementName: [ElementName](ElementName.md), callback?: AsyncCallback<[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)>): void

取消订阅NFC Tag读卡事件。设备退出读卡模式，并恢复卡模拟。如果已通过[tag.on](#ZH-CN_TOPIC_0000002529445389__tagon11)设置NFC的读卡器模式，需要在页面退出前台或页面销毁时调用off进行取消。

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明typestring是要注销的回调类型，固定填"readerMode"字符串。elementName[ElementName](ElementName.md)是所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。callbackAsyncCallback<[TagInfo](#ZH-CN_TOPIC_0000002529445389__taginfo)>否前台读卡监听回调函数，返回读到的Tag信息。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息201Permission denied.401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3100201The tag running state is abnormal in the service.3100203The off() API can be called only when the on() has been called.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

let discTech : number[] = [tag.NFC_A, tag.NFC_B]; // 用前台ability时所需要的技术代替
let elementName : bundleManager.ElementName;

function readerModeCb(err : BusinessError, tagInfo : tag.TagInfo) {
    if (!err) {
        console.info("offCallback: tag found tagInfo = ", JSON.stringify(tagInfo));
    } else {
        console.error("offCallback err: " + err.message);
        return;
    }
  // taginfo的其他操作
}

export default class MainAbility extends UIAbility {
    OnCreate(want : Want, launchParam : AbilityConstant.LaunchParam) {
        console.info("OnCreate");
        elementName = {
            bundleName: want.bundleName as string,
            abilityName: want.abilityName as string,
            moduleName: want.moduleName as string
        }
    }

    onForeground() {
        console.info("on start");
        try {
            tag.on('readerMode', elementName, discTech, readerModeCb);
        } catch (e) {
            console.error("tag.on error: " + (e as BusinessError).message);
        }
    }

    onBackground() {
        console.info("onBackground");
        try {
            tag.off('readerMode', elementName, readerModeCb);
        } catch (e) {
            console.error("tag.off error: " + (e as BusinessError).message);
        }
    }

    onWindowStageDestroy() {
        console.info("onWindowStageDestroy");
        try {
            tag.off('readerMode', elementName, readerModeCb);
        } catch (e) {
            console.error("tag.off error: " + (e as BusinessError).message);
        }
    }

  // ability生命周期内的其他功能
}
```

#### tag.ndef.makeUriRecord9+

makeUriRecord(uri: string): NdefRecord

根据输入的URI，构建NDEF标签的Record数据对象。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明uristring是写入到NDEF Record里面的数据内容。

**返回值：**

**类型****说明**[NdefRecord](#ZH-CN_TOPIC_0000002529445389__ndefrecord9)NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF_1.0》。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';

try {
    let uri = "https://www.example.com"; // 修改为正确可用的uri
    let ndefRecord : tag.NdefRecord = tag.ndef.makeUriRecord(uri);
    if (ndefRecord != undefined) {
        console.info("ndefMessage makeUriRecord rtdType: " + ndefRecord.rtdType);
        console.info("ndefMessage makeUriRecord payload: " + ndefRecord.payload);
    } else {
        console.error("ndefMessage makeUriRecord ndefRecord: " + ndefRecord);
    }
} catch (businessError) {
    console.error("ndefMessage makeUriRecord catch businessError: " + businessError);
}
```

#### tag.ndef.makeTextRecord9+

makeTextRecord(text: string, locale: string): NdefRecord

根据输入的文本数据和编码类型，构建NDEF标签的Record。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明textstring是写入到NDEF Record里面的文本数据内容。localestring是文本数据内容的编码方式。

**返回值：**

**类型****说明**[NdefRecord](#ZH-CN_TOPIC_0000002529445389__ndefrecord9)NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF_1.0》。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';

try {
    let text = "Hello World";   // 修改为想要写入的文本
    let locale = "en"; // 修改为预期的编码格式
    let ndefRecord : tag.NdefRecord = tag.ndef.makeTextRecord(text, locale);
    if (ndefRecord != undefined) {
        console.info("ndefMessage makeTextRecord rtdType: " + ndefRecord.rtdType);
        console.info("ndefMessage makeTextRecord payload: " + ndefRecord.payload);
    } else {
        console.error("ndefMessage makeTextRecord ndefRecord: " + ndefRecord);
    }
} catch (businessError) {
    console.error("ndefMessage makeTextRecord catch businessError: " + businessError);
}
```

#### tag.ndef.makeApplicationRecord18+

makeApplicationRecord(bundleName: string): NdefRecord

根据HarmonyOS应用的bundlename，构建NDEF标签的Record。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明bundleNamestring是要创建标签的应用包名。

**返回值：**

**类型****说明**[NdefRecord](#ZH-CN_TOPIC_0000002529445389__ndefrecord9)NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF_1.0》。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';

try {
    let bundleName: string = 'com.demo.test';
    let ndefRecord : tag.NdefRecord = tag.ndef.makeApplicationRecord(bundleName);
    if (ndefRecord != undefined) {
        console.info("ndefMessage makeApplicationRecord rtdType: " + ndefRecord.rtdType);
        console.info("ndefMessage makeApplicationRecord payload: " + ndefRecord.payload);
    } else {
        console.error("ndefMessage makeApplicationRecord ndefRecord: " + ndefRecord);
    }
} catch (businessError) {
    console.error("ndefMessage makeApplicationRecord catch businessError: " + businessError);
}
```

#### tag.ndef.makeMimeRecord9+

makeMimeRecord(mimeType: string, mimeData: number[]): NdefRecord

根据输入的MIME数据和类型，构建NDEF标签的Record。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明mimeTypestring是符合RFC规则的MIME类型，比如"text/plain"或"image/jpeg"。mimeDatanumber[]是MIME数据内容，每个number十六进制表示，范围是0x00~0xFF。

**返回值：**

**类型****说明**[NdefRecord](#ZH-CN_TOPIC_0000002529445389__ndefrecord9)NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF_1.0》。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';

try {
    let mimeType = "text/plain";   // 修改为预期的符合规则的MIME类型
    let mimeData = [0x01, 0x02, 0x03, 0x04]; // 修改为预期的符合格式的数据
    let ndefRecord : tag.NdefRecord = tag.ndef.makeMimeRecord(mimeType, mimeData);
    if (ndefRecord != undefined) {
        console.info("ndefMessage makeMimeRecord rtdType: " + ndefRecord.rtdType);
        console.info("ndefMessage makeMimeRecord payload: " + ndefRecord.payload);
    } else {
        console.error("ndefMessage makeMimeRecord ndefRecord: " + ndefRecord);
    }
} catch (businessError) {
    console.error("ndefMessage makeMimeRecord catch businessError: " + businessError);
}
```

#### tag.ndef.makeExternalRecord9+

makeExternalRecord(domainName: string, type: string, externalData: number[]): NdefRecord

根据应用程序特定的外部数据，构建NDEF标签的Record。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明domainNamestring是外部数据发布组织的域名，一般是应用程序的包名。typestring是外部数据的指定类型。externalDatanumber[]是外部数据内容，每个number十六进制表示，范围是0x00~0xFF。

**返回值：**

**类型****说明**[NdefRecord](#ZH-CN_TOPIC_0000002529445389__ndefrecord9)NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF_1.0》。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';

try {
    let domainName = "ohos.nfc.application"; // 修改为符合规范的包名
    let type = "test"; // 修改为正确的数据类型
    let externalData = [0x01, 0x02, 0x03, 0x04]; // 修改为正确的外部数据内容
    let ndefRecord : tag.NdefRecord = tag.ndef.makeExternalRecord(domainName, type, externalData);
    if (ndefRecord != undefined) {
        console.info("ndefMessage makeExternalRecord rtdType: " + ndefRecord.rtdType);
        console.info("ndefMessage makeExternalRecord payload: " + ndefRecord.payload);
    } else {
        console.error("ndefMessage makeExternalRecord ndefRecord: " + ndefRecord);
    }
} catch (businessError) {
    console.error("ndefMessage makeExternalRecord catch businessError: " + businessError);
}
```

#### tag.ndef.messageToBytes9+

messageToBytes(ndefMessage: [NdefMessage](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndefmessage9)): number[]

把输入的NDEF消息数据对象，转换为字节格式的数据。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明ndefMessage[NdefMessage](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndefmessage9)是NDEF消息数据对象。

**返回值：**

**类型****说明**number[]NDEF消息数据对象，所转换成的字节格式的数据。每个number十六进制表示，范围是0x00~0xFF。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';

let rawData = [0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43]; // 必须符合NDEF格式的数据
try {
    let ndefMessage : tag.NdefMessage = tag.ndef.createNdefMessage(rawData);
    console.info("ndef createNdefMessage, ndefMessage: " + ndefMessage);
    let rawData2 : number[] = tag.ndef.messageToBytes(ndefMessage);
    console.info("ndefMessage messageToBytes rawData2: " + rawData2);
} catch (businessError) {
    console.error("ndef createNdefMessage businessError: " + businessError);
}
```

#### tag.ndef.createNdefMessage9+

createNdefMessage(data: number[]): [NdefMessage](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndefmessage9)

使用原始字节数据创建NDEF标签的Message。该数据必须符合NDEF Record数据格式，如果不符合格式，则返回的NdefMessage数据对象，所包含的NDEF Record列表会为空。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

**参数名****类型****必填****说明**datanumber[]是原始字节，每个number十六进制表示，范围是0x00~0xFF。要求必须满足NDEF Record的格式。

**返回值：**

**类型****说明**[NdefMessage](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndefmessage9)NDEF标签的Message，详见NDEF技术规范《NFCForum-TS-NDEF_1.0》。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';

let rawData = [0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43];  //必须是可以被解析的NDEF记录
try {
    let ndefMessage : tag.NdefMessage = tag.ndef.createNdefMessage(rawData);
    console.info("ndef createNdefMessage, ndefMessage: " + ndefMessage);
} catch (businessError) {
    console.error("ndef createNdefMessage businessError: " + businessError);
}
```

#### tag.ndef.createNdefMessage9+

createNdefMessage(ndefRecords: NdefRecord[]): [NdefMessage](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndefmessage9)

使用NDEF Records列表，创建NDEF Message。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

**参数名****类型****必填****说明**ndefRecords[NdefRecord](@ohos.nfc.tag (标准NFC-Tag).md#ZH-CN_TOPIC_0000002529445389__ndefrecord9)[]是NDEF标签的Record列表，详见NDEF技术规范《NFCForum-TS-NDEF_1.0》。

**返回值：**

**类型****说明**[NdefMessage](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndefmessage9)NDEF标签的Message，详见NDEF技术规范《NFCForum-TS-NDEF_1.0》。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

**示例：**

```ets
import { tag } from '@kit.ConnectivityKit';

let uriRecord : tag.NdefRecord = tag.ndef.makeUriRecord("https://www.example.com");
let textRecord : tag.NdefRecord = tag.ndef.makeTextRecord("Hello World", "en");
let ndefRecords : tag.NdefRecord[] = [uriRecord, textRecord];
try {
    let ndefMessage : tag.NdefMessage = tag.ndef.createNdefMessage(ndefRecords);
    console.info("ndef createNdefMessage ndefMessage: " + ndefMessage);
} catch (businessError) {
    console.error("ndef createNdefMessage businessError: " + businessError);
}
```

#### TagInfo

NFC服务在读取到标签时给出的对象，通过该对象属性，应用知道该标签支持哪些技术类型，并使用匹配的技术类型来调用相关接口。

**系统能力：** SystemCapability.Communication.NFC.Tag

**需要权限：** ohos.permission.NFC_TAG

**名称****类型****只读****可选****说明**uid9+number[]否否

标签的uid，每个number值是十六进制表示，范围是0x00~0xFF。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

technology9+number[]否否

支持的技术类型，每个number值表示所支持技术类型的常量值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

supportedProfilesnumber[]否否支持的技术类型，从API version 7开始支持，从API version 9开始废弃，使用[tag.TagInfo#technology](#ZH-CN_TOPIC_0000002529445389__taginfo)替代。

#### NdefRecord9+

NDEF标签Record属性的定义，参考NDEF标签技术规范《NFCForum-TS-NDEF_1.0》的定义细节。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**名称****类型****只读****可选****说明**tnfnumber否否NDEF Record的TNF(Type Name Field)。rtdTypenumber[]否否NDEF Record的RTD(Record Type Definition)类型值，每个number十六进制表示，范围是0x00~0xFF。idnumber[]否否NDEF Record的ID，每个number十六进制表示，范围是0x00~0xFF。payloadnumber[]否否NDEF Record的PAYLOAD，每个number十六进制表示，范围是0x00~0xFF。

#### 常量

NFC Tag有多种不同的技术类型，定义常量描述不同的技术类型。

**系统能力：** SystemCapability.Communication.NFC.Tag

**名称****类型****值****说明**NFC_A7+number1

NFC-A (ISO 14443-3A)技术。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

NFC_B7+number2

NFC-B (ISO 14443-3B)技术。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ISO_DEP7+number3

ISO-DEP (ISO 14443-4)技术。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

NFC_F7+number4

NFC-F (JIS 6319-4)技术。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

NFC_V7+number5

NFC-V (ISO 15693)技术。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

NDEF7+number6

NDEF技术。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

NDEF_FORMATABLE9+number7

可以格式化的NDEF技术。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

MIFARE_CLASSIC7+number8

MIFARE Classic技术。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

MIFARE_ULTRALIGHT7+number9

MIFARE Ultralight技术。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

NFC_BARCODE18+number10

BARCODE技术。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

#### TnfType9+

NDEF Record的TNF(Type Name Field)类型值，参考NDEF标签技术规范《NFCForum-TS-NDEF_1.0》的定义细节。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**名称****值****说明**TNF_EMPTY0x0Empty。TNF_WELL_KNOWN0x1NFC Forum well-known type [NFC RTD]。TNF_MEDIA0x2Media-type as defined in RFC 2046 [RFC 2046]。TNF_ABSOLUTE_URI0x3Absolute URI as defined in RFC 3986 [RFC 3986]。TNF_EXT_APP0x4NFC Forum external type [NFC RTD]。TNF_UNKNOWN0x5Unknown。TNF_UNCHANGED0x6Unchanged (see section 2.3.3)。

#### NDEF Record RTD类型定义

NDEF Record的RTD(Record Type Definition)类型值，参考NDEF标签技术规范《NFCForum-TS-NDEF_1.0》的定义细节。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**名称****类型****值****说明**RTD_TEXT9+number[][0x54]文本类型的NDEF Record。RTD_URI9+number[][0x55]URI类型的NDEF Record。

#### NfcForumType9+

NFC Forum标准里面Tag类型的定义。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**名称****值****说明**NFC_FORUM_TYPE_11NFC论坛类型1。NFC_FORUM_TYPE_22NFC论坛类型2。NFC_FORUM_TYPE_33NFC论坛类型3。NFC_FORUM_TYPE_44NFC论坛类型4。MIFARE_CLASSIC101MIFARE Classic类型。

#### MifareClassicType9+

MIFARE Classic标签类型的定义。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**名称****值****说明**TYPE_UNKNOWN0未知的MIFARE类型。TYPE_CLASSIC1MIFARE Classic类型。TYPE_PLUS2MIFARE Plus类型。TYPE_PRO3MIFARE Pro类型。

#### MifareClassicSize9+

MIFARE Classic标签存储大小的定义。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**名称****值****说明**MC_SIZE_MINI320每个标签5个扇区，每个扇区4个块。MC_SIZE_1K1024每个标签16个扇区，每个扇区4个块。MC_SIZE_2K2048每个标签32个扇区，每个扇区4个块。MC_SIZE_4K4096每个标签40个扇区，每个扇区4个块。

#### MifareUltralightType9+

MIFARE Ultralight标签类型的定义。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**名称****值****说明**TYPE_UNKNOWN0未知的 MIFARE 类型。TYPE_ULTRALIGHT1MIFARE Ultralight类型。TYPE_ULTRALIGHT_C2MIFARE UltralightC 类型。

#### NfcATag7+

type NfcATag = _NfcATag

获取NfcATag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_NfcATag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcatag)NfcATag 提供 NFC-A(ISO 14443-3A)技术的属性和I/O操作的访问。

#### NfcBTag7+

type NfcBTag = _NfcBTag

获取NfcBTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_NfcBTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcbtag)NfcBTag 提供 NFC-B(ISO 14443-3B)技术的属性和I/O操作的访问。

#### NfcFTag7+

type NfcFTag = _NfcFTag

获取NfcFTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_NfcFTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcftag)NfcFTag 提供对 NFC-F(JIS 6319-4)技术的属性和I/O操作的访问。

#### NfcVTag7+

type NfcVTag = _NfcVTag

获取NfcVTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_NfcVTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__nfcvtag)NfcVTag 提供对 NFC-V(ISO 15693)技术的属性和I/O操作的访问。

#### IsoDepTag9+

type IsoDepTag = _IsoDepTag

获取IsoDepTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_IsoDepTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__isodeptag9)IsoDepTag 提供 ISO-DEP(ISO 14443-4)技术的属性和I/O操作的访问。

#### NdefTag9+

type NdefTag = _NdefTag

获取NdefTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_NdefTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndeftag9)提供对已格式化为NDEF的NFC标签的数据和操作的访问。

#### MifareClassicTag9+

type MifareClassicTag = _MifareClassicTag

获取MifareClassicTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_MifareClassicTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__mifareclassictag9)MifareClassicTag提供对MIFARE Classic属性和I/O操作的访问。

#### MifareUltralightTag9+

type MifareUltralightTag = _MifareUltralightTag;

获取MifareUltralightTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_MifareUltralightTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__mifareultralighttag9)MifareUltralightTag 提供对MIFARE Ultralight属性和I/O操作的访问。

#### NdefFormatableTag9+

type NdefFormatableTag = _NdefFormatableTag

获取NdefFormatableTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_NdefFormatableTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndefformatabletag9)NdefFormatableTag为NDEF Formattable的标签提供格式化操作。

#### BarcodeTag18+

type BarcodeTag = _BarcodeTag

获取BarcodeTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

类型说明[_BarcodeTag](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__barcodetag18)提供对条形码标签的属性和I/O操作的访问。

#### NdefMessage9+

type NdefMessage = _NdefMessage

获取NdefMessage。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_NdefMessage](nfctech (标准NFC-Tag Nfc 技术).md#ZH-CN_TOPIC_0000002497605426__ndefmessage9)获取NDEF消息中的所有记录。

#### TagSession7+

type TagSession = _TagSession

获取TagSession。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

类型说明[_TagSession](tagSession (标准NFC-Tag TagSession).md#ZH-CN_TOPIC_0000002497445448__tagsession)TagSession是所有[NFC Tag技术类型](nfctech (标准NFC-Tag Nfc 技术).md)的基类， 提供建立连接和发送数据等共同接口。