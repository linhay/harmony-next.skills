# 通过mercContractCode查询签约信息

**功能介绍**

开发者可以调用此接口来查询所有通过华为支付签约成功的详细信息。

**场景描述**

存在签约关系前提下，开发者可以通过该接口查看某笔签约信息，也可以通过主动查询签约状态用以完成下一步的业务逻辑，常见的使用场景：

-

支付时由于网络、服务器等异常未收到签约回调通知。

-

调用签约接口返回未知签约状态时。

**接口原型**

-

承载协议： HTTPS GET

-

接口方向： 开发者服务器 -> 华为支付服务器

-

接口URL： https://petalpay-developer.cloud.huawei.com.cn/api/v1/partner/contract/sign/merc-contracts/{mercContractCode}

-

数据格式：

请求消息：Content-Type: application/json

响应消息：Content-Type: application/json

**请求参数**

Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：PayMercAuth的JSON串 |

Request path

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| mercContractCode | 是 | String | 商户签约协议号。商户请求签约时传入的签约协议号，商户侧须唯一。最大长度64。 |

**请求示例**

```ets
GET /api/v1/partner/contract/sign/merc-contracts/{mercContractCode} HTTP/1.1
Content-Type: application/json;charset=UTF-8
PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+KYaq1jD********************eR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TIkT********************xUasPj10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
```

**响应参数**

Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

Response Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 返回码，"000000"表示成功，其他表示见错误码。 |
| resultDesc | 是 | String | 结果描述。 |
| subCode | 否 | String | 业务错误码。 |
| subDesc | 否 | String | 业务错误描述信息。 |
| sign | 是 | String | 签名值。用于开发者对响应报文进行防篡改验证。 |
| spMercNo | 是 | String | 合作伙伴父商户号。最大长度12。 |
| subMercNo | 否 | String | 合作伙伴子商户号。最大长度12。 |
| spAppId | 否 | String | 合作伙伴父商户关联的应用ID。 |
| subAppId | 否 | String | 合作伙伴子商户关联的应用ID。 说明： 平台子商户当前不支持绑定AppID，平台类商户请求传递该入参可能导致校验异常。 |
| contractId | 否 | String | 委托代扣协议ID。 |
| mercContractCode | 否 | String | 商户签约协议号。 |
| planId | 否 | String | 协议模板ID。该模板ID是商户在向华为支付提交代扣权限申请时由华为支付生成。 |
| signedTime | 否 | String | 签约时间，格式：yyyy-MM-dd hh:mm:ss。 |
| expireDate | 否 | String | 签约过期时间，格式：yyyy-MM-dd。 |
| signStatus | 否 | String | 签约状态。 1：已签约 9：已解约 |
| payer | 否 | PayerOut | 用户支付时客户端信息。 |

**响应示例**

```ets
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "mercContractCode": "2024020316555432***",
  "signedTime": "2023-09-01 09:01:25",
  "resultCode": "000000",
  "sign": "MEUCIQDQ206irxpkVWGQPN3********************gsKCEyx/O9Dvy1CaNnXaKU+uZBnrJmdhm5aG4JM=",
  "contractId": "2024070914615843071097***",
  "planId": "1***",
  "resultDesc": "success",
  "spMercNo": "10132120***"
}
```

**错误码**

resultCode非400000的错误码请看[公共错误码说明](REST API错误码.md#ZH-CN_TOPIC_0000002522082504__公共错误码说明)。

| 返回码 | 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- | --- |
| 400000 | UNKNOW_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |
| 400000 | CUST_NOT_EXIST | 用户不存在或已销户 | 请更换签约号重试。 |
| 400000 | CHECK_CONTRACT_STATUS | 签约号无效 | 1. 请确认是否存在签约关系。 2. 检查签约号输入是否正确。 |