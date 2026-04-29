# promotionService(营销服务)

本模块支持拉起营销服务，包括活动入口组件以及选券组件。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

起始版本： 6.1.0(23)

**导入模块**

```ets
import { promotionService } from "@kit.PaymentKit";
```

**UserAction**

用户行为，包括关闭组件、点击领取按钮以及点击去使用按钮。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Promotion

起始版本： 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| doNothing | boolean | 否 | 否 | 表示是否关闭组件。 - true:是  - false：否（默认）。 |
| useButtonClicked | boolean | 否 | 否 | 表示是否点击“去使用”按钮。 - true:是  - false：否（默认）。 |
| receiveButtonClicked | boolean | 否 | 否 | 表示是否点击“领取”按钮。 - true:是  - false：否（默认）。 |

**OrderContext**

订单上下文信息，用于拉起选券组件。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Promotion

起始版本： 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mercNo | string | 否 | 否 | 商户号。 |
| tradeOrderAmount | number | 否 | 否 | 订单交易金额，单位为分。 |
| goodsCodes | string[] | 否 | 是 | 商品编码列表。 |
| authId | string | 否 | 否 | 商户证书ID。 |
| sign | string | 否 | 否 | 签名，使用除了sign字段以外的其他字段计算签名值。可参考签名规则。 |

**CouponCategory**

优惠券品类枚举类型。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Promotion

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLATFORM_COUPON | 0 | 平台券。 |

**CouponType**

优惠券类型枚举。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Promotion

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VOUCHER | 0 | 满减券类型。 |

**CouponDetail**

券详情信息。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Promotion

起始版本： 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| couponCategory | CouponCategory | 否 | 否 | 优惠券品类枚举类型。 |
| couponCode | string | 否 | 否 | 券码。 |
| batchNo | string | 否 | 否 | 批次号。 |
| couponType | CouponType | 否 | 否 | 券类型。 |
| effectiveTime | number | 否 | 否 | 优惠券生效时间。 |
| expireTime | number | 否 | 否 | 优惠券过期时间。 |
| amount | number | 否 | 是 | 优惠券面额，单位为分。 |
| logoUrl | string | 否 | 否 | 优惠券图标地址。 |
| couponDesc | string | 否 | 否 | 优惠券描述信息。最大长度3096。 |

**PromotionComponentController**

该类为营销组件控制器。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Promotion

起始版本： 6.1.0(23)

**constructor**

constructor(context: UIContext)

该方法实例化营销组件控制器对象，通过该接口可以拉起活动入口组件。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该实例方法支持在元服务中使用。

系统能力： SystemCapability.Payment.Promotion

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | UIContext | 是 | UI上下文对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码 | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1019200001 | System internal error. |
| 1019200002 | Network connection error. |

示例：

```ets
import { promotionService } from '@kit.PaymentKit';

@Component
struct StartPromotionEntryDialogDemo {
    controller: promotionService.PromotionComponentController = new promotionService.PromotionComponentController(this.getUIContext());

    build() {}
}
```

**startPromotionEntryDialog**

startPromotionEntryDialog(mercNo: string, offset?: number): Promise<UserAction>

拉起活动入口组件，使用Promise异步返回。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Promotion

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mercNo | string | 是 | 商户号。 |
| offset | number | 否 | 活动入口组件底部到屏幕边框底部的距离差，默认为100px。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<UserAction> | Promise对象。返回UserAction的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码 | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1019200001 | System internal error. |
| 1019200002 | Network connection error. |

示例：

```ets
import { promotionService } from "@kit.PaymentKit";

@Component
struct StartPromotionEntryDialogDemo {
  controller: promotionService.PromotionComponentController = new promotionService.PromotionComponentController(this.getUIContext());

  build() {
    Column() {
      Button('拉起活动入口组件')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(async () => {
          try {
            // 拉起活动入口组件
            let userAction = await this.controller.startPromotionEntryDialog('', 10);
            // 点击关闭、去使用后会分别返回doNothing、useButtonClicked为true
            console.info(`userAction ${JSON.stringify(userAction)}`);
          } catch (e) {
            console.error(`startUserSelectCouponsPopup error ${JSON.stringify(e)}`);
          }
        })
    }
```

**startUserChooseCouponsPopup**

startUserChooseCouponsPopup(context: common.Context, orderContext: OrderContext): Promise<CouponDetail[]>

选券组件拉起方法，调用后使用Promise异步返回。

模型约束： 本模块接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Promotion

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | 上下文。 |
| orderContext | OrderContext | 是 | 用户订单上下文。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<CouponDetail[]> | Promise对象。返回CouponDetail数组的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码 | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1019200001 | System internal error. |
| 1019200002 | Network connection error. |
| 1019200003 | Trade amount is invalid. |

示例：

```ets
import { promotionService } from "@kit.PaymentKit";

@Component
export struct StartUserChooseCouponsPopupDemo {
  build() {
    Column() {
      Button('选券页面')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          let req: promotionService.OrderContext = {
            // 商户号
            mercNo: '',
            // 订单金额，单位为分
            tradeOrderAmount: 15,
            // 商品编码
            goodsCodes: ['', ''],
            // 商户证书ID
            authId: '',
            // 签名内容调云侧接口获取
            sign: 'MEQCIEIWzdpziRyTi8vhwWHFuDdxf********************CHljer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ=='
          }
          console.info(`req ${JSON.stringify(req)}`);
          promotionService.startUserChooseCouponsPopup(this.getUIContext().getHostContext()!, req).then(res => {
            console.info(`startUserChooseCouponsPopup res ${JSON.stringify(res)}.`);
          }).catch((e: BusinessError) => {
            console.error(`startUserSelectCouponsPopup error ${JSON.stringify(e)}`);
          })
    }
```