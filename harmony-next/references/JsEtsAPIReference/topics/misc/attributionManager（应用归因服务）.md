# attributionManager（应用归因服务）

为媒体/分发平台提供向应用归因服务登记归因来源、开发者/归因监测平台向应用归因服务登记转化事件功能。

调用接口需捕获异常。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { attributionManager } from '@kit.AppGalleryKit';
```

#### AdSourceInfo

媒体/分发平台登记的归因来源信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| adTechId | string | 否 | 否 | 分发平台对应的归因角色ID，本次登记归因来源对应营销任务所归属的分发平台的标识符。 分发平台向应用归因云侧注册归因角色时，由应用归因服务分配，长度固定为8个字符。 |
| campaignId | string | 否 | 否 | 营销任务ID，登记归因来源对应的营销任务的ID，长度不超过6个字符。 说明： 从6.0.2(22)开始，该接口支持长度由不超过6个字符变为不超过9个字符。 |
| destinationId | string | 否 | 否 | 开发者应用上架华为应用市场的AppId，长度不超过64个字符。 说明： 您的应用ID参考查看应用基本信息获取。 |
| sourceType | SourceType | 否 | 否 | 归因来源类型： 0：曝光。 1：点击。 |
| mmpIds | string[] | 否 | 是 | 本次广告投放，使用的归因监测平台对应的归因角色ID。最大数量2个，每个ID字符串长度固定为8字符。 如果调用方传递了归因监测平台ID，应用归因服务会向归因监测平台回传归因结果；如果调用方没有传递归因监测平台ID，则归因监测平台收不到回传的归因结果。 |
| serviceTag | string | 否 | 是 | 分发平台关注的业务信息，如创意、素材等，长度不超过32个字符。 如果调用方传递了serviceTag，在申请开通权限后应用归因服务会将serviceTag回传分发平台。 |
| nonce | string | 否 | 否 | 用于计算签名的随机数，每次广告请求，nonce唯一。长度固定为32个字符。 同一个adTechId下，同一个nonce最多可以登记5次曝光，5次点击类型的归因来源信息。 |
| timestamp | number | 否 | 否 | 请求广告的时间戳（即广告投放时间，登记归因来源时，要求广告时间与当前时间偏差不超过10分钟）。unix时间戳，单位：毫秒 |
| signature | string | 否 | 否 | 签名值，分发平台/媒体根据广告相应信息按照归因来源签名计算规则计算生成签名并提供，长度不超过800个字符。 |

#### AdTriggerInfo

开发者登记的转化事件信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| businessScene | number | 否 | 是 | 业务场景值，在开发者登记转化时，用于标识开发者的业务场景。 取值范围：[0,99]。 |
| triggerData | number | 否 | 否 | 转化事件编码。 标准转化事件取值范围：[1, 200]。 自定义转化事件取值范围：[501, 600]。 |
| timestamp | number | 否 | 是 | 转化事件发生时间（要求登记转化事件接口调用时间与转化事件发生时间的间隔默认不超过10分钟）。unix时间戳，单位：毫秒。 起始版本： 6.0.2(22) |
| serviceTag | string | 否 | 是 | 开发者关注的业务信息，长度不超过32个字符。 如果调用方传递了serviceTag，在申请开通权限后应用归因服务会将serviceTag回传分发平台。 起始版本： 6.0.2(22) |

#### SourceType

归因来源类型的枚举。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMPRESSION | 0 | 归因来源类型：曝光。 |
| CLICK | 1 | 归因来源类型：点击。 |

#### attributionManager.registerSource

registerSource(adSourceInfo: AdSourceInfo): Promise<void>

登记归因来源接口，由媒体/分发平台接入注册。通过Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adSourceInfo | AdSourceInfo | 是 | 媒体/分发平台登记归因来源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码]([ArkTS API错误码](../../errors/ArkTS API错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1009300001 | The specified service extension connect failed. |
| 1009300002 | System internal error. |
| 1009300003 | The identity check error. |
| 1009300004 | The sign check error. |

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionManager } from '@kit.AppGalleryKit';
import { SignUtil } from '../common/utils/SignUtil';  //参考指南附录生成签名方法部分代码
import { util } from '@kit.ArkTS';
import { BusinessError,deviceInfo } from '@kit.BasicServicesKit';

const TAG: string = 'Attribution';

class  Attribution {
  async registerSource(): Promise<void> {
    try {
      // 使用在应用归因服务云侧注册角色时，提供的公钥所对应的私钥
      let privateKey: string =" ";
      // 在应用归因云侧注册广告生态伙伴角色时，由应用归因服务分配
      let adTechId: string = '20****8';
      // 分发平台创建的营销任务id，6.0.2(22)之前支持长度不超过6个字符，6.0.2(22)及以上支持长度不超过9个字符
      let campaignId: string = '';
      let osApiVersion: number = deviceInfo.sdkApiVersion;
      if (osApiVersion >= 22) {
        campaignId = '1*******9';
      } else {
        campaignId = '1****6';
      }
      // 开发者应用上架华为应用市场的appId，不带C
      let destinationId: string = '691****4';
      // 归因监测平台id
      let mmpIds: string[] = ['2f76e815'];
      // 分发平台关注的业务信息
      let serviceTag: string = 'testServiceTag';
      // 用于计算签名的随机数，不带'-'
      let nonce: string = util.generateRandomUUID().replace(/-/g, '');
      // 时间戳
      let timestamp: number = Date.now()
      let adSourceInfo: attributionManager.AdSourceInfo = {
        adTechId: adTechId,
        campaignId: campaignId,
        destinationId: destinationId,
        // 归因来源类型：曝光
        sourceType: attributionManager.SourceType.IMPRESSION,
        mmpIds: mmpIds,
        serviceTag: serviceTag,
        nonce: nonce,
        timestamp: timestamp,
        // 签名值
        signature: await SignUtil.getSign(SignUtil.genSignContent(adTechId, campaignId, destinationId, mmpIds, serviceTag, nonce, timestamp), privateKey)
      };

      attributionManager.registerSource(adSourceInfo).then(() => {
        hilog.info(0, TAG, 'Succeeded in registering source.');
      }).catch((error: BusinessError) => {
        hilog.error(0, TAG, `registerSource error.code is ${error.code}, message is ${error.message}`);
      })
    } catch (error) {
      hilog.error(0, TAG, `registerSource error.code is ${error.code}, message is ${error.message}`);
    }
```

