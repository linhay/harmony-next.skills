# @ohos.telephony.esim (eSIM卡管理)

eSIM卡管理模块提供了eSIM卡管理的基础能力，包括获取指定卡槽是否支持eSIM功能，如果支持则允许用户添加单个配置文件。

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { eSIM } from '@kit.TelephonyKit';
```

#### eSIM.isSupported

isSupported(slotId: number): boolean

获取指定卡槽是否支持eSIM功能。

**系统能力**：SystemCapability.Telephony.CoreService.Esim

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明boolean返回指定卡槽是否支持eSIM功能，如果支持返回true。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401Invalid parameter value.3120001Service connection failed.3120002System internal error.

**示例：**

```ets
import { eSIM } from '@kit.TelephonyKit';

let isSupported: boolean = eSIM.isSupported(1);
console.info(`the esim is Supported:` + isSupported);
```

#### eSIM.addProfile

addProfile(profile: DownloadableProfile): Promise<boolean>

通过该接口拉起下载界面，允许用户添加单个配置文件。使用Promise异步回调。

**需要权限**：ohos.permission.SET_TELEPHONY_ESIM_STATE_OPEN

**系统能力**：SystemCapability.Telephony.CoreService.Esim

**参数：**

参数名类型必填说明profile[DownloadableProfile](#ZH-CN_TOPIC_0000002497605490__downloadableprofile)是可下载的配置文件信息。

**返回值：**

类型说明Promise<boolean>以Promise形式返回最终用户添加单个配置文件的结果。返回true为成功，false为失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter value.801Capability not supported.3120001Service connection failed.3120002System internal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

let profile: eSIM.DownloadableProfile = {
  activationCode:'1',
  confirmationCode:'1',
  carrierName:'test',
  accessRules:[{
    certificateHashHexStr:'test',
    packageName:'com.example.testcoreservice',
    accessType:0
  }]
};

eSIM.addProfile(profile).then(() => {
    console.info(`addProfile invoking succeeded.`);
}).catch((err: BusinessError<void>) => {
    console.error(`addProfile, promise: err->${JSON.stringify(err)}`);
});
```

#### DownloadableProfile

可下载的配置文件。

**系统能力**：SystemCapability.Telephony.CoreService.Esim

名称类型只读可选说明activationCodestring否否激活码。对于不基于激活码的配置文件，可能为空。confirmationCodestring否是确认码。carrierNamestring否是订阅名称。accessRulesArray<[AccessRule](#ZH-CN_TOPIC_0000002497605490__accessrule20)>否是访问规则数组。

#### AccessRule20+

访问规则。

**系统能力**：SystemCapability.Telephony.CoreService.Esim

名称类型只读可选说明certificateHashHexStrstring否否证书哈希的十六进制字符串。packageNamestring否否规则适用的程序包名称。accessTypenumber否否规则的类型。