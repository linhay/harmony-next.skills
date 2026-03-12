# 通过combinedMercOrderNo查询订单信息

#### 功能介绍

开发者可以调用此接口查询已经在华为支付创建成功的合单支付订单详细信息。

resultCode返回“000000”表示查询支付订单成功，不代表支付订单成功，订单状态需根据orderStatus字段判断。

#### 场景描述

用户已完成合单支付，开发者调此接口获取合单支付订单信息。

#### 接口原型

承载协议

HTTPS GET

接口方向

开发者服务器 -> 华为支付服务器

接口URL

https://petalpay-developer.cloud.huawei.com.cn/api/v2/partner/combined/transactions/merc-orders/{combinedMercOrderNo}

数据格式

请求消息：Content-Type: application/json

响应消息：Content-Type: application/json

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

取值为：[PayMercAuth](数据模型说明.md#section11744172016145)的JSON字符串

**request path**

参数

是否必填

参数类型

描述

combinedMercOrderNo

是

String

商户合单支付主单订单号。

#### 请求示例

```ets
GET /api/v2/partner/combined/transactions/merc-orders/{combinedMercOrderNo} HTTP/1.1
Content-Type: application/json;charset=UTF-8
PayMercAuth: {"callerId":"10132120***","traceId":"202305151047578634337","time":1684118877557,"authId":"120291744647139***","headerSign":"FB0vzUONHsvsurnKHZhc4*******************sZ3oJYeLt/4Da5n3DLXlSKYFmE=","bodySign":"DDRuPlG/QFb3OQTNHLIOaNFKnQ********************kvvni+9cVmsqHir0bRFLANqqh2zyzv4="}
```

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

结果码，"000000"表示成功，其他表示失败。

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

combinedSysTransOrderNo

否

String

华为支付合单支付交易订单号。

combinedMercOrderNo

否

String

商户生成的合单支付主订单号。

combinedAppId

否

String

商户申请并关联的应用id。

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

合单商户下单时传入的预留字段，原样返回。

subOrders

否

List<[SubOrderResult](数据模型说明.md#section883324283110)>

合单支付子订单信息。

payer

否

[PayerOut](数据模型说明.md#section796891012811)

用户支付时客户端信息。

#### 响应示例

```ets
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
    "resultCode": "000000",
    "resultDesc": "Success.",
    "sign": "MEYCIQDOsSJ5gL9mcYKi9usz4I/u********************77jclylTWJOTThPxOdJs+2zsDv3sg38UY/Wy",
    "combinedSysTransOrderNo": "12407030857530004914518***",
    "payload": "example-payload",
    "combinedMercOrderNo": "czl00120240705***",
    "orderStatus": "TRX_SUCCESS",
    "subOrders": [
        {
            "sysTransOrderNo": "12407030857530004914518***",
            "mercOrderNo": "czl00120240705***",
            "orderStatus": "TRX_SUCCESS",
            "payload": "example-payload",
            "currency": "CNY",
            "totalAmount": 40,
            "payerAmount": 1,
            "paymentTools": "AGMT"
        }
    ]
}
```

#### 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](REST API错误码.md#section1187515498410)。

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