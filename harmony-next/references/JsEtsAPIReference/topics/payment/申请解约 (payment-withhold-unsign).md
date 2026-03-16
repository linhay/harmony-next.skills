[]()[]()

# 申请解约

[]()[]()

#### 功能介绍

开发者可以调用该接口解约已存在的华为支付签约关系。

[]()[]()

#### 使用场景

在有签约关系的前提下，开发者的应用/元服务可以通过该接口完成某笔签约的解约操作，解约成功后华为支付会回调解约结果给开发者服务器。

[]()[]()

#### 接口原型

承载协议

HTTPS POST

接口方向

开发者服务器 -> 华为支付服务器

接口URL

https://petalpay-developer.cloud.huawei.com.cn/api/v2/contract/unsign

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

**Request Body**

参数

是否必选

类型

说明

contractId

否

String

委托代扣协议ID，签约成功后回调接口中返回。与mercContractCode参数必选其一，同时传递则以contractId为准。

mercContractCode

否

String

商户签约协议号。与contractId参数必选其一，同时传递则以contractId为准。

mercNo

是

String

商户号。

callbackUrl

否

String

回调通知地址，通知URL必须为外网环境可直接访问的URL，要求为https地址。具体要求参考[通知回调接口说明](../../guides/公共说明 (payment-rest-overview).md#section2091445712409)。最大长度为512。

[]()[]()

#### 请求示例

```ets
POST /api/v2/contract/unsign HTTP/1.1
Content-Type: application/json;charset=UTF-8
PayMercAuth: {"callerId":"10132120***","traceId":"202305151442062977847","time":1684132926969,"authId":"120291744647139***","headerSign":"BpOBa8o+gJnKG+vHVI7u********************mVuKDV8iPqNJ+Y8b4XDpSi3FHgjozsWH+uLoTSIg=","bodySign":"lHjrX3dv44zyfu+PO1G+oa9tJi2********************EatA8QTjLPsSPKfM="}
Accept: application/json
{
  "mercContractCode": "2024020316555432***",
  "mercNo": "10132120***"
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

mercNo

否

String

解约商户号。

mercContractCode

否

String

商户签约协议号。

planId

否

String

协议模板ID。该模板ID是商户在向华为支付[提交代扣权限申请](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-password-free-pay-overview)时由华为支付生成。

[]()[]()

#### 响应示例

```ets
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "mercContractCode": "2024020316555432***",
  "resultCode": "000000",
  "sign": "MEUCIQCFNGKlqpBiH********************6h433eRZI9A07c9NiF91jeGRXNUtc0=",
  "planId": "1***",
  "resultDesc": "success",
  "mercNo": "10132120***"
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

CUST_NOT_EXIST

用户不存在或已销户

请切换签约号重试。

400000

INVALID_ARGUMENTS

参数不合法

请检查入参是否正确。