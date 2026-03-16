[]()[]()

# 数据类型说明

[]()[]()

#### InAppPurchaseData

购买数据模型，支持消耗型商品、非消耗型商品。

名称

是否必选

类型

说明

applicationId

是

number

应用ID。

applicationIdString

是

string

字符串应用ID。

autoRenewing

是

boolean

消耗型商品或者非消耗型商品：固定为false。

orderId

是

string

订单ID，唯一标识一笔需要收费的收据，由IAP服务器在创建订单以及自动续期订阅商品续费时生成。

每一笔新的收据都会使用不同的orderId。

kind

是

number

商品类别，取值包括：

- 0：消耗型商品
- 1：非消耗型商品

packageName

否

string

应用安装包名。

productId

是

string

商品ID。

 说明：

为避免资金损失，开发者在对支付结果验签成功后，必须对其进行校验。

productName

否

string

商品名称。

purchaseTime

否

number

商品购买时间，UTC时间戳，以毫秒为单位。

如果没有完成购买，则没有值。

purchaseTimeMillis

否

number

历史接口兼容用，同purchaseTime，新接入无需关注本字段。

purchaseState

是

number

订单交易状态。

- -1：初始化

- 0：已购买
- 1：已取消
- 2：已退款
- 3：待处理

developerPayload

否

string

商户侧保留信息，由应用在调用支付接口时传入。

developerChallenge

否

string

应用发起消耗请求时自定义的挑战字，可唯一标识此次消耗请求。

consumptionState

否

number

消耗状态，取值包括：

- 0：未消耗
- 1：已消耗

confirmed

否

number

确认状态，取值包括：

- 0：未确认
- 1：已确认
- 没有值表示不需要确认

 说明：

该字段当前仅做兼容用，开发者无需关注。

purchaseToken

是

string

用于唯一标识商品和用户对应关系的购买令牌，在支付完成时由IAP服务器生成。

 说明：

- 当前92位，后续存在扩展可能，如要进行存储，建议预留128位的长度。
- 如要进行存储，为保证安全，建议加密存储。

purchaseType

否

number

购买类型。

- 0：沙盒环境（暂不支持）。
- 1：促销（暂不支持）。

正式购买不会返回该参数。

currency

否

string

币种。例如CNY。

 说明：

为避免资金损失，在对支付结果验签成功后，必须对其进行校验。

price

否

number

价格，单位：分。价格受如下因素影响：

