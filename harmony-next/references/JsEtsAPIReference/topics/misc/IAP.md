# IAP

本模块提供应用内支付的能力。

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**4.0.0(10)

#### 导入模块

```ets
import { iap } from '@kit.IAPKit';
```

#### ProductType

商品类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

名称

值

说明

CONSUMABLE

0

消耗型商品。

NONCONSUMABLE

1

非消耗型商品。

AUTORENEWABLE

2

自动续期订阅商品。

该属性不支持Wearable设备。

**起始版本：**4.1.0(11)

NONRENEWABLE

3

非续期订阅商品。

该属性不支持Wearable设备。

**元服务API：**从版本5.0.2(14)开始，该接口支持在元服务中使用。

**起始版本：**5.0.2(14)

#### PurchaseQueryType

查询购买信息的类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

名称

值

说明

ALL

0

所有历史购买记录，包括消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。

UNFINISHED

1

已购买但未交付的消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。

CURRENT_ENTITLEMENT

2

已购非消耗型商品和当前生效的自动续期订阅商品。

#### PeriodUnit

自动续期订阅商品的周期单位。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

名称

值

说明

DAY

0

天。

WEEK

1

周。

MONTH

2

月。

YEAR

3

年。

MINUTE

4

分（预留参数，暂未支持）。

#### OfferPaymentMode

促销的付费方式。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

名称

值

说明

FREE_TRIAL

1

免费试用。

PAY_AS_YOU_GO

2

随用随付。

PAY_UP_FRONT

3

提前支付。

SINGLE_PROMOTION

5

单次优惠（暂不支持），仅适用于消耗型/非消耗型/非续期订阅商品。

该属性不支持Wearable、TV设备。

**元服务API：**从版本5.0.5(17)开始，该接口支持在元服务中使用。

**起始版本：**5.0.5(17)

#### OfferType

促销类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

名称

值

说明

INTRODUCTORY

0

推介促销。

PROMOTIONAL

1

优惠促销。

#### IAPErrorCode

错误码枚举。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

名称

值

说明

USER_CANCELED

1001860000

用户取消当前操作。

SYSTEM_ERROR

1001860001

通用失败错误码。

APP_NOT_AUTHORIZED

1001860002

应用未被授权访问接口。

INVALID_PRODUCT

1001860003

无效的商品信息。

FREQUENT_CALLS

1001860004

接口访问过频。

NETWORK_ERROR

1001860005

网络连接异常。

PRODUCT_TERRITORY_NOT_SUPPORTED

1001860007

商品所属的应用未在指定国家/地区上架。

ACCOUNT_NOT_LOGGED_IN

1001860050

未登录华为账号。

PRODUCT_OWNED

1001860051

由于已经拥有该商品，购买失败。

PURCHASE_NOT_PAID

1001860052

由于未拥有该商品，发货失败。

PURCHASE_FINISHED

1001860053

此次购买已经完成发货，无需重复发货。

ACCOUNT_TERRITORY_NOT_SUPPORTED

1001860054

用户账号所在服务地暂不支持IAP。

USER_NOT_ALLOWED

1001860056

用户交易被拒绝。

APP_NOT_DEBUG

1001860057

当前应用不是debug签名的应用。

**起始版本：**5.0.0(12)

ACCOUNT_NOT_TEST

1001860058

华为账号不是沙盒测试账号。

**起始版本：**5.0.0(12)

INVALID_PROMOTIONAL_OFFER

1001860059

无效的优惠信息。

**起始版本：**5.0.0(12)

INVALID_PURCHASE_SIGNATURE

1001860060

无效的签名信息。

**起始版本：**5.0.0(12)

PURCHASE_ALREADY_REFUNDED

1001860061

商品已退款或退款中。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**起始版本：**5.0.3(15)

REFUND_NOT_ALLOWED

1001860062

不允许退款。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**起始版本：**5.0.3(15)

#### WindowScreenMode

界面窗口模式。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**5.0.0(12)

名称

值

说明

DIALOG_BOX

1

界面窗口弹窗模式。

FULLSCREEN

2

界面窗口全屏模式。

#### ProductStatus

商品状态枚举。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**5.0.0(12)

名称

值

说明

VALID

0

生效状态。

CANCELED

1

取消状态，即删除。此状态的商品不可续订，也不可订阅。

OFFLINE

3

下线状态，不能订阅，但老用户仍可续订。

#### iap.queryEnvironmentStatus

queryEnvironmentStatus(context: common.Context): Promise<void>

查询用户登录的账号服务地是否在IAP Kit支持结算的国家/地区中。当前只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

