# sceneManager （生态查询服务）

对场景值进行管理，提供查询自身场景值，获取广告验签版本功能。

调用接口需捕获异常。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { sceneManager } from '@kit.AppGalleryKit';
```

#### sceneManager.getSelfSceneCode

getSelfSceneCode(): string

查询自身场景值。调用此接口需捕获异常。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.BundleManager.EcologicalRuleManager.SceneManager

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

string

自身场景值。

**示例：**

```ets
import { sceneManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const selfSceneCode: string = sceneManager.getSelfSceneCode();
  hilog.info(0, 'TAG', "Succeeded in getting SelfSceneCode res = " + selfSceneCode);
} catch (err) {
  hilog.error(0, 'TAG', `get self sceneCode failed.code is ${err.code}, message is ${err.message}`);
}
```

#### sceneManager.getAdsVerificationVersion

getAdsVerificationVersion(): number

获取广告验签版本。调用此接口需捕获异常。

**系统能力：**SystemCapability.BundleManager.EcologicalRuleManager.SceneManager

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

number

广告验签版本。当前返回值为1。

广告场景中开发者需要在want参数中携带以下参数：ohos.market.param.signature、ohos.market.param.ad_networkid、ohos.market.param.timestamp、ohos.market.param.verify_version、ohos.market.param.ad_nonce，验签时会根据want中这些字段值使用公钥进行验签。

**示例：**

```ets
import { sceneManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const version: number = sceneManager.getAdsVerificationVersion();
  hilog.info(0, 'TAG', "Succeeded in getting AdsVerificationVersion res = " + version);
} catch (err) {
  hilog.error(0, 'TAG', `get ads verification version failed.code is ${err.code}, message is ${err.message}`);
}
```