[]()[]()

# 通过sysTransOrderNo查询订单信息

[]()[]()

#### 功能介绍

开发者可以调用此接口来查询所有通过华为支付方式支付且已成功创建交易订单的订单详细信息。

resultCode返回“000000”表示查询支付订单成功，不代表支付订单成功，订单状态需根据orderStatus字段判断。

[]()[]()

#### 场景描述

在产生交易订单前提下，商户可以通过该接口查看某笔订单的支付状态，也可以通过主动查询交易订单状态用以完成下一步的业务逻辑，常见的使用场景：

- 支付时由于网络、服务器等异常未收到支付回调通知。
- 调用支付接口返回未知支付状态时。

[]()[]()

#### 接口原型

承载协议

HTTPS GET

接口方向

开发者服务器 -> 华为支付服务器

接口URL

https://petalpay-developer.cloud.huawei.com.cn/api/v2/aggr/transactions/orders/{sysTransOrderNo}

数据格式

请求消息：Content-Type: application/json; charset=UTF-8

响应消息：Content-Type: application/json; charset=UTF-8

[]()[]()

#### 请求参数

**Request Header**

参数

是否必选

参数类型

描述

Content-Type

是

String

取值为：application/json; charset=UTF-8

PayMercAuth

是

String

取值为：[PayMercAuth](../../guides/数据模型说明.md#section11744172016145)的JSON字符串

**Request Path**

参数

是否必填

参数类型

描述

sysTransOrderNo

是

String

华为支付系统订单号。

用户支付成功后通过支付结果回调通知返回给商户或通过mercOrderNo查询订单信息接口查询获取。

[]()[]()

#### 请求示例

```ets
GET /api/v2/aggr/transactions/orders/{sysTransOrderNo} HTTP/1.1
Content-Type: application/json;charset=UTF-8
PayMercAuth:
{"callerId":"10132120***","traceId":"202305151047588466083","time":1684118878350,"authId":"120291744647139***","headerSign":"OaLyLiENHhYxXwZ+XhKKiYnzWsX/HJf+02A60A42fjh********************znmsDJOALXgvh/RKeReQBbc4lXZp5wnyZmdwTesmPGdszSNP/s=","bodySign":"kf9AZmVjBSGUI2MldsIFShO+Ak00qpPKaXgJo+K********************7gdghaJShhzAsNjt8DE9ulUIlQ0Q95/dZt2jEHcXyLfGNVzDNfFPhvF08NnnGM4="}
```

[]()[]()

#### 响应参数

**Response Header**

参数

是否必选

参数类型

描述

Content-Type

是

String

取值为：application/json; charset=UTF-8

**Response Body**

参数

是否必选

参数类型

描述

resultCode

是

String

结果码，“000000”表示成功，其他表示失败。

resultDesc

是

String

结果描述。

subCode

否

String

业务错误码。

subDesc

否

String

业务错误描述信息。

sign

是

String

签名值。用于开发者对响应报文进行防篡改验证。

mercNo

否

String

商户号。

appId

否

String

应用ID。获取方式请参见[AppID管理及关联](https://developer.huawei.com/consumer/cn/doc/pay-docs/hwzf-appidguanli-0000001757041165)。

sysTransOrderNo

否

String

华为支付系统订单号。

mercOrderNo

是

String

商户订单号，由商户自己生成，商户需保证订单信息唯一性。最大长度46。

orderStatus

是

String

订单状态。

- TRX_SUCCESS：交易成功
- TRX_FAILED：交易失败
- TRX_APPLY：交易处理中
- TRX_PROC：交易处理中

payload

否

String

预留信息，如商户请求时传递该参数，此时会原样返回。

currency

是

String

交易币种单位，最大长度为3。

- CNY （默认，当前仅支持该币种单位）

totalAmount

是

Long

订单总金额，单位：分。

payerAmount

否

Long

买家实付金额，单位：分。

promotionAmount

否

Long

优惠金额，单位：分。

finishTime

否

String

支付完成时间，UTC时间格式（yyyy-MM-dd'T'HH:mm:ss.SSSZ）。

paymentTools

否

String

支付工具。

- WECHAT_MICROPAY：微信小程序支付
- AGMT：快捷
- ACCT：账户余额
- HUAWEIPAY：华为pay

promotionDetail

否

List<[PromotionItem](../../guides/数据模型说明.md#section11685193853815)>

营销信息。

 说明：

当用户支付时参与过营销活动，此字段才会返回。

payer

否

[PayerOut](../../guides/数据模型说明.md#section796891012811)

用户支付时客户端信息。

[]()[]()

#### 响应示例

```ets
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "resultCode": "000000",
  "resultDesc": "Success.",
  "sign": "MEUCIQCO8t5lbWmI+94L1DCah********************2XmM05x1SmFAIrepM9Pg=",
  "currency": "CNY",
  "finishTime": "2023-02-23T10:02:04.000+0800",
  "mercOrderNo": "czl00120240705***",
  "appId": "5765880207853***",
  "mercNo": "10132120***",
  "orderStatus": "TRX_SUCCESS",
  "payerAmount": 10000,
  "payload": "example-payload",
  "paymentTools": "AGMT",
  "promotionAmount": 0,
  "sysTransOrderNo": "12407030857530004914518***",
  "totalAmount": 10000
}
```

[]()[]()

#### 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](../../errors/REST API错误码 (payment-error-code-rest).md#section1187515498410)。

**返回码**

**错误码**

**错误描述**

解决方案

400000

UNKNOW_ERROR

服务暂不可用，请稍后重试

稍后重试。

400000

INVALID_ARGUMENTS

参数不合法

检查请求参数。

400000

PAY_ORDER_NOT_EXIST

支付订单号不存在

检查入参订单号是否正确。

400000

MERC_ORDER_NOT_EXIST

商户订单号不存在

检查入参订单号是否正确。

400000

INVALID_MERCNO

无效商户号

检查入参商户号是否正确。

400000

CHECK_ORDER_STATUS

订单状态异常

请检查是否使用相同订单重复下单。