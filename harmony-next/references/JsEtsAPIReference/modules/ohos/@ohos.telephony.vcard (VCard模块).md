# @ohos.telephony.vcard (VCard模块)

VCard是电子名片的文件格式标准，它可包含的信息有：姓名、地址资讯、电话号码、URL、logo、相片等。VCard模块提供了VCard能力，包括将VCard文件导入联系人数据库和将联系人数据导出为VCard文件等。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**导入模块**

```ets
import { vcard } from '@kit.TelephonyKit';
```

**vcard.importVCard**

importVCard(context: Context, filePath: string, accountId: number, callback: AsyncCallback<void>): void

将VCard文件导入联系人数据库。使用callback异步回调。

需要权限：ohos.permission.WRITE_CONTACTS 和 ohos.permission.READ_CONTACTS

系统能力：SystemCapability.Telephony.CoreService

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 |
| filePath | string | 是 | VCF(vcard file)文件地址。 |
| accountId | number | 是 | 联系人账户ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数，返回导入成功或失败的状态码。 |

错误码：

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

示例：

```ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let filePath: string = "/data/storage/vcf/contacts.vcf";
        let accountId: number = 0;
        vcard.importVCard(this.context, filePath, accountId, (err: BusinessError) => {
            console.error(`callback: err->${JSON.stringify(err)}`);
        });
    }
```

**vcard.importVCard**

importVCard(context: Context, filePath: string, accountId?: number): Promise<void>

将VCard文件导入联系人数据库。使用Promise异步回调。

需要权限：ohos.permission.WRITE_CONTACTS 和 ohos.permission.READ_CONTACTS

系统能力：SystemCapability.Telephony.CoreService

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 |
| filePath | string | 是 | VCF(vcard file)文件地址。 |
| accountId | number | 否 | 联系人账户ID。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回重置的结果码。 |

错误码：

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

示例：

```ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let filePath: string = "/data/storage/vcf/contacts.vcf";
        let accountId: number = 0;
        vcard.importVCard(this.context, filePath, accountId).then(() => {
            console.info(`importVCard success.`);
        }).catch((err: BusinessError) => {
            console.error(`importVCard failed, promise: err->${JSON.stringify(err)}`);
        });
    }
```

**vcard.importVCard**

importVCard(context: Context, filePath: string, callback: AsyncCallback<void>): void

将VCard文件导入联系人数据库。使用callback异步回调。

需要权限：ohos.permission.WRITE_CONTACTS 和 ohos.permission.READ_CONTACTS

系统能力：SystemCapability.Telephony.CoreService

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 |
| filePath | string | 是 | VCF(vcard file)文件地址。 |
| callback | AsyncCallback<void> | 是 | 回调函数，返回导入成功或失败的状态码。 |

错误码：

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

示例：

```ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let filePath: string = "/data/storage/vcf/contacts.vcf";
        vcard.importVCard(this.context, filePath, (err: BusinessError) => {
            console.error(`callback: err->${JSON.stringify(err)}`);
        });
    }
```

**vcard.exportVCard**

exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options: VCardBuliderOptions, callback: AsyncCallback<string>): void

将联系人导出为 VCF(vcard file)文件。使用callback异步回调。

需要权限：ohos.permission.WRITE_CONTACTS 和 ohos.permission.READ_CONTACTS

系统能力：SystemCapability.Telephony.CoreService

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 |
| predicates | dataSharePredicates.DataSharePredicates | 是 | 查询语句。 |
| options | VCardBuilderOptions | 是 | VCard版本与编码类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。生成的 VCF(vcard file)文件地址。 |

错误码：

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

示例：

```ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';
import { dataSharePredicates } from '@kit.ArkData';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let predicates = new dataSharePredicates.DataSharePredicates();
        predicates.equalTo("NAME", "Rose");
        let options: vcard.VCardBuilderOptions = {
            cardType: vcard.VCardType.VERSION_21,
            charset: "UTF-8"
        };
        vcard.exportVCard(this.context, predicates, options, (err: BusinessError, data: string) => {
            console.error(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
        });
    }
```

**vcard.exportVCard**

exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options?: VCardBuilderOptions): Promise<string>

将联系人导出为 VCF(vcard file)文件。使用Promise异步回调。

需要权限：ohos.permission.WRITE_CONTACTS 和 ohos.permission.READ_CONTACTS

系统能力：SystemCapability.Telephony.CoreService

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 |
| predicates | dataSharePredicates.DataSharePredicates | 是 | 查询语句。 |
| options | VCardBuilderOptions | 否 | VCard版本与编码类型。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回重置的结果码。 |

错误码：

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

示例：

```ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';
import { dataSharePredicates } from '@kit.ArkData';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let predicates = new dataSharePredicates.DataSharePredicates();
        predicates.equalTo("NAME", "Rose");
        let options: vcard.VCardBuilderOptions = {
            cardType: vcard.VCardType.VERSION_21,
            charset: "UTF-8"
        };
        vcard.exportVCard(this.context, predicates, options).then(() => {
            console.info(`exportVCard success.`);
        }).catch((err: BusinessError) => {
            console.error(`exportVCard failed, promise: err->${JSON.stringify(err)}`);
        });
    }
```

**vcard.exportVCard**

exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<string>): void

将联系人导出为 VCF(vcard file)文件。使用callback异步回调。

需要权限：ohos.permission.WRITE_CONTACTS 和 ohos.permission.READ_CONTACTS

系统能力：SystemCapability.Telephony.CoreService

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 |
| predicates | dataSharePredicates.DataSharePredicates | 是 | 查询语句。 |
| callback | AsyncCallback<string> | 是 | 回调函数。生成的 VCF(vcard file)文件地址。 |

错误码：

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

示例：

```ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';
import { dataSharePredicates } from '@kit.ArkData';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let predicates = new dataSharePredicates.DataSharePredicates();
        predicates.equalTo("NAME", "Rose");

        vcard.exportVCard(this.context, predicates, (err: BusinessError, data: string) => {
            console.error(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
        });
    }
```