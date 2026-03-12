# attributionTestManager（应用归因接入调试功能）

提供验证归因来源、设置归因结果回传、触发归因结果回传调试功能。

调用接口需捕获异常。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { attributionTestManager } from '@kit.AppGalleryKit';
```

#### attributionTestManager.validateSource

validateSource(adSourceInfo: AdSourceInfo, publicKey: string): Promise<void>

验证媒体App/分发平台登记的归因来源信息，通过Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

adSourceInfo

[AdSourceInfo](#section1262013338292)

是

媒体app/分发平台登记的归因来源信息。

publicKey

string

是

已[生成密钥对](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-register#section1810151768)中的公钥。注册归因角色时提供给应用归因服务云侧的公钥。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1009300001

The specified service extension connect failed.

1009300002

System internal error.

1009300101

AdTechId is missing in the request.

1009300102

CampaignId is missing in the request.

1009300104

DestinationId is missing in the request.

1009300105

SourceType is missing in the request.

1009300106

Nonce is missing in the request.

1009300107

Timestamp is missing in the request.

1009300108

Signature is missing in the request.

1009300111

AdSourceInfo is missing in the request.

1009300112

PublicKey is missing in the request.

1009300114

The signature verification failed in the testing environment.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionTestManager } from '@kit.AppGalleryKit';
import { SignUtil } from '../common/utils/SignUtil'; //参考指南附录[生成签名方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-attribution-appendix-triger#section5203225132112)部分代码
import { util } from '@kit.ArkTS';
import { deviceInfo } from '@kit.BasicServicesKit';

const TAG: string = 'AttributionTest';

class  AttributionTest {

  async validateSource(): Promise<void> {
    try {
      // 使用在应用归因服务云侧注册角色时，提供的公钥和对应的私钥, 验证接口， 用户可自己生成
      let privateKey: string = '';
      let publicKey: string = '';
      // 在应用归因云侧注册广告生态伙伴角色时，由应用归因服务分配
      let adTechId: string = '12345678';
      // 分发平台创建的营销任务id
      let campaignId: string = '';
      let osApiVersion: number = deviceInfo.sdkApiVersion;
      if (osApiVersion >= 22) {
        campaignId = '1*******9';
      } else {
        campaignId = '1****6';
      }
      // 开发者应用上架华为应用市场的appId，不带C
      let destinationId: string = '102345678';
      // 归因监测平台id
      let mmpIds: string[] = ['12345678', '23456789'];
      // 分发平台关注的业务信息
      let serviceTag: string = 'testServiceTag';
      // 用于计算签名的随机数，不带'-'
      let nonce: string = util.generateRandomUUID().replace(/-/g, '');
      // 时间戳
      let timestamp: number = Date.now()
      let adSourceInfo: attributionTestManager.AdSourceInfo = {
        adTechId: adTechId,
        campaignId: campaignId,
        destinationId: destinationId,
        // 归因来源类型：曝光
        sourceType: attributionTestManager.SourceType.IMPRESSION,
        mmpIds: mmpIds,
        serviceTag: serviceTag,
        nonce: nonce,
        timestamp: timestamp,
        // 签名值
        signature: await SignUtil.getSign(SignUtil.genSignContent(adTechId, campaignId, destinationId, mmpIds, serviceTag, nonce, timestamp), privateKey)
      };

      await attributionTestManager.validateSource(adSourceInfo, publicKey);
      hilog.info(0, TAG, 'Succeeded in validating source.');
    } catch (error) {
      hilog.error(0, TAG, `validateSource error.code is ${error.code}, message is ${error.message}`);
    }
  }
}
```

#### attributionTestManager.setPostback

setPostback(postbackInfo: PostbackInfo): Promise<void>

设置归因结果回传信息。用于验证triggerData的合法性，设置调试使用的归因结果回传信息，通过Promise异步回调。

单个adTechId下，待回传的调试postbackInfo数据量<=5。

单个设备下，待回传的调试postbackInfo数据量<=100。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

postbackInfo

[PostbackInfo](#section1812319373298)

是

归因结果回传信息。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1009300001

The specified service extension connect failed.

1009300002

System internal error.

1009300101

AdTechId is missing in the request.

1009300102

CampaignId is missing in the request.

1009300103

SourceId is missing in the request.

1009300104

DestinationId is missing in the request.

1009300109

TriggerData is missing in the request.

1009300110

PostbackUrl is missing in the request.

1009300113

PostbackInfo is missing in the request.

1009300115

Too many postbacks setting to the testing environment.

**示例**：

```ets
import { BusinessError,deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionTestManager } from '@kit.AppGalleryKit';

const TAG: string = 'AttributionTest';

class AttributionTest {

  setPostback(): void {
    try {
      let postbackInfo: attributionTestManager.PostbackInfo = {
        adTechId: '12345678',
        campaignId: ' ',
        sourceId: '112345678',
        destinationId: '102345678',
        serviceTag: 'testServiceTag',
        businessScene: 5,
        triggerData: 123,
        postbackUrl: 'https://xxx.com'
      };
      let osApiVersion: number = deviceInfo.sdkApiVersion;
      if (osApiVersion >= 22) {
        postbackInfo.campaignId = '1*******9';
      } else {
        postbackInfo.campaignId = '1****6';
      }
      attributionTestManager.setPostback(postbackInfo).then(() => {
        hilog.info(0, TAG, 'Succeeded in setting postback.');
      }).catch((error: BusinessError) => {
        hilog.error(0, TAG, `setPostback onError.code is ${error.code}, message is ${error.message}`);
      })
    } catch (error) {
      hilog.error(0, TAG, `setPostback onError.code is ${error.code}, message is ${error.message}`);
    }
  }
}
```

#### attributionTestManager.flushPostbacks

flushPostbacks(adTechId: string): Promise<void>

触发归因结果回传。验证开发者服务器接收及处理归因回传结果的逻辑是否正确，通过Promise异步回调。

单个设备上，每5秒调用次数<=1。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

adTechId

string

是

分发平台对应的归因角色ID，本次登记归因来源对应营销任务所归属的分发平台的标识符，长度固定为8字符。

使用setPostback()接口中成功设置的adTechId值。

 说明：

调试过程不依赖云侧注册，开发者可以使用虚拟的adTechId。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1009300001

The specified service extension connect failed.

1009300002

System internal error.

1009300101

AdTechId is missing in the request.

1009300116

There is no postback to be sent of this adTechId.

1009300117

Failed to send postbacks to the postbackUrl.

1009300119

Network error.

1009300120

Request too frequent.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionTestManager } from '@kit.AppGalleryKit';