#### attributionManager.registerTrigger

registerTrigger(adTriggerInfo: AdTriggerInfo): Promise<void>

登记转化接口，由开发者接入注册。通过Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.AttributionManager

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adTriggerInfo | AdTriggerInfo | 是 | 转化事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1009300001 | The specified service extension connect failed. |
| 1009300002 | System internal error. |
| 1009300003 | The identity check error. |

**示例：**

```ets
import { BusinessError,deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionManager } from '@kit.AppGalleryKit';

const TAG: string = 'Attribution';

class Attribution {
  registerTrigger(): void {
    try {
      let adTriggerInfo: attributionManager.AdTriggerInfo = {
        businessScene: 5,
        // 转化事件编码，从应用归因云端管理平台获取
        triggerData: 123,

      };
      let osApiVersion: number = deviceInfo.sdkApiVersion;
      if (osApiVersion >= 22) {
        // 从6.0.2（22）开始， 增加事件转化时间
        adTriggerInfo.timestamp = Date.now();
        adTriggerInfo.serviceTag = 'testServiceTag';
      };

      attributionManager.registerTrigger(adTriggerInfo).then(() => {
        hilog.info(0, TAG, 'Succeeded in registering triggerdata.');
      }).catch((error: BusinessError) => {
        hilog.error(0, TAG, `registerTrigger error.code is ${error.code}, message is ${error.message}`);
      })
    } catch (error) {
      hilog.error(0, TAG, `registerTrigger error.code is ${error.code}, message is ${error.message}`);
    }
```