[]()[]()

# 预下单

[]()[]()

#### 功能介绍

商户服务端调用此接口获取预支付ID（prepayId）。

[]()[]()

#### 场景描述

开发者接入合单支付，首先需要调用该接口获取到prepayId，然后将prepayId组参返回给客户端调用支付接口拉起华为支付收银台。

[]()[]()

#### 接口原型

承载协议

HTTPS POST

接口方向

开发者服务器-> 华为支付服务器

接口URL

https://petalpay-developer.cloud.huawei.com.cn/api/v2/partner/combined/preorder/create/app

 说明：

元服务预下单接口请使用以下URL：

https://petalpay-developer.cloud.huawei.com.cn/api/v2/partner/combined/preorder/create/fa

数据格式

请求消息：Content-Type: application/json

响应消息：Content-Type: application/json

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

取值为：[PayMercAuth](../../guides/数据模型说明.md#section11744172016145)的JSON串

**Request Body**

参数

是否必选

类型

说明

combinedMercOrderNo

是

String

合单支付商户主订单号，由商户自己生成，**商户需保证订单信息唯一性**。最大长度46。

combinedAppId

是

String

合单支付商户关联的应用id。

combinedMercNo

是

String

合单支付发起方商户号。

tradeSummary

是

String

合单支付交易摘要。最大长度128。

subOrders

是

List<[SubMercOrder](../../guides/数据模型说明.md#section760421624415)>

合单支付子订单信息。

callbackUrl

是

String

回调通知地址，通知URL必须为外网环境可直接访问的URL，要求为https地址。具体要求参考[通知回调接口说明](../../guides/公共说明 (payment-rest-overview).md#section2091445712409)。最大长度为512。

payload

否

String

商户预留信息，在查询和回调通知时会原样返回。最大长度255。

expireTime

否

String

交易过期时间。此时间必须为准确的UTC时间。

格式要求："yyyy-MM-dd'T'HH:mm:ss.SSSZ" 。

 说明：

- 下单过期时间，不传默认2个小时，如果传递则最小值无限制，最大180天，超过180天系统会报错。
- 传已过时间可能会导致订单因过期、超时等原因异常关闭。
- 开发者可以参考如下函数获取对应的UTC过期时间：

```ets
/**
* 获取UTC格式的过期时间
* **@param ***expectedExpiredTime *交易过期时间，请换算为分钟
* **@return **UTC时间
*/
private static String getTradeExpireTime(int expectedExpiredTime) {
     SimpleDateFormat formater = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSZ");
     formater.setTimeZone(TimeZone.*getTimeZone*("UTC"));
     Calendar calendar = Calendar.*getInstance*();
     calendar.set(Calendar.*MINUTE*, calendar.get(Calendar.*MINUTE*) + expectedExpiredTime);
      return formater.format(calendar.getTime());
 }
```

payer

否

[PayerIn](../../guides/数据模型说明.md#section20529174721111)

支付者信息。

[]()[]()

#### 请求示例

```ets
POST /api/v2/partner/combined/preorder/create/app HTTP/1.1
Content-Type: application/json;charset=UTF-8
PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELY******************Yaq1jDH/+VmefC29ZXpK54c5DwKJH7rMv6SB******************N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSp******************xPAHE0TIkTxHMcUWx7N6405QrcBimTcTN7pBpFA7pvFexUasPj10******************vta6J5UxIUmAp+wGdV/juGEvQ="}
Accept: application/json
{
  "combinedAppId":"5765880207853***",
  "combinedMercNo": "10132120***",
  "combinedMercOrderNo": "czl00120240705***",
  "callbackUrl": "https://www.xxxxxx.com/hw/pay/callback",
  "subOrders": [
    {
      "allocationType": "NO_ALLOCATION",
      "currency": "CNY",
      "totalAmount": 100,
      "tradeSummary": "xx服务-杂志报刊",
      "mercNo": "10132120***",
      "mercOrderNo": "czl00120240705***",
      "payload": "example-payload"
    }
  ],
  "tradeSummary": "xx服务-合单交易摘要"
}
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

返回码，"000000"表示成功，其他表示见错误码。

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

prepayId

是

String

预支付ID。有效期10分钟。

combinedMercOrderNo

否

String

合单支付商户主订单号。

[]()[]()

#### 响应示例

```ets
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "resultCode": "000000",
  "resultDesc": "Success.",
  "sign": "MEQCIEIWzdpziRyTi8vhwWHFuDdxfsiw**********YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
  "prepayId": "12407091401520894056950***",
  "combinedMercOrderNo": "2023032******118876122"
}
```

[]()[]()

#### 错误码

(**resultCode**非400000的错误码请看[公共错误码说明](../../errors/REST API错误码 (payment-error-code-rest).md#section1187515498410))

**返回码**

**错误码**

**错误描述**

解决方案

400000

INVALID_ARGUMENTS

参数不合法

检查请求参数。

400000

CHECK_ORDER_STATUS

订单状态异常

请检查是否使用相同订单重复下单。