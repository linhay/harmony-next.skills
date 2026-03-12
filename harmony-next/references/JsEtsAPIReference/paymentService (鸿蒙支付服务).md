# paymentService (鸿蒙支付服务)

本模块提供支付、签约服务能力，包括基础支付、支付并签约、合单支付、签约代扣等。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { paymentService } from '@kit.PaymentKit';
```

#### PayResult

用户在通用收银台选择支付方式并确认支付后的支付信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**5.0.2(14)

**名称**

**类型**

只读

可选

**说明**

selectedPaymentType

string

否

是

用户选择的支付方式。

- wechat_pay：微信支付
- ali_pay：支付宝支付

- 其他（其他为商户申请配置三方支付方式时所申请的三方支付相关配置）

clientToken

string

否

是

客户端凭证。

nextStep

string

否

是

下一步支付流程。

[extraInfo](数据模型说明.md#section151931211104318)

string

否

是

保留字段。json string格式。

[payload](数据模型说明.md#section17853161714224)

string

否

是

预留信息，在请求接口时，入参如果传递，接口响应中则会原样返回。

 说明：

拉起H5支付场景下需要固定传递“AP”。

#### PaymentInfo

三方支付拉起通用收银台时传入的支付订单信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**5.0.2(14)

**名称**

**类型**

只读

可选

**说明**

tradeSummary

string

否

是

订单的摘要信息。若未填写，默认为空。

amount

number

否

是

订单总金额（单位：分）。

currency

string

否

是

货币单位。若未填写，默认为空。

 说明：

- 不传递则收银台不显示货币单位。
- 传递后收银台可以转换成货币符号则显示货币符号（比如￥），转换不了则显示所传递的值。

[extraInfo](数据模型说明.md#section151931211104318)

string

否

是

保留字段。json string格式。若未填写，默认为空。

 说明：  商户可以通过保留字段指定支付方式。指定收银台支付方式列表传递内容示例如下：

```ets
{"selectPayType":"wechat_pay|xxx"}
```

#### PickerResult

三方支付拉起通用收银台时响应给开发者的订单支付信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**5.0.2(14)

**名称**

**类型**

只读

可选

**说明**

selectedPaymentType

string

否

是

用户选择的支付方式。

- wechat_pay：微信支付
- ali_pay：支付宝支付
- 其他（其他为商户申请配置三方支付方式时所申请的相关配置）

clientToken

string

否

是

客户端凭证。

#### BindCardResult

绑卡结果信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.5(17)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**5.0.5(17)

**名称**

**类型**

只读

可选

**说明**

hasBankCard

boolean

否

否

用户当前是否有已绑定的银行卡。

- true：是
- false：否

hasJustBoundCard

boolean

否

是

用户在拉起绑卡管理页面后是否完成了绑卡。

- true：是
- false：否

#### paymentService.requestPayment

requestPayment(context: common.UIAbilityContext, orderStr: string): Promise<void>

该方法提供基础支付、支付并签约等功能，调用方法前请确保网络已连接，调用该方法后会拉起Payment Kit收银台，支付完成后使用Promise异步返回。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**4.1.0(11)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

UIAbility上下文，不传会报401参数错误。

[orderStr](数据模型说明.md#section159202591414)

string

是

拉起收银台传入的订单信息，[orderStr](数据模型说明.md#section159202591414)是json字符串的格式。不传会报401参数错误。

**返回值**:

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

401

Parameter error.

1001930000

The operation was canceled by the user.

1001930001

Pay failed.

1001930002

The transaction has been processed.

1001930010

Duplicate request.

1001930011

Network connection error.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestPaymentPromise() {
    // use your own orderStr
    const orderStr = '{"app_id":"***","merc_no":"***","prepay_id":"xxx","timestamp":"1680259863114","noncestr":"1487b8a60ed9f9ecc0ba759fbec23f4f","sign":"****","auth_id":"***"}';
    paymentService.requestPayment(this.context, orderStr)
      .then(() => {
        // succeeded in paying
        console.info('succeeded in paying');
      })
      .catch((error: BusinessError) => {
        // failed to pay
        console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestPaymentPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestPaymentPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### paymentService.requestPayment

requestPayment(context: common.UIAbilityContext, orderStr: string, callback: AsyncCallback<void>): void

该方法提供基础支付、支付并签约等功能，调用该方法前请确保网络已连接，调用该方法后会拉起Payment Kit收银台，支付完成后通过AsyncCallback回调结果。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**4.1.0(11)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

UIAbility上下文，不传会报401参数错误。

[orderStr](数据模型说明.md#section159202591414)

string

是

拉起收银台传入的订单信息，[orderStr](数据模型说明.md#section159202591414)是json字符串的格式。不传会报401参数错误。

callback

AsyncCallback<void>

是

回调函数。当支付成功，error为undefined，否则为错误对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

401

Parameter error.

1001930000

The operation was canceled by the user.

1001930001

Pay failed.

1001930002

The transaction has been processed.

1001930010

Duplicate request.

1001930011

Network connection error.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestPaymentCallBack() {
    // use your own orderStr
    const orderStr = '{"app_id":"***","merc_no":"***","prepay_id":"xxx","timestamp":"1680259863114","noncestr":"1487b8a60ed9f9ecc0ba759fbec23f4f","sign":"****","auth_id":"***"}';
    paymentService.requestPayment(this.context, orderStr, (error: BusinessError) => {
      if (error) {
        // failed to pay
        console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
        return;
      }
      // succeeded in paying
      console.info('succeeded in paying');
    })
  }

  build() {
    Column() {
      Button('requestPaymentCallBack')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestPaymentCallBack();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### paymentService.requestContract

requestContract(context: common.UIAbilityContext, contractStr: string): Promise<void>

该方法提供签约功能，调用方法前请确保网络已连接，调用该方法后会拉起Payment Kit签约收银台，签约完成后使用Promise异步返回。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

UIAbility上下文，不传会报401参数错误。

[contractStr](数据模型说明.md#section01944104716)

string

是

拉起签约收银台入参，[contractStr](数据模型说明.md#section01944104716)是json字符串的格式。不传会报401参数错误。

**返回值**:

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

401

Parameter error.

1001930000

The operation was canceled by the user.

1001930002

The transaction has been processed.

1001930003

Withhold failed.

1001930010

Duplicate request.

1001930011

Network connection error.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestContractPromise() {
    // use your own contractStr
    const contractStr = '{"appId":"***","preSignNo":"***"}';
    paymentService.requestContract(this.context, contractStr)
      .then(() => {
        // succeeded in signing
        console.info('succeeded in signing');
      })
      .catch((error: BusinessError) => {
        // failed to sign
        console.error(`failed to sign, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestContractPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestContractPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### paymentService.requestContract

requestContract(context: common.UIAbilityContext, contractStr: string, callback: AsyncCallback<void>): void

该方法提供签约功能，调用该方法前请确保网络已连接，调用该方法后会拉起Payment Kit签约收银台，签约完成后通过AsyncCallback回调结果。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

UIAbility上下文，不传会报401参数错误。

[contractStr](数据模型说明.md#section01944104716)

string

是

拉起签约收银台入参，[contractStr](数据模型说明.md#section01944104716)是json字符串的格式。不传会报401参数错误。

callback

AsyncCallback<void>

是

回调函数。当签约成功，error为undefined，否则为错误对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

401

Parameter error.

1001930000

The operation was canceled by the user.

1001930002

The transaction has been processed.

1001930003

Withhold failed.

1001930010

Duplicate request.

1001930011

Network connection error.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestContractCallBack() {
    // use your own contractStr
    const contractStr = '{"appId":"***","preSignNo":"***"}';
    paymentService.requestContract(this.context, contractStr, (error: BusinessError) => {
      if (error) {
        // failed to sign
        console.error(`failed to sign, error.code: ${error.code}, error.message: ${error.message}`);
        return;
      }
      // succeeded in signing
      console.info('succeeded in signing');
    })
  }

  build() {
    Column() {
      Button('requestContractCallBack')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestContractCallBack();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### paymentService.requestPayment

requestPayment(context: common.UIAbilityContext, orderStr: string, payload: string): Promise<PayResult>

该方法提供拉起通用收银台、跳转三方支付功能，调用方法前请确保网络已连接，用户在通用收银台选择支付方式并确认支付后，使用Promise异步返回。

**元服务API：**从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**5.0.2(14)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

UIAbility上下文，不传会报401参数错误。

[orderStr](数据模型说明.md#section159202591414)

string

是

拉起收银台或跳转三方支付传入的订单信息。

orderStr是json字符串的格式，不传会报401参数错误。

[payload](数据模型说明.md#section17853161714224)

string

是

预留信息，在请求接口时，入参如果传递，接口响应中则会原样返回。

 说明：

- 拉起华为支付收银台，需传空或空字符。H5支付场景下跳转三方支付收银台需要固定传递“AP”。

**返回值**:

类型

说明

Promise<[PayResult](#section363mcpsimp)>

Promise对象。带[PayResult](#section363mcpsimp)返回结果的Promise对象。

 说明：

华为支付场景下，[PayResult](#section363mcpsimp)可能返回为空，支付结果以回调通知或查询结果为准。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

401

Parameter error.

1001930000

The operation was canceled by the user.

1001930001

Pay failed.

1001930002

The transaction has been processed.

1001930010

Duplicate request.

1001930011

Network connection error.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestPaymentPromise() {
    // use orderStr to pay for an order, use your own orderStr.
    // const orderStr = '{"app_id":"***","merc_no":"***","prepay_id":"xxx","timestamp":"1680259863114","noncestr":"1487b8a60ed9f9ecc0ba759fbec23f4f","sign":"****","auth_id":"***"}';
    // use orderStr to jump third-party payment, use your own orderStr.
    const orderStr = '{"nextAction":"L","linkUrl":"https://www.***.pay.com/h5pay?prepay_id=***&sign=***","scheme":"","clientToken":"***"}';
    paymentService.requestPayment(this.context, orderStr, "AP")
      .then((payResult: paymentService.PayResult) => {
        // succeeded in paying
        console.info('succeeded in paying, pay result: ', payResult);
      })
      .catch((error: BusinessError) => {
        // failed to pay
        console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestPaymentPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestPaymentPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### paymentService.cashierPicker

cashierPicker(context: common.UIAbilityContext, paymentInfo: PaymentInfo): Promise<PickerResult>

该方法提供拉起通用收银台功能，调用方法前请确保网络已连接，用户在通用收银台选择支付方式并确认支付后，使用Promise异步返回。

**元服务API：**从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**5.0.2(14)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

UIAbility上下文，不传会报401参数错误。

paymentInfo

[PaymentInfo](#section1158325715256)

是

拉起通用收银台传入的支付信息。

**返回值**:

类型

说明

Promise<[PickerResult](#section1129353710263)>

Promise对象。带[PickerResult](#section1129353710263)返回结果的Promise对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

401

Parameter error.

1001930000

The operation was canceled by the user.

1001930001

Pay failed.

1001930002

The transaction has been processed.

1001930010

Duplicate request.

1001930011

Network connection error.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestCashierPicker() {
    // use your own paymentInfo
    const paymentInfo: paymentService.PaymentInfo= {
      tradeSummary: "***交易",
      amount: 100,
      currency: "CNY",
      extraInfo: '{"***":"***"}'
    }
    paymentService.cashierPicker(this.context, paymentInfo)
      .then((pickerResult: paymentService.PickerResult) => {
        // succeeded in paying
        console.info('succeeded in paying, picker result: ', pickerResult);
      })
      .catch((error: BusinessError) => {
        // failed to pay
        console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestCashierPicker')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestCashierPicker();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### paymentService.requestBindCard

requestBindCard(context: common.UIAbilityContext | common.UIExtensionContext): Promise<BindCardResult>

该方法提供用户绑卡功能，调用该方法后会拉起Payment Kit用户绑卡页面，绑卡完成后使用Promise异步返回。调用方法前请确保网络已连接。

**元服务API：**从版本5.0.5(17)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.PaymentService

**起始版本：**5.0.5(17)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) | common.[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)

是

UIAbility上下文，不传会报401参数错误。

**返回值**:

类型

说明

Promise<[BindCardResult](#section1492519912514)>

Promise对象。带[BindCardResult](#section1492519912514)返回结果的Promise对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

401

Parameter error.

1001930000

The operation was canceled by the user.

1001930011

Network connection error.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestBindCardPromise() {
    paymentService.requestBindCard(this.context)
      .then((bindCardResult: paymentService.BindCardResult) => {
        // succeeded in bind card
        console.info('succeeded in bind card');
      })
      .catch((error: BusinessError) => {
        // failed to bind card
        console.error(`failed to bind card, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestBindCardPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestBindCardPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```