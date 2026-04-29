# thirdPaymentService(三方支付服务)

本模块提供直接通过依赖包拉起第三方支付方式收银台能力。

起始版本： 6.0.0(20)

**导入模块**

```ets
import { thirdPaymentService } from '@kit.PaymentKit';
```

**PayMethod**

三方支付方式。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.ThirdPaymentService

起始版本： 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WECHAT_PAY | wechat_pay | 微信支付。 |
| ALI_PAY | ali_pay | 支付宝支付。 |
| WECHAT_MINI_PROGRAM | wechat_mini_program | 拉起微信小程序。 |

**ThirdPayClient**

支付请求客户端。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.ThirdPaymentService

起始版本： 6.0.0(20)

**constructor**

constructor(context: common.UIAbilityContext, payMethod: PayMethod, thirdAppId: string);

构造器，构造三方支付等请求客户端ThirdPayClient实例。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.ThirdPaymentService

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext | 是 | UIAbility上下文。 |
| payMethod | PayMethod | 是 | 支付方式。 |
| thirdAppId | string | 是 | 三方支付应用appID。 |

示例：

```ets
import { thirdPaymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  thirdPayClient = new thirdPaymentService.ThirdPayClient(this.getUIContext().getHostContext() as common.UIAbilityContext, thirdPaymentService.PayMethod.WECHAT_PAY, "third_appid_123456");

  build() { }
}
```

**pay**

pay(payInfo: string): Promise<void>;

该方法提供拉起三方支付方式收银台等功能，调用方法前请确保网络已连接，调用该方法后会拉起三方支付收银台，完成后使用Promise异步返回。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.ThirdPaymentService

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| payInfo | string | 是 | 拉起收银台传入的订单信息，payInfo是json字符串的格式（具体参数根据三方支付方式拉起收银台要求传递，参考payInfo）。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022830000 | The operation was canceled by the user. |
| 1022830001 | Pay failed. |
| 1022830002 | The payInfo invalid. Possible causes: 1.Data format is not json string; 2.Mandatory parameters are left unspecified. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { thirdPaymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

export let thirdPayClient: thirdPaymentService.ThirdPayClient | undefined = undefined;

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  thirdPaymentServicePayPromise() {
    thirdPayClient = new thirdPaymentService.ThirdPayClient(this.context, thirdPaymentService.PayMethod.WECHAT_PAY, "appid_123456");
    // 不同支付方式参数构建参考示例如下：
    // PayMethod.WECHAT_PAY：'{"appId":"***","partnerId":"***","prepayId":"***","packageValue":"***","nonceStr":"***","timeStamp":"***","sign":"***","extData":"***","token":"***"}'
    // PayMethod.ALI_PAY：'{"orderInfo":"***", "token":"***"}'
    // PayMethod.WECHAT_MINI_PROGRAM：'{"userName":"原始id", "path":"小程序启动路径", "miniProgramType":"小程序的类型，0-正式版 1-开发版 2-体验版 默认0", "extData":"***", "token":"***"}'
    const payInfo = '{"xxx1":"***", "xxx2":"***", "token":"***"}';
    thirdPayClient.pay(payInfo).then(() => {
        // succeeded in paying
        console.info('succeeded in paying.');
      }).catch((error: BusinessError) => {
        // failed to pay
        console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('thirdPaymentServicePayPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.thirdPaymentServicePayPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
```

**handlePayCallback**

handlePayCallback(want: Want): boolean;

该方法提供处理支付处理结果回调功能，调用方法前请确保网络已连接，请求处理完成后使用返回布尔类型结果。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.ThirdPaymentService

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | common.Want | 是 | 应用组件间的信息传递的载体。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 回调处理结果（该结果为用户支付操作处理结果，非实际支付结果，实际支付结果以三方支付结果为准）。 - true：用户支付操作成功 - false：用户支付操作失败 |

示例：

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIAbility, Want } from '@kit.AbilityKit';
// 需要从thirdPayClient对象定义的代码文件中导入三方支付客户端对象，以下为示例，具体以应用定义路径为准。
import { thirdPayClient } from '../pages/thirdPaymentServicetest';

// 如果已有Ability实现类，可直接添加onNewWant生命周期方法处理即可。
export default class EntryAbility extends UIAbility {
  onNewWant(want: Want): void {
    // 需要和拉起支付收银台的三方支付客户端对象为同一个
    if (thirdPayClient) {
      hilog.info(0x0000, 'testTag', '%{public}s','clientForThirdPayment handlePayCallback');
      let handlePayCallback = thirdPayClient.handlePayCallback(want);
      hilog.info(0x0000, 'testTag', 'clientForThirdPayment handlePayCallback result: %{public}s', handlePayCallback);
    }
```