const TAG: string = 'AttributionTest';

class AttributionTest {
  flushPostbacks(): void {
    try {
      let adTechId: string = '12345678';
      attributionTestManager.flushPostbacks(adTechId).then(() => {
        hilog.info(0, TAG, 'Succeeded in flushing postbacks.');
      }).catch((error: BusinessError) => {
        hilog.error(0, TAG, `flushPostbacks onError.code is ${error.code}, message is ${error.message}`);
      })
    } catch (error) {
      hilog.error(0, TAG, `flushPostbacks onError.code is ${error.code}, message is ${error.message}`);
    }
  }
}
```

#### AdSourceInfo

媒体app/分发平台登记的归因来源信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

adTechId

string

否

否

分发平台对应的归因角色ID，本次登记归因来源对应营销任务所归属的分发平台的标识符。

分发平台向应用归因云侧[注册归因角色](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-register#section11218192952612)时，由应用归因服务分配，长度固定为8字符。

 说明：

调试过程不依赖云侧注册，开发者可以使用虚拟的adTechId。

campaignId

string

否

否

营销任务ID，登记归因来源对应的营销任务的ID，长度不超过6字符。

 说明：

从6.0.2(22)开始，该接口支持长度由不超过6字符变为不超过9字符。

destinationId

string

否

否

开发者应用上架华为应用市场的AppId，长度不超过64字符。

 说明：

您的应用ID参考[查看应用基本信息](https://developer.huawei.com/consumer/cn/doc/app/agc-help-appinfo-0000001100014694)获取。

sourceType

[SourceType](#section142399205014)

否

否

归因来源类型：

0：曝光。

1：点击。

mmpIds

string[]

否

是

本次广告投放，使用的归因监测平台对应的归因角色ID。最大数量2个，每个ID字符串长度固定为8字符。

如果调用方传递了归因监测平台ID，应用归因服务会向归因监测平台回传归因结果；如果调用方没有传递归因监测平台ID，则归因监测平台收不到回传的归因结果。

serviceTag

string

否

是

分发平台关注的业务信息，如创意、素材等，长度不超过32字符。

如果调用方传递了serviceTag，应用归因服务通过白名单方式向分发平台开放（白名单开放方式请联系华为运营）；如果调用方没有传递serviceTag，则分发平台收不到回传的serviceTag。

nonce

string

否

否

用于计算签名的随机数，每次广告请求，nonce唯一。长度固定为32字符。

timestamp

number

否

否

请求广告的时间戳。（即广告投放时间，与当前时间偏差不超过10分钟）。unix时间戳，单位：毫秒。

signature

string

否

否

签名值，分发平台/媒体根据广告相应信息按照[归因来源签名计算规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-attribution-appendix-triger#section4208115642013)计算并提供，长度不超过800字符。

#### PostbackInfo

待回传数据信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

adTechId

string

否

否

分发平台对应的归因角色ID，本次登记归因来源对应营销任务所归属的分发平台的标识符。

使用setPostback()接口中成功设置的adTechId值。

 说明：

调试过程不依赖云侧注册，开发者可以使用虚拟的adTechId。

campaignId

string

否

否

营销任务ID，登记归因来源对应的营销任务的ID，长度不超过6个字符。

 说明：

从6.0.2(22)开始，该接口支持长度由不超过6字符变为不超过9字符。

sourceId

string

否

否

媒体应用id，长度不超过64个字符。

destinationId

string

否

否

开发者应用上架华为应用市场的AppId，长度不超过64个字符。

serviceTag

string

否

是

分发平台关注的业务信息，如创意、素材等，长度不超过32字符。

如果调用方传递了serviceTag，应用归因服务会向分发平台回传serviceTag；如果调用方没有传递serviceTag，则分发平台收不到回传的serviceTag。

businessScene

number

否

是

业务场景值，在开发者登记转化时，用于标识开发者的业务场景。

取值范围：[0,99]。

triggerData

number

否

否

转化事件编码。

取值范围：[0,999]。

postbackUrl

string

否

否

用于接收归因回传归因结果的URL地址，推荐使用HTTPS协议。

#### SourceType

归因来源类型的枚举。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

名称

值

说明

IMPRESSION

0

归因来源类型：曝光。

CLICK

1

归因来源类型：点击。