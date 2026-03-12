# 通过mercContractCode查询签约订单信息

#### 功能介绍

开发者可以调用此接口来查询所有通过华为支付签约成功的订单的详细信息。

#### 场景描述

存在签约关系前提下，开发者可以通过该接口查看某笔签约订单的信息，也可以通过主动查询签约订单状态用以完成下一步的业务逻辑，常见的使用场景：

- 支付时由于网络、服务器等异常未收到签约回调通知。
- 调用签约接口返回未知签约状态时。

#### 接口原型

承载协议

HTTPS GET

接口方向

开发者服务器 -> 华为支付服务器

接口URL

https://petalpay-developer.cloud.huawei.com.cn/api/v2/contract/sign/merc-contracts/{mercContractCode}

数据格式

请求消息：Content-Type: application/json; charset=UTF-8

响应消息：Content-Type: application/json; charset=UTF-8

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

**Request Path**

参数

是否必填

参数类型

描述

mercContractCode

是

String

商户签约协议号。商户请求签约时传入的签约协议号。

#### 请求示例

```ets
GET /api/v2/contract/sign/merc-contracts/{mercContractCode} HTTP/1.1
Content-Type: application/json;charset=UTF-8
PayMercAuth:
{"callerId":"10132120***","traceId":"202305151047588466083","time":1684118878350,"authId":"120291744647139***","headerSign":"4Xb1tDGRC4f/B58ANI********************znmsDJOALXgvh/RKeReQBbc4lXZp5wnyZmdwTesmPGdszSNP/s=","bodySign":"kf9AZmVjBSGUI2MldsIFShO+Ak00qpPKaXgJo+K********************7gdghaJShhzAsNjt8DE9ulUIlQ0Q95/dZt2jEHcXyLfGNVzDNfFPhvF08NnnGM4="}
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

mercNo

否

String

签约商户号。

appId

否

String

应用ID。获取方式请参见[AppID管理及关联](https://developer.huawei.com/consumer/cn/doc/pay-docs/hwzf-appidguanli-0000001757041165)。

contractId

否

String

委托代扣协议ID。

mercContractCode

否

String

商户签约协议号。

planId

否

String

协议模板ID。该模板ID是商户在向华为支付[提交代扣权限申请](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-password-free-pay-overview)时由华为支付生成。

signedTime

否

String

签约时间，格式：yyyy-MM-dd hh:mm:ss。

expireDate

否

String

签约过期时间，格式：yyyy-MM-dd。

signStatus

否

String

签约状态。

- 1：已签约
- 9：已解约

payer

否

[PayerOut](数据模型说明.md#section796891012811)

用户支付时客户端信息。

#### 响应示例

```ets
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "mercContractCode": "2024020316555432***",
  "signedTime": "2023-09-01 09:01:25",
  "resultCode": "000000",
  "sign": "MEUCIQDQ206irxpkVWGQPN*************Dvy1CaNnXaKU+uZBnrJmdhm5aG4JM=",
  "contractId": "2024070914615843071097***",
  "planId": "1***",
  "resultDesc": "success",
  "mercNo": "10132120***"
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

CUST_NOT_EXIST

用户不存在或已销户

请更换签约号重试。

400000

CHECK_CONTRACT_STATUS

签约号无效

1. 请确认是否存在签约关系。
1. 检查签约号输入是否正确。