上下文。建议使用[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860000

The operation was canceled by the user.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

iap.queryEnvironmentStatus(this.getUIContext().getHostContext() as common.UIAbilityContext).then(() => {
  // 请求成功
  console.info('Succeeded in querying environment status.');
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to query environment status. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.queryEnvironmentStatus

queryEnvironmentStatus(context: common.Context, callback: AsyncCallback<void>): void

查询用户登录的账号服务地是否在IAP Kit支持结算的国家/地区中。当前只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

上下文。建议使用[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

callback

AsyncCallback<void>

是

回调函数。当用户登录的账号服务地在IAP Kit支持结算的国家/地区中时，err为undefined，否则为错误对象。

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860000

The operation was canceled by the user.

1001860001

System internal error.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

iap.queryEnvironmentStatus(this.getUIContext().getHostContext() as common.UIAbilityContext, (err: BusinessError) => {
  if (err) {
    // 请求失败
    console.error(`Failed to query environment status. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  // 请求成功
  console.info('Succeeded in querying environment status.');
});
```

#### iap.queryProducts

queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter): Promise<Array<Product>>

获取在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)上配置的商品详情信息。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[QueryProductsParameter](#section1033653365917)

是

包含请求信息的[QueryProductsParameter](#section1033653365917)对象。

**返回值：**

类型

说明

Promise<Array<[Product](#section346874219313)>>

Promise对象，返回商品详情信息。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860003

Invalid product information.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860050

The HUAWEI ID is not signed in.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryProductsParameter = {
  // iap.ProductType.CONSUMABLE：消耗型商品
  // iap.ProductType.NONCONSUMABLE：非消耗型商品
  // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
  // iap.ProductType.NONRENEWABLE：非续期订阅商品
  productType: iap.ProductType.CONSUMABLE,
  // productIds中的商品需要替换成开发者在AppGallery Connect网站配置的商品
  productIds: ['testConsumeProduct01', 'testConsumeProduct02']
}
iap.queryProducts(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: Array<iap.Product>) => {
  // 请求成功
  console.info(`Succeeded in querying products. data length: ${data?.length}`);
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.queryProducts

queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter, callback: AsyncCallback<Array<Product>>): void

用于获取在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)上配置的商品详情信息。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[QueryProductsParameter](#section1033653365917)

是

包含请求信息的[QueryProductsParameter](#section1033653365917)对象。

callback

AsyncCallback<Array<[Product](#section346874219313)>>

是

回调函数。当查询成功时，err为undefined，data为获取到的Array<[Product](#section346874219313)>；否则为错误对象。

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860003

Invalid product information.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860050

The HUAWEI ID is not signed in.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryProductsParameter = {
  // iap.ProductType.CONSUMABLE：消耗型商品
  // iap.ProductType.NONCONSUMABLE：非消耗型商品
  // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
  // iap.ProductType.NONRENEWABLE：非续期订阅商品
  productType: iap.ProductType.CONSUMABLE,
  // productIds中的商品需要替换成开发者在AppGallery Connect网站配置的商品
  productIds: ['testConsumeProduct01', 'testConsumeProduct02']
}
iap.queryProducts(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: Array<iap.Product>) => {
  if (err) {
    // 请求失败
    console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  // 请求成功
  console.info(`Succeeded in querying products. data length: ${data?.length}`);
});
```

#### iap.queryProducts

queryProducts(context: common.UIAbilityContext, productIds: string[]): Promise<Array<Product>>

查询在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)上配置的商品详情信息。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**6.0.0(20)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

productIds

string[]

是

待查询商品ID列表。商品ID必须已经在当前应用中创建且唯一。

商品ID来源于开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)中配置商品信息时设置的商品ID，请参见[配置商品信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-config-product)。

 说明：

一次最多可查询200个商品，商品数量较多时建议分批查询。

**返回值：**

类型

说明

Promise<Array<[Product](#section346874219313)>>

Promise对象，返回商品详情信息。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1001860001

System internal error.

1001860002

The application is not authorized.

1001860003

Invalid product information.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860050

The HUAWEI ID is not signed in.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// productIds中的商品需要替换成开发者在AppGallery Connect网站配置的商品
const productIds: string[] = ['testConsumeProduct01', 'testConsumeProduct02'];
iap.queryProducts(this.getUIContext().getHostContext() as common.UIAbilityContext, productIds).then((data: Array<iap.Product>) => {
  // 请求成功
 console.info(`Succeeded in querying products. data length: ${data?.length}`);
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
})
```

#### iap.purchase(deprecated)

purchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<PurchaseResult>

创建订单，支持消耗型商品和非消耗型商品。在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)创建商品后，应用使用此接口调用华为应用内支付收银台，显示商品、价格和支付方式。

使用Promise异步回调。

**废弃说明：**从4.1.0(11)开始废弃，建议使用[createPurchase](#section18798154545516)替代。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[PurchaseParameter](#section1340120344598)

是

包含请求信息的[PurchaseParameter](#section1340120344598)对象。

**返回值：**

类型

说明

Promise<[PurchaseResult](#section111613541391)>

Promise对象，返回购买结果。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860000

The operation was canceled by the user.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860003

Invalid product information.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860051

Failed to purchase a product because the user already owns the product.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

1001860056

The user is not allowed to make purchase.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.PurchaseParameter = {
  // iap.ProductType.CONSUMABLE：消耗型商品
  // iap.ProductType.NONCONSUMABLE：非消耗型商品
  productType: iap.ProductType.CONSUMABLE,
  // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
  productId: 'testConsumeProduct01',
  developerPayload: 'test developer payload string.'
}
iap.purchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.PurchaseResult) => {
  // 请求成功
  console.info('Succeeded in purchasing.');
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to purchase. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.purchase(deprecated)

purchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<PurchaseResult>): void

创建订单，支持消耗型商品和非消耗型商品。在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)创建商品后，使用此接口调用华为应用内支付收银台，显示商品、价格和支付方式。

使用callback异步回调。

**废弃说明：**从4.1.0(11)开始废弃，建议使用[createPurchase](#section19694203910585)替代。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[PurchaseParameter](#section1340120344598)

是

包含请求信息的[PurchaseParameter](#section1340120344598)对象。

callback

AsyncCallback<[PurchaseResult](#section111613541391)>

是

回调函数。当购买成功时，err为undefined，data为获取到的[PurchaseResult](#section111613541391)对象；否则为错误对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860000

The operation was canceled by the user.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860003

Invalid product information.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860051

Failed to purchase a product because the user already owns the product.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

1001860056

The user is not allowed to make purchase.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.PurchaseParameter = {
  // iap.ProductType.CONSUMABLE：消耗型商品
  // iap.ProductType.NONCONSUMABLE：非消耗型商品
  productType: iap.ProductType.CONSUMABLE,
  // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
  productId: 'testConsumeProduct01',
  developerPayload: 'test developer payload string.'
}
iap.purchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.PurchaseResult) => {
  if (err) {
    // 请求失败
    console.error(`Failed to purchase. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  // 请求成功
  console.info('Succeeded in purchasing.');
});
```

#### iap.createPurchase

createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<CreatePurchaseResult>

发起购买，支持消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)创建商品后，使用此接口拉起华为应用内支付收银台，显示商品名称、商品价格等信息。

使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[PurchaseParameter](#section1340120344598)

是

包含请求信息的[PurchaseParameter](#section1340120344598)对象。

**返回值：**

类型

说明

Promise<[CreatePurchaseResult](#section193852021105111)>

Promise对象，返回购买结果。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860000

The operation was canceled by the user.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860003

Invalid product information.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860051

Failed to purchase a product because the user already owns the product.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

1001860056

The user is not allowed to make purchase.

1001860059

Invalid promotional offer id.

1001860060

Invalid purchase signature.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.PurchaseParameter = {
  // iap.ProductType.CONSUMABLE：消耗型商品
  // iap.ProductType.NONCONSUMABLE：非消耗型商品
  // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
  // iap.ProductType.NONRENEWABLE：非续期订阅商品
  productType: iap.ProductType.AUTORENEWABLE,
  // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
  productId: 'testProduct01',
  developerPayload: 'test developer payload string.'
}
iap.createPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.CreatePurchaseResult) => {
  // 请求成功
  console.info(`Succeeded in creating purchase. data: ${data.purchaseData}`);
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to create purchase. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.createPurchase

createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<CreatePurchaseResult>): void

发起购买，支持消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)创建商品后，使用此接口拉起华为应用内支付收银台，显示商品名称、价格等信息。

使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[PurchaseParameter](#section1340120344598)

是

包含请求信息的[PurchaseParameter](#section1340120344598)对象。

callback

AsyncCallback<[CreatePurchaseResult](#section193852021105111)>

是

回调函数。当购买成功时，err为undefined，data为获取到的[CreatePurchaseResult](#section193852021105111)对象；否则为错误对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860000

The operation was canceled by the user.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860003

Invalid product information.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860051

Failed to purchase a product because the user already owns the product.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

1001860056

The user is not allowed to make purchase.

1001860059

Invalid promotional offer id.

1001860060

Invalid purchase signature.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.PurchaseParameter = {
  // iap.ProductType.CONSUMABLE：消耗型商品
  // iap.ProductType.NONCONSUMABLE：非消耗型商品
  // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
  // iap.ProductType.NONRENEWABLE：非续期订阅商品
  productType: iap.ProductType.AUTORENEWABLE,
  // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
  productId: 'testProduct01',
  developerPayload: 'test developer payload string.'
}
iap.createPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.CreatePurchaseResult) => {
  if (err) {
    // 请求失败
    console.error(`Failed to create purchase. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  // 请求成功
  console.info(`Succeeded in creating purchase. data: ${data.purchaseData}`);
});
```

#### iap.consumePurchase(deprecated)

consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter): Promise<ConsumeResult>

在消耗型商品支付成功后，应用需要在发放商品成功之后调用此接口对消耗型商品执行消耗操作。使用Promise异步回调。

**废弃说明：**从4.1.0(11)开始废弃，建议使用[finishPurchase](#section124751324135814)替代。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[ConsumePurchaseParameter](#section659703618597)

是

包含请求信息的[ConsumePurchaseParameter](#section659703618597)对象。

**返回值：**

类型

说明

Promise<[ConsumeResult](#section1343816549919)>

Promise对象，返回消耗结果。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860050

The HUAWEI ID is not signed in.

1001860052

The purchase cannot be finished because the user has not paid for it.

1001860053

The purchase has been finished and cannot be finished again.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.ConsumePurchaseParameter = {
  purchaseToken: '***',
  developerChallenge: 'developerChallenge'
}
iap.consumePurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.ConsumeResult) => {
  // 请求成功
  console.info('Succeeded in consuming purchase.');
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to consume purchase. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.consumePurchase(deprecated)

consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter, callback: AsyncCallback<ConsumeResult>): void

在消耗型商品支付成功后，应用需要在发放商品成功之后调用此接口对消耗型商品执行消耗操作。使用callback异步回调。

**废弃说明：**从4.1.0(11)开始废弃，建议使用[finishPurchase](#section2045683917408)替代。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[ConsumePurchaseParameter](#section659703618597)

是

包含请求信息的[ConsumePurchaseParameter](#section659703618597)对象。

callback

AsyncCallback<[ConsumeResult](#section1343816549919)>

是

回调函数。当消耗成功时，err为undefined，data为获取到的[ConsumeResult](#section1343816549919)对象；否则为错误对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860050

The HUAWEI ID is not signed in.

1001860052

The purchase cannot be finished because the user has not paid for it.

1001860053

The purchase has been finished and cannot be finished again.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.ConsumePurchaseParameter = {
  purchaseToken: '***',
  developerChallenge: 'developerChallenge'
}
iap.consumePurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.ConsumeResult) => {
  if (err) {
    // 请求失败
    console.error(`Failed to consume purchase. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  // 请求成功
  console.info('Succeeded in consuming purchase.');
});
```

#### iap.finishPurchase

finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter): Promise<void>

应用完成已购商品的发货后，调用此接口确认发货，指明此次购买流程结束。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[FinishPurchaseParameter](#section103714142118)

是

包含请求信息的[FinishPurchaseParameter](#section103714142118)对象。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

1001860052

The purchase cannot be finished because the user has not paid for it.

1001860053

The purchase has been finished and cannot be finished again.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const finishPurchaseParam: iap.FinishPurchaseParameter = {
  // iap.ProductType.CONSUMABLE：消耗型商品
  // iap.ProductType.NONCONSUMABLE：非消耗型商品
  // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
  // iap.ProductType.NONRENEWABLE：非续期订阅商品
  productType: iap.ProductType.CONSUMABLE,
  purchaseToken: '***',
  purchaseOrderId: '***'
};
iap.finishPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, finishPurchaseParam).then(() => {
  // 请求成功
  console.info('Succeeded in finishing purchase.');
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.finishPurchase

finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter, callback: AsyncCallback<void>): void

应用完成已购商品的发货后，调用此接口确认发货，指明此次购买流程结束。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[FinishPurchaseParameter](#section103714142118)

是

包含请求信息的[FinishPurchaseParameter](#section103714142118)对象。

callback

AsyncCallback<void>

是

回调函数。当确认发货成功时，err为undefined，否则为错误对象。

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

1001860052

The purchase cannot be finished because the user has not paid for it.

1001860053

The purchase has been finished and cannot be finished again.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const finishPurchaseParam: iap.FinishPurchaseParameter = {
  // iap.ProductType.CONSUMABLE：消耗型商品
  // iap.ProductType.NONCONSUMABLE：非消耗型商品
  // iap.ProductType.AUTORENEWABLE：自动续期订阅商品
  // iap.ProductType.NONRENEWABLE：非续期订阅商品
  productType: iap.ProductType.CONSUMABLE,
  purchaseToken: '***',
  purchaseOrderId: '***'
};
iap.finishPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, finishPurchaseParam, (err: BusinessError) => {
  if (err) {
    // 请求失败
    console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  // 请求成功
  console.info('Succeeded in finishing purchase.');
});
```

#### iap.queryOwnedPurchases(deprecated)

queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>

查询用户已订购商品的购买数据，包括消耗型商品和非消耗型商品，一次请求只能查询一种类型的商品。

- 若查询消耗型商品，IAP仅返回用户已购未消耗的购买数据。若有购买数据返回，说明可能存在因某些异常而导致未进行发货的情况，需要应用判断是否已发货，未发货则需要进行补发货处理。开发者应用发货成功后调用[consumePurchase](#section754232910168)接口进行消耗。消耗成功的订单信息将不会在此接口返回，可通过[queryPurchaseRecords](#section69451529105019)接口获取。

- 若查询非消耗型商品，IAP返回用户所有已订购商品的购买数据。

使用Promise异步回调。

**废弃说明：**从4.1.0(11)开始废弃，建议使用[queryPurchases](#section1147122418532)替代。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[QueryPurchasesParameter](#section555872993213)

是

包含请求信息的[QueryPurchasesParameter](#section555872993213)对象。

**返回值：**

类型

说明

Promise<[QueryPurchasesResult](#section7249204210514)>

Promise对象，返回查询的购买数据信息。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860003

Invalid product information.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860050

The HUAWEI ID is not signed in.

1001860053

The purchase has been finished and cannot be finished again.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE
}
iap.queryOwnedPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.QueryPurchasesResult) => {
  // 请求成功
  console.info('Succeeded in querying owned purchases.');
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to query owned purchases. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.queryOwnedPurchases(deprecated)

queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void

查询用户已订购商品的购买数据，包括消耗型商品和非消耗型商品，一次请求只能查询一种类型的商品。

- 若查询消耗型商品，IAP仅返回用户已购未消耗的购买数据。若有购买数据返回，说明可能存在因某些异常而导致未进行发货的情况，需要应用判断是否已发货，未发货则需要进行补发货处理。开发者应用发货成功后调用[consumePurchase](#section754232910168)接口进行消耗。消耗成功的订单信息将不会在此接口返回，可通过[queryPurchaseRecords](#section1495292925012)接口获取。

- 若查询非消耗型商品，IAP返回用户所有已订购商品的购买数据。

使用callback异步回调。

**废弃说明：**从4.1.0(11)开始废弃，建议使用[queryPurchases](#section11799839122114)替代。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[QueryPurchasesParameter](#section555872993213)

是

包含请求信息的[QueryPurchasesParameter](#section555872993213)对象。

callback

AsyncCallback<[QueryPurchasesResult](#section7249204210514)>

是

回调函数。当查询成功时，err为undefined，data为获取到[QueryPurchasesResult](#section7249204210514)对象；否则为错误对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860003

Invalid product information.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860007

The app to which the product belongs is not released in a specified location.

1001860050

The HUAWEI ID is not signed in.

1001860053

The purchase has been finished and cannot be finished again.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE
}
iap.queryOwnedPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.QueryPurchasesResult) => {
  if (err) {
    // 请求失败
    console.error(`Failed to query owned purchases. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  // 请求成功
  console.info('Succeeded in querying owned purchases.');
});
```

#### iap.queryPurchaseRecords(deprecated)

queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>

获取已执行过消耗操作的消耗型商品的购买数据。使用Promise异步回调。

**废弃说明：**从4.1.0(11)开始废弃，建议使用[queryPurchases](#section1147122418532)替代。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[QueryPurchasesParameter](#section555872993213)

是

包含请求信息的[QueryPurchasesParameter](#section555872993213)对象。

**返回值：**

类型

说明

Promise<[QueryPurchasesResult](#section7249204210514)>

Promise对象，返回已执行过消耗操作的消耗型商品的购买数据。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE
}
iap.queryPurchaseRecords(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.QueryPurchasesResult) => {
  // 请求成功
  console.info('Succeeded in querying purchase records.');
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to query purchase records. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.queryPurchaseRecords(deprecated)

queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void

获取已执行过消耗操作的消耗型商品的购买数据。使用callback异步回调。

**废弃说明：**从4.1.0(11)开始废弃，建议使用[queryPurchases](#section11799839122114)替代。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回1001860001错误码。

**起始版本：**4.0.0(10)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[QueryPurchasesParameter](#section555872993213)

是

包含请求信息的[QueryPurchasesParameter](#section555872993213)对象。

callback

AsyncCallback<[QueryPurchasesResult](#section7249204210514)>

是

回调函数。当查询成功时，err为undefined，data为获取到[QueryPurchasesResult](#section7249204210514)对象；否则为错误对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE
}
iap.queryPurchaseRecords(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.QueryPurchasesResult) => {
  if (err) {
    // 请求失败
    console.error(`Failed to query purchase records. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  // 请求成功
  console.info('Succeeded in querying purchase records.');
});
```

#### iap.queryPurchases

queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchaseResult>

查询已购商品的订单信息，包含 ：

- 已购买但是未确认发货的商品的订单信息。
- 当前生效的非消耗型商品、自动续期订阅商品和非续期订阅商品。

使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[QueryPurchasesParameter](#section555872993213)

是

包含请求信息的[QueryPurchasesParameter](#section555872993213)对象。

**返回值：**

类型

说明

Promise<[QueryPurchaseResult](#section820381425513)>

Promise对象，返回已购商品的订单信息。在沙盒场景下，已发货状态的非消耗型商品订单信息将不返回。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE,
  queryType: iap.PurchaseQueryType.UNFINISHED
}
iap.queryPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.QueryPurchaseResult) => {
  // 请求成功
  console.info(`Succeeded in querying purchases. data len: ${data.purchaseDataList?.length}`);
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.queryPurchases

queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchaseResult>): void

查询已购商品的订单信息，包含 ：

- 已购买但是未确认发货的商品的订单信息。
- 当前生效的非消耗型商品、自动续期订阅商品和非续期订阅商品。

使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)上下文。

parameter

[QueryPurchasesParameter](#section555872993213)

是

包含请求信息的[QueryPurchasesParameter](#section555872993213)对象。

callback

AsyncCallback<[QueryPurchaseResult](#section820381425513)>

是

回调函数。当查询成功时，err为undefined，data为获取到[QueryPurchaseResult](#section820381425513)对象；否则为错误对象。同时，在沙盒场景下，已发货状态的非消耗型商品订单信息将不返回。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE,
  queryType: iap.PurchaseQueryType.UNFINISHED
}
iap.queryPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.QueryPurchaseResult) => {
  if (err) {
    // 请求失败
    console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  // 请求成功
  console.info(`Succeeded in querying purchases. data len: ${data.purchaseDataList?.length}`);
});
```

#### iap.showManagedSubscriptions

showManagedSubscriptions(context: common.Context, uiParameter: UIWindowParameter, groupId?: string): Promise<void>

跳转到订阅页或订阅详情页。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、Tablet、2in1、TV设备设备中可正常调用，在其他设备中返回801错误码。

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

上下文。建议使用[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

uiParameter

[UIWindowParameter](#section12131915171317)

是

包含界面窗口模式的[UIWindowParameter](#section12131915171317)对象。

groupId

string

否

订阅组ID，来源于开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)中配置管理的订阅组，请参见[新增订阅组](https://developer.huawei.com/consumer/cn/doc/app/non-subscription-0000001958955109#section37862471018)。

 说明：

- 传递groupId，跳转到订阅详情页。
- 不传递groupId，跳转到订阅页。如果用户在应用只有一条订阅数据，此时会跳转到此条订阅的订阅详情页。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

801

Capability not supported. Failed to call the API due to limited device capabilities.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const uiWindowParameter: iap.UIWindowParameter = {
  windowScreenMode: iap.WindowScreenMode.DIALOG_BOX
}
const groupId = '***';
iap.showManagedSubscriptions(this.getUIContext().getHostContext() as common.UIAbilityContext, uiWindowParameter, groupId).then(() => {
  // 请求成功
  console.info('Succeeded in showing subscription page.');
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to show subscription page. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.isSandboxActivated

isSandboxActivated(context: common.Context): Promise<boolean>

检查沙盒测试能力是否生效。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

上下文。建议使用[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

**返回值：**

类型

说明

Promise<boolean>

Promise对象。返回true表示沙盒测试能力生效；返回false表示沙盒测试能力未生效，可根据返回的错误码检查未生效原因。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860050

The HUAWEI ID is not signed in.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

1001860057

The app provision type is not debug.

1001860058

The HUAWEI ID is not test account.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

iap.isSandboxActivated(this.getUIContext().getHostContext() as common.UIAbilityContext).then((isActivated: boolean) => {
  // 请求成功
  console.info(`Succeeded in checking the sandbox status. is activate: ${isActivated}`);
}).catch((err: BusinessError) => {
  // 请求失败
  console.error(`Failed to check the sandbox status. Code is ${err.code}, message is ${err.message}`);
});
```

#### iap.createRefundRequest

createRefundRequest(context: common.Context, purchaseOrderId: string): Promise<void>

退款接口，调用此接口拉起退款流程，仅支持非游戏应用。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**设备行为差异：**该接口在Phone、Tablet、2in1设备中可正常调用，在其他设备中返回801错误码。

**起始版本：**5.0.3(15)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

上下文。

purchaseOrderId

string

是

具体一笔订单中对应的购买订单号ID。最大长度256。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

801

Capability not supported. Failed to call the API due to limited device capabilities.

1001860000

The operation was canceled by the user.

1001860001

System internal error.

1001860002

The application is not authorized.

1001860004

Too frequent API calls.

1001860005

Network connection error.

1001860054

The country or region of the signed-in HUAWEI ID does not support IAP.

1001860061

The purchase has been refunded or in refund.

1001860062

Refund is not allowed.

**示例**：

```ets
import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct IapTest {
  /**
   * 拉起退款界面
   */
  createRefundRequest() {
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 调用iap.createRefundRequest拉起退款，传入context和purchaseOrderId
    let purchaseOrderId = '';
    iap.createRefundRequest(context, purchaseOrderId).then(() => {
      // 退款成功
      console.info('Succeeded in create refund request.');
      // ...
    }).catch((err: BusinessError) => {
      // 退款失败
      console.error(`Failed to create refund request. Code is ${err.code}, message is ${err.message}`);
      // ...
    });
  }
  build() {
  }
}
```

#### QueryProductsParameter

[queryProducts](#section55531442102518)接口的请求参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**名称**

**类型**

****只读

可选

**说明**

productType

[ProductType](#section59035422210)

否

否

需要查询的商品类型。

- CONSUMABLE：消耗型商品
- NONCONSUMABLE：非消耗型商品
- AUTORENEWABLE：自动续期订阅商品
- NONRENEWABLE：非续期订阅商品

productIds

string[]

否

否

待查询商品ID列表。商品ID必须已经在当前应用中创建且唯一。

商品ID来源于开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)中配置商品信息时设置的商品ID，请参见[配置商品信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-config-product)。

 说明：

一次查询最多支持200个商品，商品数量较多时建议分批查询。

#### Product

包含单个商品详细信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

名称

类型

只读

可选

说明

id

string

否

否

商品ID。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

type

[ProductType](#section59035422210)

否

否

商品类型。

- CONSUMABLE：消耗型商品
- NONCONSUMABLE：非消耗型商品
- AUTORENEWABLE：自动续期订阅商品
- NONRENEWABLE：非续期订阅商品

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

name

string

否

否

商品名称，为配置商品信息时配置的名称。用于显示在应用内支付收银台。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

description

string

否

否

商品描述，即配置商品信息时配置的描述信息。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

price(deprecated)

string

否

否

商品的展示价格，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。此价格含税。

- 当商品为消耗型/非消耗型商品时，若[设置促销价格](https://developer.huawei.com/consumer/cn/doc/app/promotion-non-subscription-0000001931836332#section1429175616582)，该字段为商品的促销价格，未设置则为商品原价。
- 当商品为自动续期订阅商品时，该字段为商品的原价。

 说明：

从4.1.0(11)开始废弃，建议使用localPrice替代。

localPrice

string

否

是

商品的展示价格，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。此价格含税。可选。

- 当商品为消耗型/非消耗型商品/非续期订阅商品，若设置促销价格，该字段为商品的促销价格，未设置则为商品原价。（促销价格能力已调整为[临时价格调整](https://developer.huawei.com/consumer/cn/doc/app/revise-non-subscription-0000001931836328)，临时价格调整场景下该字段为商品原价）
- 当商品为自动续期订阅商品时，该字段为商品的原价。

**起始版本：**4.1.0(11)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

microPrice

number

否

否

商品实际价格乘以1,000,000后的微单位价格。例如某个商品实际价格是1.99美元，则该商品对应的微单位价格为：1.99*1000000=1990000。

- 当商品为消耗型/非消耗型商品/非续期订阅商品，若设置促销价格，该字段为商品微单位促销价格，未设置则为商品微单位原价。（促销价格能力已调整为[临时价格调整](https://developer.huawei.com/consumer/cn/doc/app/revise-non-subscription-0000001931836328)，临时价格调整场景下该字段为商品原价）
- 当商品为自动续期订阅商品时，该字段为商品微单位原价。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

originalLocalPrice

string

否

否

商品的原价，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。此价格含税。

- 当商品为消耗型/非消耗型商品或者非续期订阅商品，无论是否[设置促销价格](https://developer.huawei.com/consumer/cn/doc/app/promotion-non-subscription-0000001931836332#section1429175616582)，该字段均为商品原价。
- 当商品为自动续期订阅商品时，无此字段返回，开发者无需关注。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

originalMicroPrice

number

否

否

商品原价的微单位价格。商品原价乘以1,000,000后的微单位价格。例如某个商品原价是1.99美元，则该商品对应的微单位价格为：1.99*1000000=1990000。

- 当商品为消耗型/非消耗型商品或者非续期订阅商品，无论是否[设置促销价格](https://developer.huawei.com/consumer/cn/doc/app/promotion-non-subscription-0000001931836332#section1429175616582)，该字段均为商品微单位原价。
- 当商品为自动续期订阅商品时，无此字段返回，开发者无需关注。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

currency

string

否

否

用于支付该商品的币种，例如CNY。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

status

[ProductStatus](#section2762171942710)

否

是

商品状态。

**起始版本：**5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

subscriptionInfo

[SubscriptionInfo](#section151973366473)

否

是

自动续期订阅商品相关的信息。可选。

**起始版本：**4.1.0(11)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

promotionalOffers

[PromotionalOffer](#section446812293465)[]

否

是

商品自定义人群优惠促销信息列表。

**起始版本：**5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

jsonRepresentation

string

否

是

商品详细信息的原始JSON字符串。

**起始版本：**4.1.0(11)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

#### PromotionalOffer

订阅商品支持的自定义优惠信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

offerId

string

否

否

优惠ID

paymentMode

[OfferPaymentMode](#section23427243315)

否

否

促销的付费方式

periodUnit

[PeriodUnit](#section3468210113210)

否

是

订阅周期单位。

periodCount

number

否

是

订阅周期数量。

localPrice

string

否

否

显示的优惠商品价格，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。

microPrice

number

否

否

显示的优惠商品实际价格乘以1,000,000后的微单位价格。例如某个商品实际价格是1.99美元，则该商品对应的微单位价格为：1.99*1000000=1990000。

#### SubscriptionInfo

订阅信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

periodUnit

[PeriodUnit](#section3468210113210)

否

否

订阅周期单位。

periodCount

number

否

否

订阅周期数量。

groupId

string

否

否

订阅组ID。

groupLevel

number

否

否

商品的订阅等级。

hasEligibilityForIntroOffer

boolean

否

是

用户是否享受过推介促销。取值如下：

- true：已享受过
- false：未享受过
- 其他：未获取到状态

introductoryOffer

[SubscriptionOffer](#section16479185319413)

否

是

促销信息。

#### SubscriptionOffer

促销信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

paymentMode

[OfferPaymentMode](#section23427243315)

否

否

促销的付费方式。

periodUnit

[PeriodUnit](#section3468210113210)

否

否

订阅周期单位。

periodCount

number

否

否

促销期数。

localPrice

string

否

否

促销价格，包含商品币种和价格，格式为“币种+商品价格”，例如 EUR 0.15。部分国家/地区会返回“货币符号+商品价格”，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）返回“￥0.15”。

microPrice

number

否

否

促销价格的微单位价格。促销价格乘以1,000,000后的微单位价格。

offerType

[OfferType](#section131398372313)

否

否

促销类型。

#### PurchaseParameter

[purchase](#section107784425446)接口和[createPurchase](#section18798154545516)接口的请求参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

可选

**说明**

productId

string

否

否

待支付的商品ID。商品ID来源于开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.md)中配置商品信息时设置的“商品ID”，具体请参见[配置商品信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-config-product)。

productType

[ProductType](#section59035422210)

否

否

需要查询的商品类型。

- CONSUMABLE：消耗型商品
- NONCONSUMABLE：非消耗型商品
- AUTORENEWABLE：自动续期订阅商品
- NONRENEWABLE：非续期订阅商品

developerPayload

string

否

是

商户侧保留信息。

若该字段有值，在支付成功后的回调结果中会原样返回给应用。

 说明：

该参数长度限制为[0, 256]。如超过长度限制，在支付成功后将返回被截断的数据。建议在发起请求前自行验证字段长度，避免非预期截断。

reservedInfo

string

否

是

要求JSON String格式，商户可以将额外需要传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。

例如：

```ets
let reservedInfo = "{\"key1\":\"value1\",\"key2\":\"value2\"}";
```

 说明：

该字段为预留字段，可选传入，开发者暂时无需关注。

promotionalOfferId

string

否

是

优惠ID。优惠ID来源于开发者为商品[配置优惠促销](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#li1264912560544)时设置的促销优惠标志符。传递该字段且要生效，需同时在jwsRepresentation字段中传递促销优惠信息。

**起始版本：**5.0.0(12)

applicationUserName

string

否

是

用户账户相关联的混淆字符串，唯一标识用户。传递优惠ID场景，可以传递该字段。

**起始版本：**5.0.0(12)

jwsRepresentation

string

否

是

包含购买参数信息的JWS格式签名数据。购买参数，如优惠促销等。详细说明见[生成优惠签名购买参数](生成优惠签名购买参数.md)。

**起始版本：**5.0.0(12)

quantity

number

否

是

购买参数。表示所购买消耗型/非续期订阅商品的数量，需满足以下限制。

- 一次仅针对单商品类型，不支持不同类型混合
- 一次请求数量不超过10个

 注意：

如果开发者使用了quantity参数以支持商品的批量购买，则需要在发货时校验下单的商品数量和最终发货商品数量是否一致，避免造成漏发、多发的情况。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**起始版本：**5.0.3(15)

#### PurchaseResult(deprecated)

[purchase](#section107784425446)接口的返回结果。

**废弃说明：**从4.1.0(11)开始废弃。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

可选

**说明**

inAppPurchaseData

string

否

否

订单数据的JSON字符串，包含的参数请参见[InAppPurchaseData](../../guides/数据类型说明.md#section494862084917)。

signature

string

否

否

返回使用IAP私钥签署paymentData字符串生成的签名字符串。

signatureAlgorithm

string

否

否

签名算法，固定为SHA256WithRSA/PSS。

#### CreatePurchaseResult

[createPurchase](#section18798154545516)接口的返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

purchaseData

string

否

否

包含支付结果的JSON字符串，包含的参数请参见[PurchaseData](../../guides/数据类型说明.md#section650794012482)。

#### ConsumePurchaseParameter(deprecated)

[consumePurchase](#section754232910168)接口的请求参数。

**废弃说明：**从4.1.0(11)开始废弃。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

可选

**说明**

purchaseToken

string

否

否

用户购买商品的标识，在支付完成时由IAP服务器生成。

 说明：

purchaseToken需从购买数据[InAppPurchaseData](../../guides/数据类型说明.md#section494862084917)中获取。支付成功或者请求[queryOwnedPurchases](#section78016131463)接口均会返回[InAppPurchaseData](../../guides/数据类型说明.md#section494862084917)的JSON字符串。

developerChallenge

string

否

是

开发者自定义的挑战字，唯一标识此次消耗请求。消耗成功后此挑战字会记录在购买数据中并返回。

 说明：

该参数长度限制为[0, 64]。

#### ConsumeResult(deprecated)

[consumePurchase](#section754232910168)接口的返回结果。

**废弃说明：**从4.1.0(11)开始废弃。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

可选

**说明**

consumedPurchaseData

string

否

否

包含消耗结果数据的JSON字符串。字符串中包含参数请参见[InAppPurchaseData](../../guides/数据类型说明.md#section494862084917)。

signature

string

否

否

使用IAP私钥签署消耗数据consumedPurchaseData生成的签名字符串。签名算法为参考signatureAlgorithm字段。

应用在收到此签名字符串后，请参见[对返回结果验签](对返回结果验签.md)对consumedPurchaseData的JSON字符串进行验签。

signatureAlgorithm

string

否

否

签名算法，固定为SHA256WithRSA/PSS。

#### FinishPurchaseParameter

[finishPurchase](#section124751324135814)接口请求参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

productType

[ProductType](#section59035422210)

否

否

商品类型。

- CONSUMABLE：消耗型商品
- NONCONSUMABLE：非消耗型商品
- AUTORENEWABLE：自动续期订阅商品
- NONRENEWABLE：非续期订阅商品

purchaseToken

string

否

否

购买订单中返回的购买token。

单次购买中与具体购买订单一一对应；订阅购买中与订阅Id一一对应。

 说明：

purchaseToken需从购买数据[PurchaseOrderPayload](../../guides/数据类型说明.md#section260562820380)中获取。请求[createPurchase](#section18798154545516)或[queryPurchases](#section1147122418532)接口均会返回[PurchaseOrderPayload](../../guides/数据类型说明.md#section260562820380)。

purchaseOrderId

string

否

否

购买订单中返回的购买订单ID。最大长度256。

 说明：

purchaseOrderId需从购买数据[PurchaseOrderPayload](../../guides/数据类型说明.md#section260562820380)中获取。请求[createPurchase](#section18798154545516)或[queryPurchases](#section1147122418532)接口均会返回[PurchaseOrderPayload](../../guides/数据类型说明.md#section260562820380)。

#### QueryPurchasesParameter

[queryOwnedPurchases](#section78016131463)、[queryPurchaseRecords](#section69451529105019)和[queryPurchases](#section1147122418532)接口的请求参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

可选

**说明**

productType

[ProductType](#section59035422210)

否

否

需要查询的商品类型。

- CONSUMABLE：消耗型商品
- NONCONSUMABLE：非消耗型商品
- AUTORENEWABLE：自动续期订阅商品
- NONRENEWABLE：非续期订阅商品

continuationToken

string

否

是

支持分页查询的数据定位标志。

第1次查询时可以不传该参数。如果用户拥有的商品数量非常大，当响应中存在continuationToken时，应用必须对当前方法发起另一个调用，并传入本次接收到的continuationToken。如果商品仍未查完，仍需要继续发起调用，直到不再返回continuationToken，表示已经返回全部商品。

queryType

[PurchaseQueryType](#section1389262216514)

否

是

查询类型。默认值为UNFINISHED。

- ALL：消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品的所有购买记录。
- UNFINISHED：已购买但未交付的消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。
- CURRENT_ENTITLEMENT：购买的非消耗型商品或当前有效的自动续期订阅商品。

 说明：

[queryOwnedPurchases](#section78016131463)、[queryPurchaseRecords](#section69451529105019)场景无需关注此字段。

**起始版本：**4.1.0(11)

#### QueryPurchasesResult(deprecated)

[queryOwnedPurchases](#section78016131463)和[queryPurchaseRecords](#section69451529105019)接口的返回结果。

**废弃说明：**从4.1.0(11)开始废弃。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

可选

**说明**

productList

string[]

否

否

商品ID的数组。

inAppPurchaseDataList

string[]

否

否

该字段以JSON字符串的形式记录[InAppPurchaseData](../../guides/数据类型说明.md#section494862084917)的数据，用于配合inAppSignatureList验签。每个JSON字符串包含的参数请参见[InAppPurchaseData](../../guides/数据类型说明.md#section494862084917)。

inAppSignatureList

string[]

否

否

对应inAppPurchaseDataList中每一个字符串的签名字符串。过程中使用IAP私钥签署，签名算法请参考signatureAlgorithm字段。

应用需要对inAppPurchaseDataList中的每个JSON字符串都进行验签，验签方法请参见[对返回结果验签](对返回结果验签.md)。

continuationToken

string

否

是

支持分页查询的数据定位标志。

如果用户拥有的商品数量非常大，当响应中存在continuationToken时，应用必须对当前方法发起另一个调用，并传入本次接收到的continuationToken。如果商品仍未查完，仍需要继续发起调用，直到不再返回continuationToken，表示已经返回全部商品。

signatureAlgorithm

string

否

否

签名算法，固定为SHA256WithRSA/PSS。

#### QueryPurchaseResult

[queryPurchases](#section1147122418532)接口的返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

purchaseDataList

string[]

否

否

[PurchaseData](../../guides/数据类型说明.md#section650794012482)字符串的数组。

continuationToken

string

否

是

支持分页查询的数据定位标志。

如果用户拥有的商品数量非常大，当响应中存在continuationToken时，应用必须对当前方法发起另一个调用，并传入本次接收到的continuationToken。如果商品仍未查完，仍需要继续发起调用，直到不再返回continuationToken，表示已经返回全部商品。

#### UIWindowParameter

[iap.showManagedSubscriptions](#section39973360502)接口界面窗口参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.IAP

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

windowScreenMode

[WindowScreenMode](#section15231134814464)

否

否

界面窗口模式。

- DIALOG_BOX：弹窗模式
- FULLSCREEN：全屏模式