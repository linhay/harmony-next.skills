# @ohos.advertising.AutoAdComponent (轮播广告展示组件)

本模块提供展示轮播广告的能力。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { AutoAdComponent } from '@kit.AdsKit';
```

#### AutoAdComponent

```ets
AutoAdComponent({
  adParam: advertising.AdRequestParams,
  adOptions: advertising.AdOptions,
  displayOptions: advertising.AdDisplayOptions,
  interactionListener: advertising.AdInteractionListener
})
```

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

**参数名**

**类型**

必填

**装饰器类型**

说明

adParam

advertising.[AdRequestParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#adrequestparams)

是

-

广告请求参数。

adOptions

advertising.[AdOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#adoptions)

是

-

广告配置参数。

displayOptions

advertising.[AdDisplayOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#addisplayoptions)

是

-

广告展示参数。

interactionListener

advertising.[AdInteractionListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#adinteractionlistener)

是

-

广告状态变化回调。

**示例：**

```ets
import { advertising, AutoAdComponent } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // 广告请求参数
  private adRequestParams: advertising.AdRequestParams = {
    // 广告位ID
    adId: 'testw6vs28auh3',
    // 广告类型
    adType: 8
  };
  // 广告配置参数
  private adOptions: advertising.AdOptions = {};
  // 广告展示参数
  private adDisplayOptions: advertising.AdDisplayOptions = {
    // 广告轮播的时间间隔，单位ms，取值范围[30000, 120000]
    refreshTime: 30000
  };

  build() {
    Column() {
      AutoAdComponent({
        adParam: this.adRequestParams,
        adOptions: this.adOptions,
        displayOptions: this.adDisplayOptions,
        interactionListener: {
          onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
            switch (status) {
              case 'onAdOpen':
                hilog.info(0x0000, 'testTag', 'onAdOpen');
                break;
              case 'onAdClick':
                hilog.info(0x0000, 'testTag', 'onAdClick');
                break;
              case 'onAdClose':
                hilog.info(0x0000, 'testTag', 'onAdClose');
                break;
            }
          }
        }
      })
        .width('100%')
        .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```

#### build

build(): void

用于创建AutoAdComponent对象的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads