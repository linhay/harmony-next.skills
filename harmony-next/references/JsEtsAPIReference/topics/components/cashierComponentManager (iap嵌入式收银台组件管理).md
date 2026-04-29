# cashierComponentManager (iap嵌入式收银台组件管理)

本模块提供iap嵌入式收银台组件的逻辑管理，辅助应用通过集成iap嵌入式收银台组件完成应用内支付功能。

起始版本： 6.1.0(23)

**导入模块**

```ets
import { cashierComponentManager } from '@kit.IAPKit';
```

**CashierListener**

[CashierComponent](CashierComponent (iap嵌入式收银台组件).md#ZH-CN_TOPIC_0000002522082362__cashiercomponent)组件的监听，用来回调组件调用的成功、失败事件。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.IAP.EmbeddedCashier

起始版本： 6.1.0(23)

**onPurchaseSuccess**

onPurchaseSuccess(productId: string, purchaseResult: iap.CreatePurchaseResult): void

iap嵌入式收银台的支付成功回调。在用户使用iap嵌入式收银台支付成功后，应用可接收此回调，用于后续逻辑处理、记录运营事件等场景。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.IAP.EmbeddedCashier

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| productId | string | 是 | 支付成功的商品ID。 |
| purchaseResult | iap.CreatePurchaseResult | 是 | 支付成功回调获取到的iap.CreatePurchaseResult对象。 |

**onPurchaseFailure**

onPurchaseFailure(productId: string, error: BusinessError<void>): void

iap嵌入式收银台的支付失败回调。在用户使用iap嵌入式收银台支付失败后，应用可接收此回调，可用于后续逻辑处理，记录运营事件等场景。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.IAP.EmbeddedCashier

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| productId | string | 是 | 支付失败的商品ID。 |
| error | BusinessError<void> | 是 | 支付失败回调获取到的iap.CreatePurchaseResult对象。 |

**CashierDisplayOptions**

该接口定义了收银台的属性。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.IAP.EmbeddedCashier

起始版本： 6.1.0(23)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backgroundColor | ResourceColor | 否 | 收银台背景颜色。 |