- 开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中配置的商品价格
- 使用优惠后的价格，优惠类型[推介促销](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#li1088435316541)、[优惠促销](../topics/misc/生成优惠签名购买参数.md)、[挽留促销](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#li27291112195419)
- 批量购买商品的总价格

 说明：

为避免资金损失，在对支付结果验签成功后，必须对其进行校验。

country

否

string

国家/地区码，用于区分国家/地区信息，请参见[ISO 3166](https://www.iso.org/iso-3166-country-codes.html)标准。

payType

否

string

支付方式，取值请参见[payType说明](#section29304511489)。

payOrderId

否

string

交易单号，用户支付后生成。

[]()[]()

#### payType

payType取值说明。

取值

说明

0

花币。

4

支付宝。

94

华为支付。

[]()[]()

#### PurchaseData

包含jws格式的订单信息、订阅状态信息。

名称

是否必选

类型

说明

type

是

number

商品类型。

- 0：消耗型商品
- 1：非消耗型商品
- 2：自动续期订阅商品
- 3：非续期订阅商品

jwsPurchaseOrder

否

string

包含订单信息的JWS格式数据。可参见[对返回结果验签](../topics/misc/对返回结果验签.md)解码验签获取相关购买数据的JSON字符串，其包含的参数请参见[PurchaseOrderPayload](#section260562820380)。

jwsSubscriptionStatus

否

string

包含订阅状态信息的JWS格式数据。可参见[对返回结果验签](../topics/misc/对返回结果验签.md)解码验签获取相关订阅状态信息的JSON字符串，其包含的参数请参见[SubGroupStatusPayload](#section1311343185318)。

[]()[]()

#### PurchaseOrderPayload

订单信息模型，支持消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。

参数

是否必选

类型

说明

environment

是

string

环境类型。

- NORMAL：生产环境
- SANDBOX：沙盒环境

purchaseOrderId

是

string

具体一笔订单中对应的购买订单号ID。最大长度256。

purchaseToken

是

string

购买token，在购买消耗型/非消耗型商品/非续期订阅场景中与具体购买订单一一对应，在自动续期订阅商品场景中与订阅ID一一对应。

applicationId

是

string

应用ID。

productId

是

string

商品ID。

productType

是

string

商品类型。具体取值如下：

- 0：消耗型商品
- 1：非消耗型商品

- 2：自动续期订阅商品
- 3：非续期订阅商品

quantity

否

number

购买参数。表示所购买消耗型/非续期订阅商品的数量，需满足以下限制。

- 一次仅针对单商品类型，不支持不同类型混合
- 一次请求数量不超过10个

 注意：

如果开发者使用了quantity参数以支持商品的批量购买，则需要在发货时校验下单的商品数量和最终发货商品数量是否一致，避免造成漏发、多发的情况。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**起始版本：**5.0.3(15)

purchaseTime

是

number

购买时间，UTC时间戳，以毫秒为单位。

如果没有完成购买，则没有值。

finishStatus

否

string

发货状态。具体取值如下：

- 1：已发货
- 2：未发货

needFinish

否

boolean

是否需要确认发货，完成购买。具体取值如下：

- true：必须确认发货，完成购买
- false：可选确认发货，完成购买

price

是

number

价格，单位：分。价格受如下因素影响：

- 开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中配置的商品价格
- 使用优惠后的价格，优惠类型[推介促销](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#li1088435316541)、[优惠促销](../topics/misc/生成优惠签名购买参数.md)、[挽留促销](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#li27291112195419)
- 批量购买商品的总价格

currency

是

string

币种，请参见[ISO 4217](https://www.iso.org/iso-4217-currency-codes.html)标准。例如CNY、USD、MYR。

developerPayload

否

string

商户侧保留信息，由开发者在调用支付接口时传入。

purchaseOrderRevocationReasonCode

否

string

购买订单撤销原因。

- 0：其他
- 1：用户遇到问题退款

revocationTime

否

number

购买订单撤销时间，UTC时间戳，以毫秒为单位。

offerTypeCode

否

string

优惠类型。

- 1：推介促销
- 2：优惠促销
- 4：挽留促销

offerId

否

string

优惠ID。

countryCode

是

string

国家/地区码，用于区分国家/地区信息，请参见[ISO 3166](https://www.iso.org/iso-3166-country-codes.html)标准。

signedTime

是

number

签名时间，UTC时间戳，以毫秒为单位。

**以下参数只在自动续期订阅商品场景返回**

subGroupGenerationId

是

string

订阅组的代ID。

- 用户切换订阅商品时，此ID不会改变。
- 订阅失效且超出[保留期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#section1656191811315)后，用户重新购买商品时，此ID会改变。

subscriptionId

是

string

商品的订阅ID。以下场景，此ID会发生改变：

- 用户切换订阅商品时。
- 订阅失效且超出[保留期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#section1656191811315)后，用户重新购买商品时。

subGroupId

是

string

订阅型商品所属的商品组ID。

duration

是

string

此次购买的有效周期，采用ISO 8601格式。例如：P1W表示一周，P1M表示一个月。

durationTypeCode

是

string

订阅周期段类型。

- 0：正常周期段
- 1：延期段

[]()[]()

#### SubGroupStatusPayload

订阅组相关的订阅状态信息。

名称

是否必选

类型

说明

environment

是

string

环境类型。

- NORMAL：生产环境
- SANDBOX：沙盒环境

applicationId

是

string

应用ID。

packageName

是

string

应用包名。

subGroupId

是

string

订阅型商品所属的商品组ID。

lastSubscriptionStatus

否

object

订阅组中最后生效的订阅状态[SubscriptionStatus](#section1834146183116)，比如A切换B，B切换C，此处是C的订阅状态。

historySubscriptionStatusList

否

object[]

订阅组最近生效的历史订阅状态[SubscriptionStatus](#section1834146183116)的列表，按订阅切换时间升序 ，最多包含10条有效订阅状态信息的记录 。比如A切换B，B切换C，这里包含A，B，C三个订阅状态信息。

[]()[]()

#### SubscriptionStatus

订阅状态信息。

名称

是否必选

类型

说明

subGroupGenerationId

是

string

订阅组的代ID。

- 用户切换订阅商品时，此ID不会改变。
- 订阅失效且超出[保留期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#section1656191811315)后，用户重新购买商品时，此ID会改变。

subscriptionId

是

string

商品的订阅ID。以下场景，此ID会发生改变：

- 用户切换订阅商品时。
- 订阅失效且超出[保留期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#section1656191811315)后，用户重新购买商品时。

purchaseToken

是

string

购买token，在购买消耗型/非消耗型商品以及非续期订阅商品场景中与具体购买订单一一对应，在订阅型商品场景中与订阅ID一一对应。

status

是

string

订阅状态。

- 1：生效中
- 2：已到期
- 3：尝试扣费
- 5：撤销

expiresTime

是

number

自动续期订阅商品的过期时间，UTC时间戳，以毫秒为单位。

lastPurchaseOrder

否

object

当前订阅最新的一笔购买订单。购买订单包含的参数请参见[PurchaseOrderPayload](#section260562820380)。

recentPurchaseOrderList

否

object[]

当前订阅最新的购买订单列表，包含续期、折算、延期等产生的购买订单。购买订单包含的参数请参见[PurchaseOrderPayload](#section260562820380)。

renewalInfo

否

object

当前订阅最新的未来扣费计划，包含的参数请参见[SubRenewalInfo](#section971712308454)。

[]()[]()

#### SubRenewalInfo

订阅的扣费计划信息。

名称

是否必选

类型

说明

environment

是

string

环境类型。

- NORMAL：生产环境
- SANDBOX：沙盒环境

subGroupGenerationId

是

string

订阅组的代ID。

- 用户切换订阅商品时，此ID不会改变。
- 订阅失效且超出[保留期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-subscription-functions#section1656191811315)后，用户重新购买商品时，此ID会改变。

nextRenewPeriodProductId

否

string

下一个计费周期续订的商品ID。

productId

是

string

当前生效的商品ID。

autoRenewStatusCode

是

string

自动续期状态。

- 0：关闭
- 1：打开

hasInBillingRetryPeriod

是

boolean

系统是否还在尝试扣费。

- true：是
- false：否

priceIncreaseStatusCode

否

string

目前涨价状态码。

- 1：用户暂未同意涨价
- 2：用户已同意涨价

offerTypeCode

否

string

优惠类型。

- 1：推介促销
- 2：优惠促销
- 4：挽留促销

offerId

否

string

优惠ID。

renewalPrice

否

number

下期续费价格，取消订阅场景下不返回，单位：分。

currency

否

string

币种，请参见[ISO 4217](https://www.iso.org/iso-4217-currency-codes.html)标准。例如CNY、USD、MYR。

renewalTime

否

number

续期时间，UTC时间戳，以毫秒为单位。

expirationIntent

否

string

订阅续期失败的原因。

- 1：用户取消
- 2：商品无效
- 3：签约无效
- 4：扣费异常
- 5：用户不同意涨价
- 6：未知
- 7：存在未发货的订阅